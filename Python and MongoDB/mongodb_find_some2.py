import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

for x in mycol.find({},{ "address": 0 }):
  print(x)

# C:\Users\My Name>python demo_mongodb_find_some2.py
# {'_id': 1, 'name': 'John'}
# {'_id': 2, 'name': 'Peter'}
# {'_id': 3, 'name': 'Amy'}
# {'_id': 4, 'name': 'Hannah'}
# {'_id': 5, 'name': 'Michael'}
# {'_id': 6, 'name': 'Sandy'}
# {'_id': 7, 'name': 'Betty'}
# {'_id': 8, 'name': 'Richard'}
# {'_id': 9, 'name': 'Susan'}
# {'_id': 10, 'name': 'Vicky'}
# {'_id': 11, 'name': 'Ben'}
# {'_id': 12, 'name': 'William'}
# {'_id': 13, 'name': 'Chuck'}
# {'_id': 14, 'name': 'Viola'}
