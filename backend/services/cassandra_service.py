from cassandra.cluster import Cluster
from typing import Any

class CassandraService:
    def __init__(self, host: str, port: int):
        self.cluster = Cluster([host], port=port)
        self.session = self.cluster.connect()

    def execute(self, cql: str, params: tuple = ()) -> Any:
        return self.session.execute(cql, params)
