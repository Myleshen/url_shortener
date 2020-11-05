from typing import Collection
import pymongo
import sys


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
        return [
            {"OriginalURL": index["original_url"], "ShortURL": index["created_url"]}
            for index in self.collection.find({})
        ]

    def get_long_url(self, short_url) -> str:
        query = {}
        if len(short_url) < 8:
            query = {"created_url": {"$regex": f".*{short_url}.*"}}
        else:
            query = {"created_url": short_url}
        try:
            query_dict = self.collection.find_one(query)
            return query_dict.get("original_url")
        except AttributeError:
            print(f"Error: The link that has been provided is not available..Exiting")
            sys.exit()
