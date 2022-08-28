import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['mydatabase']
mycol = mydb["customers"]

mydict = { "name": "John", "address": "Highway 37" }

x = mycol.insert_one(mydict)

print(x)

# C:\Users\My Name>python demo_mongodb_insert.py
# <pymongo.results.InsertOneResult object at 0x03D62918>
