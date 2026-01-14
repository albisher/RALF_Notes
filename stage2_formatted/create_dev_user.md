**Tags:** #user-creation, #authentication, #Flask, #SQLAlchemy
**Created:** 2026-01-13
**Type:** code-notes

# create_dev_user

## Summary

```
Script automates creation of a preconfigured development user with fixed credentials for testing purposes.
```

## Details

> This script initializes a development user (`username: a`) with a hardcoded password (`spq8`) using Flask’s database session. It first checks for an existing user with the same username before creating a new entry. The user’s email is set to `dev@spaceperal.local`, and credentials are hashed securely via Werkzeug’s `generate_password_hash`. The script runs within a Flask application context to ensure proper database operations.

## Key Functions

### `create_dev_user()`

Orchestrates user creation, checks for existence, and logs success/failure.

### `User.query.filter_by(username='a').first()`

Queries existing users by username.

### `generate_password_hash('spq8')`

Hashes the password for secure storage.

## Usage

Run as a standalone script (`python create_dev_user.py`) to create the dev user. The script assumes:
- Flask app context is active (via `app.app_context()`).
- Database session is managed by Flask-SQLAlchemy.

## Dependencies

> `werkzeug.security`
> `Flask-SQLAlchemy (via `models.py`/`app.py`)`
> `Python 3.x`

## Related

- [[Flask-SQLAlchemy User Model]]
- [[app]]

>[!INFO] Hardcoded Credentials
> **Security Risk**: The password (`spq8`) is hardcoded and never rotated. Avoid using this in production; replace with environment variables or a secrets manager.

>[!WARNING] No Input Validation
> **Potential Issue**: The script does not validate email format or enforce uniqueness beyond username. Always extend checks for production use.
