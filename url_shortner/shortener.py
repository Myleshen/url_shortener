from . import utility


class Shortener:
    def __init__(self) -> None:
        self.util = utility.Utility()

    def create_unique_url(self, long_url: str):
        return self.util.md5(long_url)
