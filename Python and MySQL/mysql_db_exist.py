import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="myusername",
  password="mypassword",
  database="mydatabase"
)

#If this page is executed with no error, the database "mydatabase" exists in your system


# C:\Users\My Name>python demo_mysql_db_exist.py
