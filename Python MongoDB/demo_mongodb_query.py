import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myquery = { "address": "Park Lane 38" }

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)

#   C:\Users\My Name>python demo_mongodb_query.py
# {'_id': 11, 'name': 'Ben', 'address': 'Park Lane 38'}
