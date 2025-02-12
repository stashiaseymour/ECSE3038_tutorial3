from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

app = FastAPI()

# Fruit Model
class Fruit(BaseModel):
    name: str
    variety: str
    quantity: int
    supplier: str
    harvest_date: datetime
    available: bool
    price: float

# Database Model with ID & Creation Date
class FruitDB(Fruit):
    id: int
    creation_date: datetime

# Mock Database
fruit_inventory: List[FruitDB] = []
fruit_id_counter = 1

# GET All Available Fruits
@app.get("/api/fruits", response_model=List[FruitDB])
def get_all_fruits():
    """Returns all available fruits in inventory."""
    return [fruit for fruit in fruit_inventory if fruit.available]

# GET a Single Fruit by ID
@app.get("/api/fruits/{id}", response_model=FruitDB)
def get_single_fruit(id: int):
    """Returns details of a specific fruit by ID."""
    for fruit in fruit_inventory:
        if fruit.id == id:
            return fruit
    raise HTTPException(status_code=404, detail="Fruit not found")

# POST - Add a New Fruit
@app.post("/api/fruits", response_model=FruitDB, status_code=201)
def add_fruit(fruit: Fruit):
    """Adds a new fruit to the inventory, setting creation date automatically."""
    global fruit_id_counter
    new_fruit = FruitDB(
        id=fruit_id_counter,
        creation_date=datetime.utcnow(),
        **fruit.dict()
    )
    fruit_inventory.append(new_fruit)
    fruit_id_counter += 1
    return new_fruit

# PATCH - Update a Fruit (Availability, Price, Quantity)
@app.patch("/api/fruits/{id}", response_model=FruitDB)
def update_fruit(id: int, available: Optional[bool] = None, price: Optional[float] = None, quantity: Optional[int] = None):
    """Updates availability, price, or quantity of a fruit."""
    global fruit_inventory

    for fruit in fruit_inventory:
        if fruit.id == id:
            if available is not None:
                fruit.available = available
            if price is not None:
                if price < 0:
                    raise HTTPException(status_code=400, detail="Price cannot be negative")
                fruit.price = price
            if quantity is not None:
                if quantity < 0:
                    raise HTTPException(status_code=400, detail="Quantity cannot be negative")
                fruit.quantity = quantity

            return fruit

    raise HTTPException(status_code=404, detail="Fruit not found")

# DELETE - Mark a Fruit as Unavailable
@app.delete("/api/fruits/{id}")
def delete_fruit(id: int):
    """Marks a fruit as unavailable instead of deleting it."""
    for fruit in fruit_inventory:
        if fruit.id == id:
            if not fruit.available:
                raise HTTPException(status_code=400, detail="Fruit is already unavailable")
            fruit.available = False
            return {"message": f"Fruit with ID {id} marked as unavailable", "status": "success"}

    raise HTTPException(status_code=404, detail="Fruit not found")
