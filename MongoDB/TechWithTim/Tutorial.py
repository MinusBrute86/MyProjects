import urllib
import pymongo
from pymongo import MongoClient

# MongoDB Info
user = "mongoadmin"
passwd = urllib.parse.quote_plus("R@mpage21!")
db_name = "MongoTutorial"

# Connect to MongoDB
cluster = MongoClient("mongodb+srv://"+user+":"+passwd+"@cluster0.sfzab.mongodb.net/"+db_name+"?retryWrites=true&w"
                        "=majority")

# Getting DB and Collection
db = cluster[db_name]
collection = db['Test']

# Query/Post info into MongoDB
post1 = {"_id": 1, "name": "Nathan", "About Me": "Someone who puts in a lot of effort!"}
post2 = {"_id": 2, "name": "Tim", "About Me": "Always makes great tutorials!"}
post3 = {"_id": 3, "name": "Joe", "About Me": "Example used in Tim's tutorials."}

# Insert/Delete/Update Documents
# results = collection.update_one({"_id":1}, {"$set":{"age":25}})

# Counting amount of docs
post_count = collection.count_documents({})
print(post_count)
