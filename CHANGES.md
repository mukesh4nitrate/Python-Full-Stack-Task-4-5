# Fixes made to python-fullstack-task3

## app.py
1. Role is now read from the database on every protected request (was trusted from the cookie session). A demoted admin loses access immediately; a deleted user is logged out.
2. SECRET_KEY now comes from the SECRET_KEY environment variable (random fallback) instead of a hard-coded string.
3. init_db() runs when the module loads, so `flask run` works too (it only ran under `python app.py` before).
4. /login and /register redirect already-logged-in users.
5. Duplicate username -> clear message (web) / 409 (API, also on race conditions).
6. Email format validated in /add-student, /edit/<id> and POST/PUT /api/students.
7. /delete/<id> and /admin/manage-users now report "not found" instead of silently succeeding.
8. Unknown /api/* URLs and wrong methods return JSON 404/405 instead of an HTML page.
9. Broken "# ------# ------" comment banners and empty "# delete" section removed.

## Templates / static
10. favicon.svg and logo-admin.svg were in screenshots/, not static/ -> 404. Moved to static/.
11. Flash messages were only shown on login.html. Added templates/_flash.html and included it everywhere, so "Access denied", "Student added", register errors etc. are visible.
12. Removed duplicate <title> tags from every template.
13. edit_student.html rewritten: valid <html> document, `method="post",` typo fixed, url_for() instead of hard-coded /static and /students.
14. dashboard.html: removed the stray line of dashes and invalid <h1><p> nesting.
15. "logo admin.svg" renamed to "logo-admin.svg" (no space in file name).

## Scripts
16. reset_admin_password.py printed "Username: casio" even though it edits DTS -> prints the real username; password input now hidden with getpass.
17. create_db.py created a users table WITHOUT the role column (different from database.py) -> now just calls init_db().
18. requirements.txt given minimum versions.

## Removed from the submission folder
__pycache__/, templates.zip (stale copy of templates).
