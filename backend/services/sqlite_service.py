import sqlite3
from typing import Any

class SQLiteService:
    def __init__(self, db_path: str):
        self.db_path = db_path

    def execute(self, query: str, params: tuple = ()) -> Any:
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            cur.execute(query, params)
            result = cur.fetchall() if cur.description else None
            conn.commit()
            return result
