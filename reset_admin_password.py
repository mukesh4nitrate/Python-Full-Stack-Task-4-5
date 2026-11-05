
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
from getpass import getpass
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "database.db"

username = "DTS"

new_password = getpass("Enter new admin password: ")
confirm_password = getpass("Confirm new admin password: ")

if len(new_password) < 8:
    print("Password must contain at least 8 characters.")
    raise SystemExit

if new_password != confirm_password:
    print("Passwords do not match.")
    raise SystemExit

db = sqlite3.connect(DB_PATH)

try:
    user = db.execute(
        "SELECT id, role FROM users WHERE username = ?",
        (username,)
    ).fetchone()

    if user is None:
        print("Admin account not found.")
    elif user[1] != "admin":
        print("This account is not an admin. No changes made.")
    else:
        password_hash = generate_password_hash(new_password)

        db.execute(
            "UPDATE users SET password = ? WHERE username = ?",
            (password_hash, username)
        )

        db.commit()

        print("Admin password updated successfully.")
        print(f"Username: {username}")
        print("Role: admin")

finally:
    db.close()
