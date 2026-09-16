import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Morpheus@sql26",
    database="shop_db                                            "
    )

if conn.is_connected():
    print("Connected successfully!")

cursor = conn.cursor()

cursor.execute( 
    "CREATE TABLE IF NOT EXISTS products (" 
    "id INT AUTO_INCREMENT PRIMARY KEY," 
    "product_name VARCHAR(100)," 
    "price FLOAT," 
    "quantity INT"
    ")"
    )

sql="INSERT INTO products (product_name, price, quantity) VALUES (%s, %s, %s)"
values = ("Laptop", 55000, 5)
cursor.execute(sql, values)
conn.commit()

sql="INSERT INTO products (product_name, price, quantity) VALUES (%s, %s, %s)"
values = ("mouse", 800, 20)
cursor.execute(sql,values)
conn.commit()

sql="INSERT INTO products (product_name, price, quantity) VALUES (%s, %s, %s)"
values =("keyboard", 1500, 10)
cursor.execute(sql,values)
conn.commit()