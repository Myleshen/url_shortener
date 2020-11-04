from typing import Collection
import pymongo


class DB_Mongo:
    def __init__(self, prod=False) -> None:
        self.collection = self.__connection(prod)

    def __connection(self, prod=False) -> Collection:
        connection = pymongo.MongoClient("mongodb://localhost:27017")
        database = connection.get_database("url_shortner")
        if prod:
            return database.get_collection("prod")
        return database.get_collection("test")

    def add_entry(self, entry) -> str:
        self.collection.insert_one(entry)
        return "Added data successfully"

    def list_entries(self) -> list:
        return [index for index in self.collection.find({})]

    def get_long_url(self, short_url) -> str:
        query = {"created_url": short_url}
        return self.collection.find_one(query)