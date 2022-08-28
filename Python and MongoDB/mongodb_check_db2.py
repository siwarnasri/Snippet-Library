import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')

dblist = myclient.list_database_names()
if "mydatabase" in dblist:
  print("The database exists.")
  
# C:\Users\My Name>python demo_mongodb_check_db2.py
# The database exists.
