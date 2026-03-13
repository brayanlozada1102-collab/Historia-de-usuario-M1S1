
def inventory_register(product_name,quantity,unit_value,daily_sales: list):
    update = {"name":product_name,
         "quantity" : quantity,
         "unitvalue" : unit_value
         }
    daily_sales.append(update)

def show_summary(daily_sales: list):
    for i in range(len(daily_sales)):
        print(f"{daily_sales[i]['name']} \nQuantity of product in the inventory: {daily_sales[i]['quantity']} \nPrice per unit: ${daily_sales[i]['unitvalue']}\nTotal value of the product in inventory${daily_sales[i]['unitvalue']*daily_sales[i]['quantity']}")
        print("--------------------")