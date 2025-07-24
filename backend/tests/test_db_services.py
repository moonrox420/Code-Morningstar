import pytest
from backend.services.sqlite_service import SQLiteService

@pytest.fixture
def db(tmp_path):
    db_file = tmp_path / "test.db"
    service = SQLiteService(str(db_file))
    service.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT)")
    return service

def test_insert_and_select(db):
    db.execute("INSERT INTO users (username) VALUES (?)", ("testuser",))
    rows = db.execute("SELECT username FROM users")
    assert rows[0][0] == "testuser"
