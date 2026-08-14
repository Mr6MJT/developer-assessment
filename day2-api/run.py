# cur.execute("CREATE TABLE products(sku, name, category, quantity, price)")
# cur.execute("""
#     INSERT INTO products VALUES
#         ('iphoneh17du', 'Iphone 17 pro max', 'smart phones', 47, 1999.99),
#         ('amfjue72n', 'Laptop HP 512/16 14inch', 'laptops', 13, 1300.20)
# """)
# con.commit()

# res = cur.execute("SELECT sku, name FROM products")
# res.fetchall()
# print(res)


from fastapi import FastAPI
import sqlite3
from pydantic import BaseModel
from fastapi import Request

con = sqlite3.connect("products.db")

class Product(BaseModel):
    sku: str
    name: str
    category: str 
    quantity: int
    price: float



cur = con.cursor()



app = FastAPI()

@app.get("/products")
async def list_products():
    res=cur.execute("SELECT * FROM products")
    result = res.fetchall()
    return {result}


@app.get("/products/{sku}")
async def read_product(sku: str):
    res=cur.execute(f"SELECT ALL FROM products WHERE sku = '{sku}' ")
    result = res.fetchall()
    if result == 0:
        return {"404"}
    else:
        return {result}

@app.post("/products/")
async def create_product(request: Product):
    sku = request["sku"]
    name = request["name"]
    category = request["category"]
    quantity = request["quantity"]
    price = request["price"]

    res=cur.execute(f"SELECT ALL FROM products WHERE sku = '{sku}' ")
    result = res.fetchall()
    if result != 0:
        return {"404"}
    else:
        res=cur.execute(f"INSERT INTO products VALUES ({sku}, {name}, {category}, {quantity}, {price})")
        return {"Registered Succesfully"}


@app.put("/products/{sku}")
async def update_item(sku: str, request: Item):
    sku = request["sku"]
    name = request["name"]
    category = request["category"]
    quantity = request["quantity"]
    price = request["price"]

    res=cur.execute(f"SELECT ALL FROM products WHERE sku = '{sku}' ")
    result = res.fetchall()
    if result != 0:
        return {"This product is already registered"}
    else:
        res=cur.execute(f"INSERT INTO products VALUES ({sku}, {name}, {category}, {quantity}, {price})")
        return {"Registered Succesfully"}



@app.delete("/products/{sku}")
async def delete_item(sku: str):
    res=cur.execute(f"DELETE FROM products WHERE sku = '{sku}' ")
    return {res}



@app.get("/products/low-stock/")
async def get_low_sock():
    res=cur.execute(f"SELECT * FROM products WHERE quantity <= 5")
    return {res}


@app.get("/inventory/statistics/")
async def get_statistics():
    total_products=cur.execute(f"SELECT * FROM products WHERE quantity <= 5")
    total_quantity=cur.execute(f"SELECT COUNT(quantity) FROM products")
    low_stock_products=cur.execute(f"SELECT COUNT(sku) FROM products WHERE quantity <= 5")
    inventory_value=cur.execute(f"SELECT SUM(price)*SUM(quantity) FROM products")
    return {"total products":total_products , "total quantity" : total_quantity , "low stock products" : low_stock_products , "inventory value": inventory_value }

