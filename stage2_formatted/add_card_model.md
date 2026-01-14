**Tags:** #database-migration, #SQLAlchemy, #Alembic, #data-modeling, #JSONB-support
**Created:** 2026-01-13
**Type:** documentation

# add_card_model

## Summary

```
Creates a database table for storing card models with metadata and foreign key constraints.
```

## Details

> This script defines an Alembic migration to add a `cards` table with comprehensive fields for tracking card entities in a system. The table includes:
> - **Primary key (`id`)** and foreign keys (`user_id`, `world_id`) linking to `users` and `worlds` tables.
> - **Text/JSON fields** (`liked_hash_references`, `combined_entity_data`, etc.) for flexible metadata storage via PostgreSQL’s `JSONB`.
> - **Boolean flags** (`is_event`, `is_story_element`) for categorization.
> - **Timestamps** (`created_at`, `updated_at`) for tracking lifecycle.
> 
> The `upgrade()` function creates the table, while `downgrade()` removes it, ensuring reversible migrations.

## Key Functions

### ``upgrade()``

Executes Alembic’s `op.create_table()` to deploy the `cards` schema.

### ``downgrade()``

Executes `op.drop_table()` to revert the migration.

### `ForeignKeyConstraint`

Enforces referential integrity with `users.id` and `worlds.id`.

## Usage

1. Run via Alembic command:
   ```bash
   alembic upgrade head
   ```
2. To revert:
   ```bash
   alembic downgrade head
   ```
3. **Prerequisite**: Ensure PostgreSQL supports `JSONB` (compatible with SQLAlchemy 1.4+).

## Dependencies

> ``alembic``
> ``sqlalchemy``
> ``sqlalchemy.dialects.postgresql``

## Related

- [[Alembic Documentation]]
- [[SQLAlchemy Core]]
- [[PostgreSQL JSONB Guide]]

>[!INFO] JSONB Note
> PostgreSQL’s `JSONB` is used for fields requiring nested data (e.g., `coordinates`, `tags`). Ensure your database version supports it (e.g., PostgreSQL 9.4+).

>[!WARNING] Schema Risk
> Dropping the table (`downgrade`) deletes all data. Test in a staging environment before production.
