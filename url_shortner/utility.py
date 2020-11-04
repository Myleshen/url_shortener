from random import random
from hashlib import md5


class Utility:
    def md5(self, long_url: str) -> str:
        long_url += f"{random()}"
        bytes = long_url.encode("utf-8")
        unique_url = md5(bytes)
        return unique_url.hexdigest()
