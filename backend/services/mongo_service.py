from pymongo import MongoClient
from typing import Any

class MongoService:
    def __init__(self, uri: str):
        self.client = MongoClient(uri)
    
    def find(self, db: str, collection: str, query: dict) -> list:
        return list(self.client[db][collection].find(query))
