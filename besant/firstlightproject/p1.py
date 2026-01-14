import sqlite3

# Establish a persistent database connection
conn = sqlite3.connect('grocery_store.db')
cursor = conn.cursor()


# Create the customers table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers  (
        id INTEGER PRIMARY KEY,
        name TEXT,
        favorite_product TEXT
    )
""")

# CRUD operations
def create_customer(id, name, favorite_product):
    cursor.execute("INSERT INTO customers VALUES (?, ?, ?)", (id, name, favorite_product))

def read_all():
    cursor.execute("SELECT * FROM customers")
    res = cursor.fetchall()
    for i in res:
        print(i)

def read_customer(id):
    cursor.execute("SELECT * FROM customers WHERE id=?", (id,))
    return cursor.fetchmany()

def update_customer(id, name, favorite_product):
    cursor.execute("UPDATE customers SET name=?, favorite_product=? WHERE id=?", (name, favorite_product, id))

def delete_customer(id):
    cursor.execute("DELETE FROM customers WHERE id=?", (id,))



create_customer(id=1,name='Mahesh',favorite_product='salt Biscuit')
create_customer(id=2,name='kiran',favorite_product='cake')
create_customer(id=3,name='Karan',favorite_product='puffs')
print(read_all())
update_customer(id=1,name='Mahesh kumar',favorite_product= 'salt Biscuit')
print(read_all())
delete_customer(id=1)
print(read_all())


cursor.close()
conn.close()

import pprint

# importing module
from pymongo import MongoClient


hostname = "b0n8-k.h.filess.io"
database = "Sampledb_struckadd"
port = "27017"
username = "Sampledb_struckadd"
password = "8d1ebf9da5ed84253f280aaa6663b208338cfdbf"

uri = "mongodb://" + username + ":" + password + "@" + hostname + ":" + port + "/" + database

# Connect with the portnumber and host
client = MongoClient(uri)

# Access database
mydatabase = client[database]
