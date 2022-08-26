import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

#address greater than S:
myquery = { "address": {"$gt": "S"} }

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)

# C:\Users\My Name>python demo_mongodb_query_modifier.py
# {'_id': 5, 'name': 'Michael', 'address': 'Valley 345'}
# {'_id': 8, 'name': 'Richard', 'address': 'Sky st 331'}
# {'_id': 10, 'name': 'Vicky', 'address': 'Yellow Garden 2'}
# {'_id': 14, 'name': 'Viola', 'address': 'Sideway 1633'}
