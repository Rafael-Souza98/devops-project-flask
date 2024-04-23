import os
import mongomock
class DevConfig():

    MONGODB_SETTINGS = {
        'db': os.getenv('MONGODB_DB'),
        'host': os.getenv('MONGODB_HOST'),
        'username': os.getenv('MONGODB_USER'),
        'password': os.getenv('MONGODB_PASSWORD')
    }

class ProdConfig():
    MONGODB_USER = os.getenv('MONGODB_USER')
    MONGODB_PASSWORD = os.getenv('MONGODB_PASSWORD')
    MONGODB_HOST = os.getenv('MONGODB_HOST')
    MONGODB_DB = os.getenv('MONGODB_DB')

    MONGODB_SETTINGS = {
        'db' : 'users',
        'host': "mongodb+srv://%s:%s@%s/?retryWrites=true&w=majority&appName=db-app-python" % (
            MONGODB_USER, MONGODB_PASSWORD, MONGODB_HOST
        )
    }

class MockConfig():
    MONGODB_SETTINGS = {
        'db': 'mongoenginetest',
        'host': 'mongodb://localhost',
        'mongo_client_class' : mongomock.MongoClient
    }

# db-app-python.lcmitgm.mongodb.net