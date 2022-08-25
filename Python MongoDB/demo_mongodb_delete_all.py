import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

x = mycol.delete_many({})

print(x.deleted_count, "documents deleted")

# C:\Users\My Name>python demo_mongodb_delete_all.py
# 11 documents deleted.
