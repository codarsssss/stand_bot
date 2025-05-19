import os
import sqlite3


def get_db_path():
    """Получить путь до БД из окружения (поддерживает .env, monkeypatch и т.п.)"""
    return os.getenv("DB_PATH", "data/bot_data.db")


def init_db():
    """Создание таблицы, если ещё не создана."""
    with sqlite3.connect(get_db_path()) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                standing BOOLEAN NOT NULL DEFAULT 0
            )
        """)


def get_user(user_id):
    with sqlite3.connect(get_db_path()) as conn:
        return conn.execute(
            "SELECT name, standing FROM users WHERE user_id = ?", (user_id,)
        ).fetchone()


def add_user(user_id, name):
    with sqlite3.connect(get_db_path()) as conn:
        conn.execute(
            """
            INSERT OR REPLACE INTO users (user_id, name, standing)
            VALUES (?, ?, 0)
            """,
            (user_id, name),
        )


def update_standing(user_id, standing):
    with sqlite3.connect(get_db_path()) as conn:
        conn.execute(
            "UPDATE users SET standing = ? WHERE user_id = ?",
            (standing, user_id)
        )
