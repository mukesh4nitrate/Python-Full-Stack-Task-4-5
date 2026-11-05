# Optional: python create_db.py
# The app creates its tables automatically on start (database.init_db),
# so this file just reuses that same function to avoid two different schemas.
from database import init_db, DATABASE

init_db()
print(f"Tables ready (users with role, students) in {DATABASE}")
