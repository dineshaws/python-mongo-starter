import pymongo

class Database():
    URI = 'mongodb://localhost:27017'
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['devPureSpectrum']

    @staticmethod
    def insert_one(collection, data):
        print('insert_one ', data)
        obj_data = data.dict()
        return Database.DATABASE[collection].insert_one(obj_data)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query, {'_id': 0})