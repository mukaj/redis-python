from datetime import datetime

cache = {}


class Entry:
    def __init__(self, data: str, timeout: datetime = None):
        self.data: str = data
        self.timeout: datetime = timeout
