from elasticsearch import Elasticsearch
from typing import Any

class ElasticsearchService:
    def __init__(self, host: str, port: int):
        self.client = Elasticsearch([{"host": host, "port": port}])

    def search(self, index: str, query: dict) -> Any:
        return self.client.search(index=index, body=query)