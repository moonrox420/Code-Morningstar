import psycopg2
from psycopg2.pool import ThreadedConnectionPool
from typing import Any

class PostgresService:
    def __init__(self, dsn: str, minconn: int = 1, maxconn: int = 5):
        self.pool = ThreadedConnectionPool(minconn, maxconn, dsn=dsn)

    def execute(self, query: str, params: tuple = ()) -> Any:
        conn = self.pool.getconn()
        try:
            with conn.cursor() as cur:
                cur.execute(query, params)
                if cur.description:
                    return cur.fetchall()
                if query.strip().upper().startswith(("INSERT", "UPDATE", "DELETE", "CREATE", "DROP", "ALTER")):
                    conn.commit()
        finally:
            self.pool.putconn(conn)
