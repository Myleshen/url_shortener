from db_connection.db_mongo import DB_Mongo


class DB_Connection:
    def __init__(self) -> None:
        self.conn = DB_Mongo()

    def insert(self, entry) -> str:
        return self.conn.add_entry(entry)

    def list_all(self) -> list:
        return self.conn.list_entries()