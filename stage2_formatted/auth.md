**Tags:** #authentication, #JWT, #Flask, #user-management
**Created:** 2026-01-13
**Type:** documentation

# auth

## Summary

```
Handles user registration, login, token refresh, and password management via Flask-JWT-Extended.
```

## Details

> This Flask Blueprint (`auth_bp`) manages authentication workflows, including registration, login, token refresh, logout, and password updates. It supports both username and email-based authentication and uses JWT (JSON Web Tokens) for secure session management. Passwords are hashed using Werkzeug’s `generate_password_hash`. The system includes test user creation utilities (`create_test_user`, `create_user_ab`) for development.

## Key Functions

### `register`

Creates a new user with hashed password and returns JWT tokens.

### `login`

Authenticates users via username/email and password, issuing access/refresh tokens.

### `refresh`

Validates a refresh token to generate a new access token.

### `logout`

Placeholder for token invalidation (in production, may use token blacklisting).

### `get_current_user`

Retrieves authenticated user details via JWT.

### `change_password`

Updates user password after verifying current password.

### `create_test_user`

Initializes a test user (`test`/`test@spacepearl.com`) for testing.

### `create_user_ab`

Initializes a test user (`ab`/`ab@spacepearl.com`) with a predefined password.

## Usage

1. **Register**: POST `/register` with `{ "username": "...", "email": "...", "password": "..." }`.
2. **Login**: POST `/login` with `{ "username": "...", "email": "...", "password": "..." }` to receive tokens.
3. **Refresh**: POST `/refresh` with a valid refresh token to get a new access token.
4. **Get User**: GET `/me` (requires valid access token).
5. **Change Password**: POST `/change-password` with `{ "current_password": "...", "new_password": "..." }`.

## Dependencies

> `flask`
> `flask-jwt-extended`
> `werkzeug`
> `SQLAlchemy (via `models.db`)`
> `Python `datetime`.`

## Related

- [[Flask-JWT-Extended Documentation]]
- [[SQLAlchemy User Model]]
- [[Flask Blueprint Guide]]

>[!INFO] JWT Security
> Always store `JWT_SECRET_KEY` securely in environment variables (e.g., `.env`) and avoid hardcoding. Use HTTPS in production to prevent token interception.

>[!WARNING] Password Hashing
> Ensure `generate_password_hash` uses a strong algorithm (e.g., PBKDF2 with high iterations) and never log plaintext passwords. Validate password strength policies if required.

>[!WARNING] Test Users
> The `create_test_user`/`create_user_ab` functions are for development only. Avoid using them in production; replace with proper user creation logic.
