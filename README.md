# ECSE3038 Tutorial 3 - FastAPI Fruit Inventory API

## **Project Overview**
This project is a **RESTful API** for managing a **Fresh Fruit Inventory System**, built using **FastAPI**.  
It allows users to **add, update, retrieve, and mark fruits as unavailable** while maintaining proper data validation.

This code was written as part of **ECSE3038 Tutorial 3** to help students understand **FastAPI and REST API concepts**.

---

## **API Endpoints & Function Behavior**

### **1️ GET /api/fruits**
**Function:** `get_all_fruits()`  
- Returns a list of all **available** fruits in the inventory.
- Filters out any fruits marked as **unavailable**.

---

### **2️ GET /api/fruits/{id}**
**Function:** `get_single_fruit(id: int)`  
- Returns detailed information about a **specific fruit**.
- If the fruit does not exist, returns `404 Not Found`.

---

### **3️ POST /api/fruits**
**Function:** `add_fruit(fruit: Fruit)`  
- Adds a **new fruit** to the inventory.
- Automatically sets a **creation date** on the server side.
- Returns the **created fruit object**.

---

### **4️ PATCH /api/fruits/{id}**
**Function:** `update_fruit(id: int, available: Optional[bool], price: Optional[float], quantity: Optional[int])`  
- Allows updating only the following attributes:
  - `available` (True/False)
  - `price`
  - `quantity`
- Prevents updating other fruit details.
- Returns `400 Bad Request` if **price or quantity is negative**.
- Returns `404 Not Found` if fruit does not exist.

---

### **5️ DELETE /api/fruits/{id}**
**Function:** `delete_fruit(id: int)`  
- Marks a fruit as **unavailable** instead of deleting it.
- If the fruit is already unavailable, returns `400 Bad Request`.
- If the fruit does not exist, returns `404 Not Found`.

---

