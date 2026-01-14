**Tags:** #database-migration, #alembic, #sqlalchemy, #table-creation, #session-tracking
**Created:** 2026-01-13
**Type:** documentation

# add_story_sessions_table

## Summary

```
Creates a database table for tracking story sessions with user and world associations.
```

## Details

> This script uses Alembic to generate a SQL migration for adding a `story_sessions` table to a database. The table stores metadata about narrative sessions, including session identifiers, user and world references, and timestamps for creation/activity. It enforces foreign key constraints linking to `users` and `worlds` tables, ensuring referential integrity. Indexes are created for performance optimization on frequently queried columns like `user_id`, `world_id`, `status`, and `last_activity`.

## Key Functions

### `upgrade()`

Executes Alembic’s `upgrade` function to create the `story_sessions` table with all columns, constraints, and indexes.

### `downgrade()`

Executes Alembic’s `downgrade` function to roll back by dropping the table and its indexes.

## Usage

Run this migration via Alembic’s command-line tool (e.g., `alembic upgrade head`) to apply the changes to a database. The table will persist narrative session data with metadata for tracking user engagement, world context, and session progression.

## Dependencies

> `sqlalchemy`
> `alembic`

## Related

- [[None]]

>[!INFO] Foreign Key Constraints
> Enforces relationships between `story_sessions` and `users`/`worlds` tables, preventing orphaned records.

>[!WARNING] Text Columns
> `story_parts`, `description`, `session_metadata`, and `memory_data` use `sa.Text()` for flexible storage but risk performance overhead for large text inputs. Consider truncation limits if needed.
