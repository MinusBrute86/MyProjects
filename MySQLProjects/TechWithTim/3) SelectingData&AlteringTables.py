import mysql.connector
from datetime import datetime

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="R@mpage21!",
    database="testdatabase"
)

mycursor = db.cursor()
x,y,z = ("Nikki", datetime.now(), "F")

# Create SQL Table
'''mycursor.execute("CREATE TABLE Test (name VARCHAR(50) NOT NULL, created datetime NOT NULL, gender ENUM('M', 'F', 'O'), "
                 "id int PRIMARY KEY NOT NULL AUTO_INCREMENT)")'''

# Insert Values
'''mycursor.execute("INSERT INTO Test (name, created, gender) VALUES(%s,%s,%s)", (x,y,z))
db.commit()'''

# Alter SQL Table Values
'''mycursor.execute("ALTER TABLE Test ADD COLUMN food VARCHAR(50) NOT NULL")'''
'''mycursor.execute("ALTER TABLE Test CHANGE name first_name VARCHAR(50)")'''

# Remove SQL Table Values
'''mycursor.execute("ALTER TABLE Test DROP COLUMN food")'''

mycursor.execute("DESCRIBE Test")

'''mycursor.execute("SELECT * FROM Test WHERE gender = 'M' ORDER BY id DESC")'''
for x in mycursor:
    print(x)