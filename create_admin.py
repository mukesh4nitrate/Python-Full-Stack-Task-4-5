
from database import get_db, init_db
from werkzeug.security import generate_password_hash
import getpass

init_db()

username = input("Enter admin username:").strip()
password = getpass.getpass("Enter admin password: ")

if not username or not password:
    print("Username and password are required.")
    raise SystemExit

if len(password) < 8:
    print("Password must contain at least 8 characters.")
    raise SystemExit

db = get_db()

try:
    existing = db.execute(
        "SELECT id FROM users WHERE username = ?",
        (username,)
    ).fetchone()

    if existing:
        db.execute(
            "UPDATE users SET role = 'admin' WHERE id = ?",
            (existing["id"],)
        )
        print("Existing account promoted to admin.")
    else:
        db.execute(
            """
            INSERT INTO users (username, password, role)
            VALUES (?, ?, 'admin')
            """,
            (username, generate_password_hash(password))
        )
        print("Admin account created successfully.")

    db.commit()

finally:
    db.close()
