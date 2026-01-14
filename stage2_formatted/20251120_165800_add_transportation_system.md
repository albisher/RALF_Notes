**Tags:** #database-migration, #alembic, #sqlalchemy, #transportation-system, #card-fields, #jsonb-support
**Created:** 2026-01-13
**Type:** documentation

# 20251120_165800_add_transportation_system

## Summary

```
Adds a transportation system model and associated card fields to a database schema via Alembic migration.
```

## Details

> This migration script introduces a `transportations` table to store details about transportation modes (e.g., train, bus) with metadata support via `JSONB`. It also extends the `cards` table to link transportation entries via `transportation_id` and adds a `available_transportation` JSONB field for dynamic configuration. The schema enforces foreign key constraints linking to `worlds` and `users` tables.

## Key Functions

### `upgrade()`

Executes Alembic’s `upgrade` function to create the `transportations` table, add columns to `cards`, and establish foreign keys.

### `downgrade()`

Reverts changes by dropping the `transportations` table, removing `cards` columns, and removing the foreign key constraint.

## Usage

Run via Alembic command:
```bash
alembic upgrade head
```
To revert:
```bash
alembic downgrade head
```

## Dependencies

> ``alembic``
> ``sqlalchemy``
> ``sqlalchemy.dialects.postgresql` (for `JSONB` support).`

## Related

- [[`20251120_165700`]]
- [[users tables`]]

>[!INFO] Foreign Key Handling
> `SET NULL` on `cards.transportation_id` deletes linked records if a transportation entry is dropped, preserving data integrity.

>[!WARNING] JSONB Defaults
> `available_transportation` defaults to `[]` (empty array), but invalid JSON may corrupt data if not validated.
