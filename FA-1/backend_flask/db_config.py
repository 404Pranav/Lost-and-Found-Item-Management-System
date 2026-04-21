import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="adityab2206",
    database="lost_found_db"
)

cursor = db.cursor(dictionary=True)