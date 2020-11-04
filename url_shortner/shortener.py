from url_shortner.db_connection import DB_Connection
from . import utility
from .db_connection import DB_Connection


class Shortener:
    def __init__(self) -> None:
        self.util = utility.Utility()
        self.db_conn = DB_Connection()

    def create_unique_url(self, long_url: str):
        short_url = self.util.md5(long_url)
        short_url = f"www.sample.in/{short_url[:7]}"
        self._add_to_db(long_url, short_url)
        return short_url

    def _add_to_db(self, long_url, short_url):
        entry = {
            "original_url": long_url,
            "created_url": short_url,
        }
        return self.db_conn.insert(entry)

    def list_urls_in_db(self):
        return self.db_conn.list_all()