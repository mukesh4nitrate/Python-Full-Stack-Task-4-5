TASK 4 – ROLE LOGIC, API ENDPOINTS AND SECURITY FLOW
Student Management System | Python Flask + SQLite

Purpose: This document explains how user roles, REST API endpoints, and the authentication and authorization security flow work in the Task 4 Student Management System. It is prepared as technical documentation for project submission.
1. ROLE LOGIC

The application uses Role-Based Access Control (RBAC). Each registered account has a role stored with its user record.
The application uses two roles:
- Admin - Administrative access - Access the admin dashboard, manage users and roles, and perform protected student-management operations.
- User - Standard access - Log in and use the normal user dashboard. Cannot access admin-only pages or operations.

How Role Checking Works
- A user registers or logs in with a username and password.
- The server verifies the password against the stored password hash.
- After successful login, the server stores the authenticated user's identity in the Flask session.
- For a protected page or API operation, the application checks whether the user is logged in.
- For an admin-only operation, the application additionally checks whether the current user's role is admin.
- If the user is not logged in, access is rejected. If the user is logged in but does not have admin permissions, admin-only access is rejected.

Expected Access Results
- 401 Unauthorized: User is not authenticated.
- 403 Forbidden: User is authenticated but does not have the required admin permissions.
- 200 OK: Authorized request completed successfully.

2. API ENDPOINTS
The application provides JSON-based REST API endpoints for authentication and student record management.
Authentication API
- POST /api/auth/register - Register a new user account. - Access: Public
- POST /api/auth/login - Authenticate a user and establish a session. - Access: Public
- POST /api/auth/logout - End the authenticated session. - Access: Authenticated session

Student Management API
- GET /api/students - Retrieve all student records in JSON format. - Access: Login required
- GET /api/students/<id> - Retrieve a particular student using their ID. - Access: Login required
- POST /api/students - Create a new student record. - Access: Protected
- PUT /api/students/<id> - Update an existing student record. - Access: Protected
- DELETE /api/students/<id> - Delete a student record. - Access: Protected

Note: The exact permissions for student-management operations depend on the server-side authorization checks implemented in app.py.

Common API Response Codes
- 200 OK - Request completed successfully. - Example: Student records retrieved.
- 201 Created - New resource created successfully. - Example: Student record created.
- 400 Bad Request - Invalid or incomplete request data. - Example: Missing required fields.
- 401 Unauthorized - Authentication required. - Example: {"error":"Authentication required"}
- 403 Forbidden - Insufficient permissions. - Example: {"error":"Admin access required"}
- 404 Not Found - Endpoint or requested record not found. - Example: {"error":"Student not found"}

Important: The exact success status and JSON response may vary depending on the route implementation. Use the actual Postman response when preparing submission evidence.
3. SECURITY FLOW

The security system separates two important concepts:

- Authentication: Verifies who the user is.
- Authorization: Determines what the authenticated user is allowed to do.

Step-by-Step Security Flow
- The client submits registration or login details through the application interface or API.
- Flask validates the submitted information.
- During login, the application checks the submitted password against the stored password hash.
- If the credentials are valid, Flask creates an authenticated session.
- The browser sends the session cookie with subsequent requests.
- Protected routes check the session to confirm that the user is authenticated.
- If the route requires administrator access, the application checks the user's role.
- The application validates the submitted data.
- The permitted database operation is performed using SQLite.
- The server returns an appropriate HTML or JSON response.

Security Controls
- 1. Password Hashing - Passwords are stored as hashes instead of plain text. Password verification is performed during login.
- 2. Session-Based Authentication - Protected routes require a valid authenticated session.
- 3. Role-Based Authorization - Admin-only routes check the user's role on the server. Standard users cannot gain administrator access simply by changing the frontend interface.
- 4. Server-Side Validation - Incoming form and JSON data are validated before database operations are performed.
- 5. Environment-Based Secret Key - A strong Flask SECRET_KEY should be configured through deployment environment variables. Production secrets should not be committed to GitHub.
- 6. Least Privilege - Normal user accounts receive only the permissions required for standard application usage.
- 7. Safe Error Handling - The application should return appropriate 401, 403, and 404 responses without exposing password hashes, secret keys, or internal error details.

4. SECURITY FLOW SUMMARY

The application's overall security process is:
LOGIN - VERIFY PASSWORD HASH - CREATE SESSION - CHECK LOGIN - CHECK USER ROLE - VALIDATE INPUT - DATABASE ACTION - RETURN RESPONSE

This process helps protect student records and restrict unauthorized administrative operations.

5. POSTMAN TEST EVIDENCE CHECKLIST
The following tests can be used to demonstrate the API functionality.
- Test 1 - Login using valid credentials. - Expected Result: Successful login.
- Test 2 - Access GET /api/students without logging in. - Expected Result: 401 Unauthorized.
- Test 3 - Log in as a standard user and attempt an admin-only operation. - Expected Result: 403 Forbidden.
- Test 4 - Log in as an administrator and perform an authorized operation. - Expected Result: Successful response.
- Test 5 - Use GET to retrieve student records. - Expected Result: Student data returned.
- Test 6 - Use POST to create a student record. - Expected Result: Student created.
- Test 7 - Use PUT to update a student record. - Expected Result: Student updated.
- Test 8 - Use DELETE to remove a student record. - Expected Result: Student deleted.
- Test 9 - Request a student ID that does not exist. - Expected Result: 404 Not Found.

Evidence to Attach
Include the following screenshots in the project submission:
- Successful user login in Postman.
- Successful administrator login in Postman.
- GET student records response.
- POST student creation response.
- PUT student update response.
- DELETE student response.
- 401 Unauthorized response.
- 403 Forbidden response.
- 404 Student Not Found response.

6. CONCLUSION
The Task 4 Student Management System implements user authentication, role-based access control, REST API endpoints, and database operations using Python Flask and SQLite.
The application distinguishes administrator and standard user permissions, protects restricted operations through authentication and authorization checks, and provides API responses for successful and unsuccessful requests.
These features demonstrate the implementation of backend security, user-role management, and REST API functionality in a Python Flask application.
Project: Student Management System
Technology Stack: Python, Flask, SQLite, HTML, CSS, JavaScript, REST API, Postman
Documentation: Task 4 – Role Logic, API Endpoints and Security Flow
