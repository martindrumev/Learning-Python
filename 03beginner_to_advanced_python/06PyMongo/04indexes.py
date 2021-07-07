import pymongo
from pymongo import MongoClient
import datetime

client = MongoClient()
db = client.mydb

Users = db.users

# You can search much faster in mongoDB with index
creating_index = db.users.create_index([("username", pymongo.ASCENDING)])
print(creating_index)

print(Users.find({"username": "nick"}))

