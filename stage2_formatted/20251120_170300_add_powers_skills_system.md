**Tags:** #database-migration, #alembic, #sqlalchemy, #powers-system, #skills-system, #json-storage
**Created:** 2026-01-13
**Type:** database-migration

# 20251120_170300_add_powers_skills_system

## Summary

```
Adds a powers and skills system to a game/database by creating a `powers` table and JSON fields for abilities/skills in `cards`.
```

## Details

> This migration script implements a **powers and skills** system using SQLAlchemy and Alembic. It creates a dedicated `powers` table to store ability metadata (e.g., name, type, level) linked via foreign keys to `worlds` and `users`. The `cards` table is extended with JSON fields (`powers` and `skills`) to store dynamic, nested data for each card instance. The `metadata` field in the `powers` table allows flexible JSON storage for custom attributes.

## Key Functions

### ``upgrade()``

Executes Alembic’s upgrade logic to:

### ``downgrade()``

Reverts changes by:

## Usage

1. Run via Alembic command (`alembic upgrade head`) to apply changes.
2. Use the `powers` table to manage abilities (e.g., `INSERT INTO powers (...) VALUES (...)`).
3. Store abilities/skills in `cards` via JSON (e.g., `{"powers": [...], "skills": [...]}`).

## Dependencies

> ``alembic``
> ``sqlalchemy``
> ``sqlalchemy.dialects.postgresql` (for `JSONB` support).`

## Related

- [[`20251120_170100`]]
- [[`cards` table schema]]
- [[`worlds` tables]]

>[!INFO] JSONB Limitation
> JSONB fields (`powers`/`skills`) in `cards` are stored as arrays. For nested structures, flatten or use stringified JSON (e.g., `{"powers": "[...]"}`). Avoid circular references.

>[!WARNING] Foreign Key Constraints
> Ensure `world_id`/`user_id` exist in `worlds`/`users` tables before running `upgrade()`. Otherwise, `ForeignKeyConstraint` violations will occur.
