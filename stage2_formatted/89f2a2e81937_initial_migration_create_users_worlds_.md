**Tags:** #database-migration, #alembic, #sqlalchemy, #users-worlds-entities, #jsonb-support
**Created:** 2026-01-13
**Type:** code-notes

# 89f2a2e81937_initial_migration_create_users_worlds_

## Summary

```
Creates initial database tables for user management, world systems, and world elements with Alembic migration.
```

## Details

> This migration script uses Alembic to generate SQL commands for creating three core tables: `users`, `worlds`, and `world_elements`. The `users` table stores authentication and profile data, while `worlds` links users to their virtual environments. The `world_elements` table holds configurable, JSON-stored attributes for each world. The schema includes timestamps, active status flags, and foreign key constraints to enforce referential integrity. JSONB columns support nested data structures for flexible element definitions.

## Key Functions

### `upgrade()`

Executes Alembic-generated commands to create tables with specified columns, indexes, and constraints.

### `downgrade()`

Reverts changes by dropping tables and their indexes in reverse order.

### `users table`

Manages user accounts with email uniqueness enforced via an index.

### `worlds table`

Links users to their virtual worlds with foreign key constraint on `user_id`.

### `world_elements table`

Stores world-specific elements with optional JSON data and generation hashes.

## Usage

Run via Alembic command-line tool:
```bash
alembic upgrade head
```
For rollback:
```bash
alembic downgrade head
```

## Dependencies

> `sqlalchemy`
> `postgresql (for JSONB support)`
> `alembic`

## Related

- [[Alembic Documentation]]
- [[SQLAlchemy Core]]
- [[PostgreSQL JSONB Guide]]

>[!INFO] JSONB Support
> Requires PostgreSQL 9.4+ for `JSONB` type; ensure database version matches.

>[!WARNING] Foreign Key Constraints
> Always test `downgrade()` in a staging environment—foreign key rollbacks may fail if referenced data exists.
