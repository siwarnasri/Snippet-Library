import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="myusername",
  password="mypassword"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)

  
# C:\Users\My Name>python demo_mysql_show_databases.py
# ('information_scheme',)
# ('mydatabase',)
# ('performance_schema',)
# ('sys',)
