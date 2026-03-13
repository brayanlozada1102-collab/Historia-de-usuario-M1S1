# Historia-de-usuario-M1S1
# Inventory Management System

A Python-based inventory management tool designed for product registration and total cost calculation.

## Description
This program captures product data including name, price, and quantity. It features input validation to prevent runtime errors and ensure data integrity. Upon completion, the system generates a detailed summary and calculates the cumulative total value of the inventory.

## Features
* **Data Validation:** Implements `try/except` blocks to ensure prices are processed as floats and quantities as integers.
* **Modular Design:** Separation of concerns between the entry point (`main.py`) and business logic (`logicinventory.py`).
* **Dynamic Management:** Utilizes lists and dictionaries to handle multiple records within a single execution session.

## Project Structure
* `main.py`: The main entry point containing the user interaction loop.
* `logicinventory.py`: External module containing the `inventory_register` and `show_summary` functions.
* `README.md`: Technical documentation of the project.

## Requirements
* Python 3.x.
* Ensure `logicinventory.py` is located in the same directory as the main execution file.

## Usage Instructions
1. Run the application from the terminal: `python main.py`.
2. Enter the product name when prompted.
3. Provide the unit price and quantity; the system will reject negative values or non-numeric inputs.
4. Type `yes` to continue recording items or any other key to terminate and view the summary.

## Example Execution
```text
Enter the product name: Monitor
Enter the unit price: 150.00
Enter the inventory quantity: 5
Do you want to continue recording sales? Yes/No: no

Inventory 
-----------------------
[Product details list]
The total inventory values: $750.0