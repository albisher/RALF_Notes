**Tags:** #database-migration, #sqlalchemy, #alembic, #link-model, #postgresql
**Created:** 2026-01-13
**Type:** documentation

# add_link_model

## Summary

```
Creates a migration script to add a `links` table for storing user-generated connections between resources.
```

## Details

> This script uses Alembic to generate a database migration for adding a new `links` table. It defines a table with columns for tracking user connections, including identifiers for source and target resources (via `source_hash` and `target_hash`), metadata storage (`meta_data`), timestamps (`created_at`, `updated_at`), and a foreign key constraint linking to a `users` table. The `link_type` and `link_name` fields allow categorization and naming of connections. The `downgrade()` function reverses the operation by dropping the table.

## Key Functions

### `upgrade()`

Creates the `links` table with specified columns and constraints.

### `downgrade()`

Removes the `links` table to revert changes.

## Usage

Run this script via Alembic’s `upgrade` command to apply the migration to a PostgreSQL database. The migration adds a new table for storing inter-resource links with user associations.

## Dependencies

> `sqlalchemy`
> `alembic`
> `postgresql`

## Related

- [[None]]

>[!INFO] Important Note
> Ensure the `users` table exists before running this migration, as the `links` table references it via a foreign key constraint.

>[!WARNING] Caution
> If `meta_data` is frequently updated, consider indexing it for performance optimization.
