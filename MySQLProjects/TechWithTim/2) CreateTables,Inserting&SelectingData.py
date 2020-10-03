import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="R@mpage21!",
    database="testdatabase"  # Inserted after running 'CREATE DATABASE'
)

mycursor = db.cursor()
x, y = ("Nikki", 26)

# Create Table in MySQL
'''mycursor.execute("CREATE TABLE Person (name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY "
                    "AUTO_INCREMENT)")'''

# Look at SQL Table
# mycursor.execute("DESCRIBE Person")

# Insert data into Person SQL Table
mycursor.execute("INSERT INTO Person (name, age) VALUES (%s,%s)", (x, y))
db.commit()  # Commit Changes and save permanently

mycursor.execute("SELECT * FROM Person")

for x in mycursor:
    print(x)