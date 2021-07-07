import pymongo
from pymongo import MongoClient

myClient = MongoClient()
db = myClient.mydb

Users = db.users
user1 = {"username": "nick", "password": "myverysecurepassword", "favorite_number": 445, "hobbies": ["python", "games", "pizza"]}
user_id = Users .insert_one(user1).inserted_id

print(Users.find().count())

print(user_id)