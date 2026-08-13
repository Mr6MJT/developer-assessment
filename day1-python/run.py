# Part A


# try:
#     users = [
#         {"id": 1, "name": "John", "active": True},
#         {"id": 2, "name": "Maria", "active": False},
#         {"id": 2, "name": "layla", "active": false},
#         {"id": 3, "name": "David", "active": True}
#     ]
    
#     def get_active_users(users):
#         result = []
#         for user in users:
#             if user["active"] == True:
#                 try:
#                     result.append(user["name"])
#                     return result
#                 except NameError:
#                     return 0
#     print(get_active_users("users"))
# except NameError:
#     print("ERROR in DATA List")



# PART B:

import json



# with open("db.json", "r") as ReadFromDB:
#     dataa = json.load(ReadFromDB)
#     print(dataa)

def add_product(sku, product, category, qty, price):
    newproduct = [{"sku":sku, "product": product, "category": category, "quantity": qty, "price": price}]
    with open("db.json", "w") as WriteToDB:
        json_str = json.dumps(newproduct, indent=5)
        WriteToDB.write(json_str)
    return 0

def update_product(sku, neww_sku, neww_prname, neww_category, neww_quantity, neww_price):

    return 0

def delete_product(sku):

    return 0

def find_product(sku):
    with open("db.json", "r") as ReadFromDB:
        data = json.load(ReadFromDB)    
    try:
        print(data[sku]["product"]["category"]["quantity"]["price"])
    except KeyError:
        print("SKU doesn't exist")
    return 0

def list_product():
    with open("db.json", "r") as ReadFromDB:
        data = json.load(ReadFromDB)
        print(data)
    return 0

def calculate_inventory_value():
    with open("db.json", "r") as ReadFromDb:
        data = json.load(ReadFromDb)
    x = 0
    for product in data:
        x = x + product["quantity"] * product["price"]
    return x
y = 1
while y == 1:
    print("Choose Number:\n")
    print(" 1- To add new product \n 2- Update Existing Product \n 3- Delete Existing Product \n 4- Find Existing Product \n 5- List All Products \n 6- Calculate Inventory Value")
    func = int(input("USER: "))
    if func == 1:
        
        sku = str(input("SKU: "))
        product = str(input("Product: "))
        category = str(input("Category: "))
        qty = int(input("Quantity: "))
        price = float(input("Price: "))
        add_product(sku, product, category, qty, price)

    elif func == 2:
        
        sku = str(input("Enter SKU of the product: "))
        what_to_update = int(input("1- Update SKU \n 2- Update Product Name \n 3- Update Category \n 4- Update Quantity \n 5- Update Price \n ###: ")) 
        if what_to_update == 1:
            new_sku = str(input("Enter new SKU: "))
            update_product(sku, neww_sku=new_sku)
        elif what_to_update == 2:
            new_prname = str(input("Enter new Product Name: "))
            update_product(sku, neww_prname=new_prname)
        elif what_to_update == 3:
            new_category = str(input("Enter new Category Name: "))
            update_product(sku, neww_category=new_category)

        elif what_to_update == 4:
            new_quantity = int(input("Enter new Quantity: "))
            update_product(sku, neww_quantity=new_quantity)
        elif what_to_update == 5:
            new_price = float(input("Enter new price: "))
            update_product(sku, neww_price=new_price)
        else :
            print("That\'s not an option!") 


    elif func == 3:
        sku = str(input("Enter SKU of the product you want to delete: "))

        delete_product(sku=sku)

    elif func == 4:
        sku = str(input("Enter SKU of the product you want to find: "))
        print(find_product(sku=sku))
    
    elif func == 5:

        print(list_product())

    elif func == 6:
        print (calculate_inventory_value())

    else:
        print("That\'s not an option!")

    y = 2


