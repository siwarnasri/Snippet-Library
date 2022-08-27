import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

x mycol.find_one()

print(x)

# C:\Users\My Name>python demo_mongodb_find_one.py
# {'_id': 1, 'name': 'John', 'address': 'Highway37'}
