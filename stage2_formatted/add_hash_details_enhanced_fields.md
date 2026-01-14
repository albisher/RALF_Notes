**Tags:** #Alembic, #Database Migration, #SQLAlchemy, #PostgreSQL, #Enhanced Fields, #JSONB
**Created:** 2026-01-13
**Type:** documentation

# add_hash_details_enhanced_fields

## Summary

```
Enhances the `hash_details` table by adding flexible JSONB and string columns for metadata tracking.
```

## Details

> This migration script uses Alembic to dynamically extend the `hash_details` table with four new columns:
> 1. **`custom_name`** (String, nullable) – Stores arbitrary custom identifiers.
> 2. **`custom_value`** (PostgreSQL JSONB) – Holds structured metadata as JSON.
> 3. **`tags`** (PostgreSQL JSONB, default `[]`) – Allows dynamic tagging with server-side default empty array.
> 4. **`story_references`** (PostgreSQL JSONB, default `[]`) – Tracks cross-references to stories or related records.
> 
> The script supports both upgrades (adding fields) and downgrades (removing them), ensuring backward compatibility.

## Key Functions

### ``upgrade()``

Adds the four new columns to `hash_details` using SQLAlchemy’s `op.add_column()`.

### ``downgrade()``

Safely removes the columns in reverse order to avoid dependency issues.

## Usage

1. Run via Alembic command:
   ```bash
   alembic upgrade head
   ```
2. To revert:
   ```bash
   alembic downgrade head
   ```
3. Use the new fields in application queries (e.g., `custom_name`, `JSONB` parsing for `custom_value`).

## Dependencies

> ``alembic``
> ``sqlalchemy``
> ``sqlalchemy.dialects.postgresql``

## Related

- [[`f3fa2349e0c7`]]
- [[`hash_details` table schema]]

>[!INFO] Field Order Matters
>Downgrade must drop columns in **reverse order** (e.g., `story_references` → `tags` → `custom_value` → `custom_name`) to avoid SQL errors.

>[!WARNING] JSONB Defaults
>If `tags`/`story_references` are not explicitly set, they default to `[]` (empty array). Ensure application logic handles this edge case.
