# function to store data in dictionary form within a list
def inventory_register(product_name,quantity,unit_value,daily_sales: list):
    update = {"name":product_name,
         "quantity" : quantity,
         "unitvalue" : unit_value
         }
    daily_sales.append(update)
# function to display the contents of the list in an ordered manner
def show_summary(daily_sales: list):
    for i in daily_sales:
        print(f"{i['name']} \nQuantity of product in the inventory: {i['quantity']} \nPrice per unit: ${i['unitvalue']}\nTotal value of the product in inventory: ${i['unitvalue']*i['quantity']}")
        print("--------------------")