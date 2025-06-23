import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="nimbA@1997",  # 🔐 Replace this
        database="flipkart_data"
    )
