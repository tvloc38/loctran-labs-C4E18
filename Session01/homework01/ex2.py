from pymongo import MongoClient

mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

#1. Connect to database
client = MongoClient(mongo_uri)

#2. Get database
db = client.get_default_database()

posts = db['posts']

new_post={
    'title':'Nop bai muon',
    'author':'Loc Tran',
    'content':'Qua ban nen nop bai muon'
    }

posts.insert_one(new_post)