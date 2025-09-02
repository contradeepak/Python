import mysql.connector


def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",          # your username
        password="Deepak123",  # your MySQL password
        database="todolist_db"
    )
