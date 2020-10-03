import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="R@mpage21!",
    database="testdatabase"
)
cursor = db.cursor()

users = [('tim', 'techwithtim'),
         ('joe', 'joey123'),
         ('sarah', 'sarah1234')]

user_scores = [(45 ,100),
               (30, 200),
               (46, 124)]

Q1 = "CREATE TABLE Users (id int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50), passwd VARCHAR(50))"
Q2 = "CREATE TABLE Scores (user_id int PRIMARY KEY, FOREIGN KEY(user_id) REFERENCES Users(id), game1 int DEFAULT 0, " \
     "game2 int DEFAULT 0)"

Q3 = "INSERT INTO Users (name, passwd) VALUES (%s, %s)"
Q4 = "INSERT INTO Scores (user_id, game1, game2) VALUES (%s, %s, %s)"

for x, user in enumerate(users):
    cursor.execute(Q3, user)
    last_id = cursor.lastrowid
    cursor.execute(Q4, (last_id,) + user_scores[x])
db.commit()

cursor.execute("SELECT * FROM Scores")
for x in cursor:
    print(x)

cursor.execute("SELECT * FROM Users")
for x in cursor:
    print(x)