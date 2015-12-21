from pymongo import MongoClient
import datetime

client = MongoClient('172.16.78.203',32768)
db = client.test
#posts = db.posts
#print(posts.find_one())
cursor = db.test.find()
for document in cursor:
    print(document)
