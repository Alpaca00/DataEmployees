import pymongo
from pymongo import MongoClient


client = MongoClient('localhost', 27017)
db = client.itproger
collection = db.employees


x = collection.delete_many({})
print(x.deleted_count, " documents deleted.")
