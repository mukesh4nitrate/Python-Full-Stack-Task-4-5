import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "database.db"

db = sqlite3.connect(DB_PATH)

try:
    cursor = db.execute(
        "UPDATE users SET role = 'admin' WHERE username = ?",
        ("DTS",)
    )

    db.commit()

    if cursor.rowcount == 1:
        print("DTS is now an admin!")
    else:
        print("DTS username was not found.")

finally:
    db.close()
