import mysql.connector

def connection():
    return mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "testdb1"
    )
    
