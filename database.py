
import sqlite3
import os
from pathlib import Path

# Railway uses persistent storage at /data
volume_path = os.getenv("RAILWAY_VOLUME_MOUNT_PATH")

if volume_path:
    DATABASE = Path(volume_path) / "database.db"
else:
    DATABASE = Path(__file__).resolve().parent / "database.db"


def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()

    try:
        # Create users table if it does not exist
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        """)

        # Create students table if it does not exist
        conn.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                course TEXT NOT NULL
            )
        """)

        # Safely add role column to an existing users table
        columns = conn.execute(
            "PRAGMA table_info(users)"
        ).fetchall()

        column_names = [column["name"] for column in columns]

        if "role" not in column_names:
            conn.execute("""
                ALTER TABLE users
                ADD COLUMN role TEXT NOT NULL DEFAULT 'user'
            """)

        conn.commit()

    finally:
        conn.close()


if __name__ == "__main__":
    init_db()
    print("Database initialized successfully!")
    print(f"Database location: {DATABASE}")
