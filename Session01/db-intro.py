from pymongo import MongoClient

mongo_uri = "mongodb://root:root12345@ds151530.mlab.com:51530/c4e18-lab"

#1. Connect to database
client = MongoClient(mongo_uri)

#2. Get database
db = client.get_default_database()

#3. Create collection
games = db['games']

#4. Create document
# new_movies = {
#     "title": "Titanic",
#     "description": "titanic"
# }

#5. Insert document into collection
# movies.insert_one(new_movies)

all_game = games.find()

for game in all_game:
    print(game)