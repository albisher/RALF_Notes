**Tags:** #database, #orm, #migrations, #postgresql, #sqlalchemy, #flask, #alembic
**Created:** 2026-01-13
**Type:** documentation

# task_002

## Summary

```
Configures PostgreSQL database schema and migrations for a Flask application using SQLAlchemy ORM and Alembic.
```

## Details

> This task involves setting up a PostgreSQL database schema with SQLAlchemy ORM models (`User`, `World`, `WorldElement`) and Alembic for migrations. The `User` model includes fields for authentication (email, password_hash) and optional WebAuthn credentials. The `World` model tracks user-assigned worlds with metadata, while `WorldElement` stores flexible JSON metadata via `JSONB` for dynamic data. Alembic generates migration scripts to apply schema changes, ensuring compatibility with PostgreSQL.

## Key Functions

### `SQLAlchemy ORM Models`

Define database tables (`User`, `World`, `WorldElement`) with specified fields and constraints.

### `Alembic Migrations`

Generate and apply migration scripts to synchronize the database schema with Python models.

### `Flask-SQLAlchemy Integration`

Initialize SQLAlchemy within Flask for ORM operations.

### `Flask-Migrate`

Automate Alembic setup and migration management.

## Usage

1. Install dependencies (`pip install SQLAlchemy alembic Flask-SQLAlchemy Flask-Migrate`).
2. Initialize Alembic (`alembic init alembic`).
3. Define models in Python (e.g., `models.py`).
4. Generate migrations (`alembic revision --autogenerate`).
5. Apply migrations (`alembic upgrade head`).
6. Test database tables via `psql` or Alembic’s `alembic upgrade head` command.

## Dependencies

> ``SQLAlchemy``
> ``Alembic``
> ``Flask-SQLAlchemy``
> ``Flask-Migrate``
> `PostgreSQL.`

## Related

- [[Flask Backend Architecture]]
- [[PostgreSQL Configuration Guide]]

>[!INFO] Important Note
> Ensure PostgreSQL is running and accessible before running Alembic commands. Use `alembic env` to configure the database URI (e.g., `postgresql://user:pass@localhost/dbname`).

>[!WARNING] Caution
> Avoid manual schema edits after migrations are applied. Use Alembic’s `alembic downgrade` to revert changes if needed. JSONB support requires PostgreSQL 9.4+.
