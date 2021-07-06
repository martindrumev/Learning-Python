import pymongo
from pymongo import MongoClient

myClient = MongoClient()
db = myClient.mydb

users = db.users
user1 = {"username": "nick", "password": "myverysecurepassword", "favorite_number": 445, "hobbies": ["python", "games", "pizza"]}
user_id = users.insert_one(user1).inserted_id

print(user_id)