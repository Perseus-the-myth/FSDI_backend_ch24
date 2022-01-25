import pymongo

mongo_url = "mongodb+srv://mmckitrick:mrmongo@cluster0.80ugy.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

client = pymongo.MongoClient(mongo_url)

#get the specific database
db = client.get_database("CoolStore")