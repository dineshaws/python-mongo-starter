import pymongo

from app.infrastructure.config.config_factory import ConfigFactory

config = ConfigFactory().create()

class Database():
    URI = config.DB_URI
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client[config.DB_NAME]

    @staticmethod
    def insert_one(collection, obj_data):
        return Database.DATABASE[collection].insert_one(obj_data)

    @staticmethod
    def find_one(collection, query, params):
        return Database.DATABASE[collection].find_one(query, params)