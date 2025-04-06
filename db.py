import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="shahiil@2005",
        database="feedback_db"
    )
