import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

#address starts with S:
myquery = { "address": { "$regex": "^S" } }

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)
  
#   C:\Users\My Name>python demo_mongodb_query_regex.py
# {'_id': 10, 'name': 'Richard', 'address': 'Sky st 331'}
# {'_id': 14, 'name': 'Viola', 'address': 'Sideway 1633'}
