import mysql.connector
from mysql.connector.pooling import MySQLConnectionPool
from typing import Any

class MySQLService:
    def __init__(self, pool_name: str, pool_size: int, **db_config):
        self.pool = MySQLConnectionPool(pool_name=pool_name, pool_size=pool_size, **db_config)

    def execute(self, query: str, params: tuple = ()) -> Any:
        conn = self.pool.get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(query, params)
            result = cursor.fetchall() if cursor.description else None
            if cursor.description is None:  # Commit only for data-modifying queries
                conn.commit()
            return result
        finally:
            cursor.close()
            conn.close()
