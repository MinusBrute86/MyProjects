import mysql.connector
import requests
from tqdm.auto import tqdm
import time

API = "https://api.jikan.moe/v3"
path = "/top/manga"

db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='R@mpage21!',
    database='mangatestdb'
)
cursor = db.cursor()
Q1 = "CREATE TABLE Manga (mal_id int NOT NULL, ranking int PRIMARY KEY NOT NULL, title VARCHAR(255), score FLOAT, " \
     "manga_type VARCHAR(20))"
Q2 = "DROP TABLE Manga"

# cursor.execute(Q1)

# Add Values to mal_id column
pages = 269
for i in tqdm(range(1, pages)):
    response = requests.get(f'{API}{path}/{i}')
    time.sleep(2)
    try:
        for item in response.json()['top']:
            mal_id, rank, title, score, type = item['mal_id'], item['rank'], item['title'], item['score'], item['type']
            query = "INSERT INTO Manga (mal_id, ranking, title, score, manga_type) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (mal_id, rank, title, score, type))
    except:
        print("for loop acting sus")
db.commit()

cursor.execute("SELECT * FROM manga")
for x in cursor:
    print(x)