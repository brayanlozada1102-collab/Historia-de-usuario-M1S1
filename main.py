# Function import
from logicinventory import inventory_register , show_summary
# INVENTORY REGISTRATION PROGRAM
inventory_valeu = 0
daily_sales = []

def main(inventory_valeu,daily_sales:list):
 print("Welcome to the inventory registration system \n -----------------------")
 start = True


 while start:
     # Request the product name
     name = input("Enter the product name: ")
     # Request and validate the price (must be a decimal/float)
     try:
        price = float(input("Enter the unit price: "))
        if price <= 0:
            print("Error: The price cannot be negative.")
            continue
     except ValueError:
        print("Error: Please enter a numeric value for the price.")
        continue
     # Request and validate the quantity (must be an integer/int)
     try:
        quantity = int(input("Enter the inventory quantity: "))
        if quantity <= 0:
            print("Error: The quantity cannot be negative.")
            continue
     except ValueError:
        print("Error: Please enter a whole number for the quantity.")
        continue

     inventory_register(name,quantity,price,daily_sales)
     # Mathematical operation: Calculate total inventory cost
     # Price (float) is multiplied by quantity (int)
     inventory_valeu = inventory_valeu + (quantity*price)
     # Question to validate continuity
     try:
       switch = input("Do you want to continue recording products? Yes/No: ").lower()
       if switch != "yes":
           start = False
     except ValueError:
        print("Error try again")



 # Display results in console.
 print("\nInventory \n-----------------------")
 show_summary(daily_sales)
 print(f"The total inventory values: ${inventory_valeu}")

# General comment:
# This program allows registering a product by capturing its name, price, and quantity.
# It includes data type validation to ensure the total cost calculation 
# (price * quantity) is performed without execution errors.
if __name__ == "__main__":
    main(inventory_valeu,daily_sales)