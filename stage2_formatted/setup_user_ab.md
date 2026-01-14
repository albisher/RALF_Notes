**Tags:** #user-management, #database-migration, #flask-jwt, #SQLAlchemy, #password-hashing
**Created:** 2026-01-13
**Type:** documentation

# setup_user_ab

## Summary

```
Script for setting up or updating a user 'ab' with password reassignment and data migration to this user.
```

## Details

> This script uses Flask and SQLAlchemy to create or update a user named 'ab' with a predefined password. It checks if the user exists, updates the password if found, or creates a new user. If other users exist, it reassigns all their associated data (worlds, elements, timelines, events, preferences, etc.) to the new user 'ab'. The script gracefully handles missing models (e.g., `Card`) by skipping reassignment for those entities.
> 
> The script dynamically checks for optional models (`Card`, `Link`, `CustomGenerator`) and skips reassignment if they are not available. It logs progress and errors during the reassignment process.

## Key Functions

### `setup_user_ab()`

Core function that creates/updates user 'ab' and reassigns all data from other users to this user.

### `generate_password_hash()`

Uses Flask-Werkzeug to hash the password for secure storage.

### `create_access_token()`

(Indirectly used) Generates JWT tokens for authentication (though not explicitly called in this script).

## Usage

1. Run the script directly (`python setup_user_ab.py`).
2. The script will:
   - Check if user 'ab' exists.
   - Update the password if the user exists.
   - Create a new user 'ab' if it does not exist.
   - Reassign all data (worlds, elements, timelines, etc.) from other users to 'ab'.
3. Logs progress and errors during execution.

## Dependencies

> `Flask`
> `Flask-JWT-Extended`
> `SQLAlchemy`
> `Werkzeug`
> ``app` (Flask app instance)`
> ``models` (SQLAlchemy models including `User``
> ``World``
> ``Timeline``
> `etc.).`

## Related

- [[SQLAlchemy User Model Documentation]]
- [[Flask-JWT Extended Documentation]]
- [[Password Hashing Best Practices]]

>[!INFO] Dynamic Model Handling
> The script dynamically checks for optional models (`Card`, `Link`, `CustomGenerator`) using `try-except` blocks. If these models are missing, reassignment for those entities is skipped with a warning.
>

>[!WARNING] Data Reassignment Risks
> Reassigning all data to a single user may cause data loss or corruption if:
> - The reassignment fails partially (e.g., some tables fail silently).
> - The original user data is not backed up before reassignment.
> - Foreign key constraints are violated during updates. The script uses `synchronize_session=False` for `TimelineEvent` updates to avoid cascading issues.
