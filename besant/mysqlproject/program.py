
import mysql.connector
from faker import Faker
import random
import mysql.connector
from mysql.connector import Error
import pandas as pd
# import scikitlearn
    
hostname = "localhost"
database = "grocery_store"
port = "3306"
username = "root"
password = "Deepak123"

try:
    connection = mysql.connector.connect(host=hostname, database=database, user=username, password=password, port=port)
    if connection.is_connected():
        db_Info = connection.server_info
        print("Connected to MySQL Server version", db_Info)

        cursor = connection.cursor()

        # Step 1: Create grocery_store table
        print("creating the table")
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS grocery_store_cus (
            customer_id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            email VARCHAR(100) UNIQUE,
            phone VARCHAR(100),
            address VARCHAR(500),
            total_spent DECIMAL(60,2)
        )
        """)

        print("generating the data")
        # Step 2: Generate 100 sample customer records
        fake = Faker()
        customers = []

        for _ in range(100):
            name = fake.name()
            email = fake.unique.email()
            phone = fake.phone_number()
            address = fake.address().replace("\n", ", ")
            total_spent = round(random.uniform(100, 5000), 2)
            customers.append((name, email, phone, address, total_spent))

        query = """
                INSERT INTO grocery_store_cus (name, email, phone, address, total_spent)
                VALUES (%s, %s, "%s, %s, %s)
                """
        print("loading the data to db")
        cursor.executemany(query, customers)
        print("data loaded successfully ")

        print("fetching the data from cloud")
        # cursor.execute("select * from grocery_store_cus")
        # record = cursor.fetchall()
        # print("customer records: ", record)

        df = pd.read_sql_query("select * from grocery_store_cus", connection)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        connection.commit()
        cursor.close()
        connection.close()
        print("MySQL connection is closed")


import mysql.connector
from faker import Faker
import random
import mysql.connector
from mysql.connector import Error
import pandas as pd
# import scikitlearn
    
hostname = "k76zi1.h.filess.io"
database = "Sampledb_programcup"
port = "3307"
username = "Sampledb_programcup"
password = "8a9204ac825bd0589049d25f67da6d8047c5087c"

try:
    connection = mysql.connector.connect(host=hostname, database=database, user=username, password=password, port=port)
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()

        # Step 1: Create grocery_store table
        print("creating the table")
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS grocery_store_cus (
            customer_id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            email VARCHAR(100) UNIQUE,
            phone VARCHAR(100),
            address VARCHAR(500),
            total_spent DECIMAL(60,2)
        )
        """)

        print("generating the data")
        # Step 2: Generate 100 sample customer records
        fake = Faker()
        customers = []

        for _ in range(100):
            name = fake.name()
            email = fake.unique.email()
            phone = fake.phone_number()
            address = fake.address().replace("\n", ", ")
            total_spent = round(random.uniform(100, 5000), 2)
            customers.append((name, email, phone, address, total_spent))

        query = """
                INSERT INTO grocery_store_cus (name, email, phone, address, total_spent)
                VALUES (%s, %s, %s, %s, %s)
                """
        print("loading the data to db")
        cursor.executemany(query, customers)
        print("data loaded successfully ")

        print("fetching the data from cloud")
        # cursor.execute("select * from grocery_store_cus")
        # record = cursor.fetchall()
        # print("customer records: ", record)

        df = pd.read_sql_query("select * from grocery_store_cus", connection)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        connection.commit()
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

