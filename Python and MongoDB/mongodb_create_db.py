import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')

mydb = myclient['mydatabase']

# database created!

# C:\Users\My Name>python demo_mongodb_create_db.py
