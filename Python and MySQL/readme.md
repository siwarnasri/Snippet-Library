Python can be used in database applications.

One of the most popular databases is MySQL.

# MySQL Database:
To be able to experiment with the code examples in this tutorial, you should have MySQL installed on your computer.

You can download a free MySQL database at https://www.mysql.com/downloads/.

Install MySQL Driver
Python needs a MySQL driver to access the MySQL database.

In this tutorial we will use the driver "MySQL Connector".

We recommend that you use PIP to install "MySQL Connector".

PIP is most likely already installed in your Python environment.

Navigate your command line to the location of PIP, and type the following:

> Download and install "MySQL Connector":

```python
C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>python -m pip install mysql-connector-python
```

Now you have downloaded and installed a MySQL driver.

### Test MySQL Connector:

To test if the installation was successful, or if you already have "MySQL Connector" installed, create a Python page with the following content:

> demo_mysql_test.py:

```python
import mysql.connector
```

If the above code was executed with no errors, "MySQL Connector" is installed and ready to be used.

### Create Connection:

Start by creating a connection to the database.

Use the username and password from your MySQL database:

> demo_mysql_connection.py:

```python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)

print(mydb)
```

Now you can start querying the database using SQL statements.

# Python MySQL Create Database:

### Creating a Database:

To create a database in MySQL, use the "CREATE DATABASE" statement:

> create a database named "mydatabase":

```python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")
```

If the above code was executed with no errors, you have successfully created a database.

### Check if Database Exists:

You can check if a database exist by listing all databases in your system by using the "SHOW DATABASES" statement:

> Return a list of your system's databases:

```python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)
```

Or you can try to access the database when making the connection:

> Try connecting to the database "mydatabase":

```python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)
```

If the database does not exist, you will get an error.

# Python MySQL Create Table:

### Creating a Table:

To create a table in MySQL, use the "CREATE TABLE" statement.

Make sure you define the name of the database when you create the connection

> Create a table named "customers":

```python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
```

If the above code was executed with no errors, you have now successfully created a table.

### Check if Table Exists:

You can check if a table exist by listing all tables in your database with the "SHOW TABLES" statement:

```python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)
```

> Return a list of your system's databases:

### Primary Key:

When creating a table, you should also create a column with a unique key for each record.

This can be done by defining a PRIMARY KEY.

We use the statement "INT AUTO_INCREMENT PRIMARY KEY" which will insert a unique number for each record. Starting at 1, and increased by one for each record.

> Create primary key when creating the table:

```python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
```

If the table already exists, use the ALTER TABLE keyword:

> Create primary key on an existing table:

```python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
```

# Python MySQL Insert Into Table:

### Insert Into Table:

To fill a table in MySQL, use the "INSERT INTO" statement.

> Insert a record in the "customers" table:

```python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
```

```diff
+ Important!: Notice the statement: mydb.commit(). It is required to make the changes, otherwise no changes are made to the table.
```

### Insert Multiple Rows:

To insert multiple rows into a table, use the executemany() method.

The second parameter of the executemany() method is a list of tuples, containing the data you want to insert:

> Fill the "customers" table with data:

```python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")
```

### Get Inserted ID:

You can get the id of the row you just inserted by asking the cursor object.

```diff
+ Note: If you insert more than one row, the id of the last inserted row is returned.
```

> Insert one row, and return the ID:

```python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Michelle", "Blue Village")
mycursor.execute(sql, val)

mydb.commit()

print("1 record inserted, ID:", mycursor.lastrowid)
```

# Python MySQL Select From:

### Select From a Table:

To select from a table in MySQL, use the "SELECT" statement:

> Select all records from the "customers" table, and display the result:

```python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
```

```diff
+ Note: We use the fetchall() method, which fetches all rows from the last executed statement.
```

### Selecting Columns:

To select only some of the columns in a table, use the "SELECT" statement followed by the column name(s):

> Select only the name and address columns:

```python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT name, address FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
```

### Using the fetchone() Method:

If you are only interested in one row, you can use the fetchone() method.

The fetchone() method will return the first row of the result:

> Fetch only one row:

```python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchone()

print(myresult)
```

# Python MySQL Where:

### Select With a Filter

When selecting records from a table, you can filter the selection by using the "WHERE" statement:

> Select record(s) where the address is "Park Lane 38": result:

```python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE address ='Park Lane 38'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
```

### Wildcard Characters:

You can also select the records that starts, includes, or ends with a given letter or phrase.

Use the %  to represent wildcard characters:

> Select records where the address contains the word "way":

```python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE address LIKE '%way%'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
```

### Prevent SQL Injection:

When query values are provided by the user, you should escape the values.

This is to prevent SQL injections, which is a common web hacking technique to destroy or misuse your database.

The mysql.connector module has methods to escape query values:

> Escape query values by using the placholder %s method:

```python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )

mycursor.execute(sql, adr)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
```

# Python MySQL Order By:

### Sort the Result:

Use the ORDER BY statement to sort the result in ascending or descending order.

The ORDER BY keyword sorts the result ascending by default. To sort the result in descending order, use the DESC keyword.

> Sort the result alphabetically by name: result:

```python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers ORDER BY name"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
```

### ORDER BY DESC:

Use the DESC keyword to sort the result in a descending order.

> Sort the result reverse alphabetically by name:

```python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers ORDER BY name DESC"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
```

# Python MySQL Delete From By:

### Delete Record:

You can delete records from an existing table by using the "DELETE FROM" statement:

> Delete any record where the address is "Mountain 21":

```python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "DELETE FROM customers WHERE address = 'Mountain 21'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")
```

```diff
+ Important!: Notice the statement: mydb.commit(). It is required to make the changes, otherwise no changes are made to the table.

+ Notice the WHERE clause in the DELETE syntax: The WHERE clause specifies which record(s) that should be deleted. 
+ If you omit the WHERE clause, all records will be deleted!
```

### Prevent SQL Injection:

It is considered a good practice to escape the values of any query, also in delete statements.

This is to prevent SQL injections, which is a common web hacking technique to destroy or misuse your database.

The mysql.connector module uses the placeholder %s to escape values in the delete statement:

> Escape values by using the placeholder %s method:

```python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "DELETE FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )

mycursor.execute(sql, adr)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")
```

# Python MySQL Drop Table:

### Delete a Table/:

You can delete an existing table by using the "DROP TABLE" statement:

> Delete the table "customers":

```python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "DROP TABLE customers"

mycursor.execute(sql)
```

### Drop Only if Exist:

If the table you want to delete is already deleted, or for any other reason does not exist, you can use the IF EXISTS keyword to avoid getting an error.

> Delete the table "customers" if it exists:

```python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "DROP TABLE IF EXISTS customers"

mycursor.execute(sql)
```

# Python MySQL Update Table:

### Update Table:

You can update existing records in a table by using the "UPDATE" statement:

> Overwrite the address column from "Valley 345" to "Canyon 123":

```python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")
```

```diff
+ Important!: Notice the statement: mydb.commit(). It is required to make the changes, otherwise no changes are made to the table.

+ Notice the WHERE clause in the UPDATE syntax: The WHERE clause specifies which record or records that should be updated. 
+ If you omit the WHERE clause, all records will be updated!
```

### Prevent SQL Injection:

It is considered a good practice to escape the values of any query, also in update statements.

This is to prevent SQL injections, which is a common web hacking technique to destroy or misuse your database.

The mysql.connector module uses the placeholder %s to escape values in the delete statement:

> Escape values by using the placeholder %s method:

```python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "UPDATE customers SET address = %s WHERE address = %s"
val = ("Valley 345", "Canyon 123")

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")
```

# Python MySQL Limit:

### Limit the Result:

You can limit the number of records returned from the query, by using the "LIMIT" statement:

> Select the 5 first records in the "customers" table:

```python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers LIMIT 5")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
```

### Start From Another Position:

If you want to return five records, starting from the third record, you can use the "OFFSET" keyword:

> Start from position 3, and return 5 records:

```python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
```
# Python MySQL Join:

### Join Two or More Tables:
You can combine rows from two or more tables, based on a related column between them, by using a JOIN statement.

Consider you have a "users" table and a "products" table:

> users


$$\textcolor{Purple}{\text``\{ id: 1, name: 'John', fav: 154\},``}$$

$$\textcolor{Purple}{\text`\{ id: 2, name: 'Peter', fav: 154\},`}$$

$$\textcolor{Purple}{\text``\{ id: 3, name: 'Amy', fav: 155\},``}$$ 

$$\textcolor{Purple}{\text``\{ id: 4, name: 'Hannah', fav:\},``}$$

$$\textcolor{Purple}{\text``\{ id: 5, name: 'Michael', fav:\}``}$$

> products

$$\textcolor{Purple}{\text``\{ id: 154, name: 'Chocolate Heaven' \},``}$$

$$\textcolor{Purple}{\text``\{ id: 155, name: 'Tasty Lemons' \},``}$$

$$\textcolor{Purple}{\text``\{ id: 156, name: 'Vanilla Dreams' \}``}$$

These two tables can be combined by using users' fav field and products' id field.

> Join users and products to see the name of the users favorite product:

```python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  INNER JOIN products ON users.fav = products.id"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
```

```diff
+ Note: You can use JOIN instead of INNER JOIN. They will both give you the same result.
```

### LEFT JOIN:

In the example above, Hannah, and Michael were excluded from the result, that is because INNER JOIN only shows the records where there is a match.

If you want to show all users, even if they do not have a favorite product, use the LEFT JOIN statement:

> Select all users and their favorite product:

```python
sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  LEFT JOIN products ON users.fav = products.id"
```

### RIGHT JOIN:

If you want to return all products, and the users who have them as their favorite, even if no user have them as their favorite, use the RIGHT JOIN statement:

> Select all products, and the user(s) who have them as their favorite:

```python
sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  RIGHT JOIN products ON users.fav = products.id"
```

```diff
+ Note: Hannah and Michael, who have no favorite product, are not included in the result.
```
