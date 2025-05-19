import tempfile
import os
import sqlite3
from app import db


def test_db_creation_and_insert(monkeypatch):
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        test_db_path = tmp.name

    monkeypatch.setenv("DB_PATH", test_db_path)
    db.init_db()

    db.add_user(42, "Ивана Иванова")
    user = db.get_user(42)

    assert user[0] == "Ивана Иванова"
    assert user[1] == 0

    db.update_standing(42, 1)
    user = db.get_user(42)
    assert user[1] == 1

    os.remove(test_db_path)
