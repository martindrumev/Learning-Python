import pymongo
from pymongo import MongoClient
import datetime

current_date = datetime.datetime.now()

old_date = datetime.datetime(2009, 12, 11)

client = MongoClient()
db = client.mydb

Users = db.users

uid = Users.insert_one({"username": "ffie", "date": current_date})

# $gt means "Greater than" $gte "Greater than and equal to" / same goes for lt "less than"
find_date = Users.find({"date": {"$gt": old_date}}).count()
find_old_date = Users.find({"date": {"$lt": old_date}}).count()

# if this even exists
find_exists = Users.find({"date": {"$exists": True}}).count()

# not equal to
find_not_equal = Users.find({"username": {"$ne": "nick"}}).count()

print(current_date)
print(old_date)
print(find_date)
print(find_old_date)
print(find_exists)
print(find_not_equal)