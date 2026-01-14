**Tags:** #Alembic, #Database-Migrations, #SQLAlchemy, #Flask, #Configuration
**Created:** 2026-01-13
**Type:** documentation-research

# env

## Summary

```
Manages database migrations for a Flask application using Alembic and SQLAlchemy.
```

## Details

> This `env.py` script configures and orchestrates database migrations for a Flask application. It dynamically loads SQLAlchemy and Alembic configurations, sets up logging, and determines whether migrations should run in **offline** (script mode) or **online** (live database) mode. The script dynamically adjusts the database URL based on the Flask app’s configuration and ensures Alembic’s metadata aligns with the application’s database models.
> 
> Key logic:
> - Loads the Flask app and database models (`app` and `db`).
> - Configures logging via `fileConfig` if a logging config file is provided.
> - Determines migration mode (`offline`/`online`) and delegates execution to `run_migrations_offline()` or `run_migrations_online()`.
> - Uses `engine_from_config` to create a SQLAlchemy engine, with `NullPool` to avoid connection pooling (common in migration scripts).

## Key Functions

### ``run_migrations_offline()``

Executes migrations in script mode (no database connection needed), using a hardcoded URL from the config.

### ``run_migrations_online()``

Runs migrations against the live database, dynamically fetching the URI from Flask’s config (`SQLALCHEMY_DATABASE_URI`).

### ``context.configure()``

Sets up Alembic’s internal configuration (metadata, connection, etc.) for migration execution.

## Usage

1. Place this script in the parent directory of your Flask app (to resolve imports).
2. Configure Alembic’s `.ini` file (e.g., `alembic.ini`) or pass a logging config file.
3. Call `alembic upgrade head` from the terminal to trigger migrations.
4. For offline testing, ensure `SQLALCHEMY_URL` is set in the config.

## Dependencies

> ``logging``
> ``sqlalchemy``
> ``alembic``
> ``flask``
> ``flask-sqlalchemy``
> ``python-dotenv` (if used for config).`

## Related

- [[Flask-SQLAlchemy-Documentation]]
- [[Alembic-User-Guide]]
- [[Flask-Configuration-Example]]

>[!INFO] Offline vs. Online Mode
> - **Offline**: Useful for testing migrations without a live DB. The script reads `SQLALCHEMY_URL` from the config.
> - **Online**: Executes migrations directly on the database, requiring a valid `SQLALCHEMY_DATABASE_URI` in Flask’s config.

>[!WARNING] Connection Pooling
> - `NullPool` is used to avoid connection leaks in migration scripts. Avoid `pool.DefaultTransaction` in `env.py` to prevent unintended DB connections.
