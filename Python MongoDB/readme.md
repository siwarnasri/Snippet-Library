Python can be used in database applications.

One of the most popular NoSQL database is MongoDB.

### MongoDB:
MongoDB stores data in JSON-like documents, which makes the database very flexible and scalable.

To be able to experiment with the code examples in this tutorial, you will need access to a MongoDB database.

You can download a free MongoDB database at [https://www.mongodb.com](https://www.mongodb.com).

Or get started right away with a MongoDB cloud service at https://www.mongodb.com/cloud/atlas.

### PyMongo:
Python needs a MongoDB driver to access the MongoDB database.

In this tutorial we will use the MongoDB driver "PyMongo".

We recommend that you use PIP to install "PyMongo".

PIP is most likely already installed in your Python environment.

Navigate your command line to the location of PIP, and type the following:
> Download and install "PyMongo":

> ```C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>python -m pip install pymongo```

Now you have downloaded and installed a mongoDB driver.

### Test PyMongo:
To test if the installation was successful, or if you already have "pymongo" installed, create a Python page with the following content:
> demo_mongodb_test.py:

> ``import pymongo``

# Python MongoDB Create Database:
### Creating a Database:
To create a database in MongoDB, start by creating a MongoClient object, then specify a connection URL with the correct ip address and the name of the database you want to create.

MongoDB will create the database if it does not exist, and make a connection to it.
> Create a database called "mydatabase":

> ``import pymongo``

> ``myclient = pymongo.MongoClient("mongodb://localhost:27017/")``

> ``mydb = myclient["mydatabase"]``

### ```diff
### + Important: In MongoDB, a database is not created until it gets content! 
### ```
