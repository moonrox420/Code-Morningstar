from cassandra.cluster import Cluster
from typing import Any

class CassandraService:
    def __init__(self, host: str, port: int):
        self.cluster = Cluster([f"{host}:{port}"])
        self.session = self.cluster.connect()

    def execute(self, cql: str, params: tuple = ()) -> Any:
        return self.session.execute(cql, params)
