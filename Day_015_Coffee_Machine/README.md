# Day 15 - Coffee Machine Project

This is the first big project combining loops, dictionaries, and functions.

### ☕️ Features
- 3 Drinks: Espresso ($1.5), Latte ($2.5), Cappuccino ($3.0)
- Checks resources: Water, Milk, Coffee
- Processes coins: quarters, dimes, nickles, pennies
- Gives change and updates profit
- Two secret commands: `report` and `off`

### 🧠 Concepts Used
- Nested Dictionaries (MENU)
- Functions with return
- While loop for machine running
- Real-world logic building

### 🔧 How It Works
1. `is_resource_sufficient()` - Checks if ingredients are enough
2. `process_coins()` - Calculates total money inserted
3. `is_transaction_successful()` - Checks if money is enough
4. `make_coffee()` - Deducts ingredients and serves coffee

### ▶️ Run
```bash
python main.py