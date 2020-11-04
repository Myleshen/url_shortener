import pymongo


class Db:
    def __init__(self) -> None:
        self.collection = self.connection()

    def connection(self):
        connection = pymongo.MongoClient("mongodb://localhost:27017")
        database = connection.get_database("anime_tracker")
        return database.get_collection("testing")

    def add_entry(self, entry):
        try:
            self.collection.insert_one(entry)
            return "Added data successfully"
        except:
            return "Failed to add the data"
