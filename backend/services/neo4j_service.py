from neo4j import GraphDatabase
from typing import Any

class Neo4jService:
    def __init__(self, uri: str, user: str, password: str):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def execute(self, cypher: str, params: dict = None) -> Any:
        with self.driver.session() as session:
            result = session.run(cypher, params or {})
            return [record.data() for record in result]
