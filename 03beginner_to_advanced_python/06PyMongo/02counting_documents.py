import pymongo
from pymongo import MongoClient

client = MongoClient()
db = client.mydb

Users = db.users
print(Users.find().count())

print(Users.find({"favorite_number": 445}).count())
print(Users.find({"favorite_number": 445, "username": "nick"}).count())
