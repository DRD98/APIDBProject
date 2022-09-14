import mysql.connector
from rest_framework.decorators import api_view

api_view()

def dbconnection():
    db1 = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "whocares@MySQL98!",
        database = "db1"
    )
    return db1

db = dbconnection()
mycursor = db.cursor()
mycursor.execute("""ALTER TABLE Employee ADD Location VARCHAR(50) NULL""")