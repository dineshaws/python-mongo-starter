from app.infrastructure.config.db_connection import Database

class BaseRepository():
    def __init__(self, collection = None) -> None:
        self.collection = collection

    def insert_one(self, data):
        obj_data = data.dict()
        Database.insert_one(self.collection, obj_data)

    def find_one(self, query, params={}):
        return Database.find_one(self.collection, query, params)