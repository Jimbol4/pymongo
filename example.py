from pymongo import MongoClient
import datetime
client = MongoClient()

db = client.test_db

post = {"author": "Mike",
         "text": "My first blog post!",
         "tags": ["mongodb", "python", "pymongo"],
         "date": datetime.datetime.utcnow()}

posts = db.posts

# select all items in a collection
#for post in posts.find():
#	print(post)

# select all items matching the given criteria
#for post in posts.find({"author" : "Mike"}):
#	print(post)

# insert single item
#post_id = posts.insert_one(post).inserted_id

#print(db.collection_names(include_system_collections=False))

# get the first record from the posts table
#print(posts.find_one())

# bulk inserts
#new_posts = [{"author": "Mike",
#               "text": "Another post!",
#               "tags": ["bulk", "insert"],
#               "date": datetime.datetime(2009, 11, 12, 11, 14)},
#              {"author": "Eliot",
#               "title": "MongoDB is fun",
#               "text": "and pretty easy too!",
#               "date": datetime.datetime(2009, 11, 10, 10, 45)}]

#result = posts.insert_many(new_posts)
#print(result.inserted_ids)

print(posts.count())
print(posts.find({'author':'Mike'}).count())