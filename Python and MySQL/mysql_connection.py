import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="myusername",
  password="mypassword"
)

print(mydb)

# C:\Users\My Name>python demo_mysql_connection.py
# <mysql.connector.connection.MySQLConnection object ar 0x016645F0>
