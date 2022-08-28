import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')

print(myclient.list_database_names())

# C:\Users\My Name>python demo_mongodb_check_db.py
# ['admin', 'local', 'mydatabase']
