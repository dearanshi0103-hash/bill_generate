import time as t
import mysql.connector


def bill():
    con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MySqlAnshika@123", #enter your password
    database="amazon" #enter your database name
    )
    cur = con.cursor()
    product_id=int(input("enter the product id: "))
    product_Name=input("enter the product name: ")
    price=float(input("enter the Price: "))
    category=input("enter the category:")
    quantity=int(input("enter the Quantity: "))
    rating=float(input("enter the rating:"))
    price=price*quantity
    sql = "INSERT INTO Product (product_id,product_name,price,category,quantity, rating,) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    values = (product_id,product_Name,price, category,quantity,rating,price)
    cur.execute(sql,values)
    con.commit()
    print("✅ Data successfully inserted into Products table!")

    price=price*quantity
    name=str(product_id)
    time=t.ctime()
    f = open(name + ".txt", "w")
    data=f.write(f'''
    Time: {time}
    --------------------
    product id: {product_id}
    product name: {product_Name}
    quantity: {quantity}
    ---------------------
    final price: {price}''')
    f.close()
    cur.close()
    con.close()
    
bill()