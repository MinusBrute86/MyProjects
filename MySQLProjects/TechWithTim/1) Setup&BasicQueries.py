import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="R@mpage21!",
    database="testdatabase"  # Inserted after running 'CREATE DATABASE'
)

mycursor = db.cursor()

# Creates Database
# mycursor.execute("CREATE DATABASE testdatabase")