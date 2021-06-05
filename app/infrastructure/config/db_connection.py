import pymongo

class Database():
    URI = 'mongodb://localhost:27017'
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['devPureSpectrum']

    @staticmethod
    def insert_one(collection, obj_data):
        return Database.DATABASE[collection].insert_one(obj_data)

    @staticmethod
    def find_one(collection, query, params):
        return Database.DATABASE[collection].find_one(query, params)