**Tags:** #database-management, #backup-and-restore, #redis-integration, #flask-service, #data-reset
**Created:** 2026-01-13
**Type:** documentation-research

# reset_service

## Summary

```
Service for managing complete data resets with backup capabilities, including database, files, and Redis cache.
```

## Details

> The `ResetService` class provides functionality to reset backend data in a controlled manner, allowing users to choose between partial or complete resets while optionally creating backups. It integrates with Redis for caching and tracks data counts across multiple database tables (e.g., `User`, `World`, `Timeline`). The service supports different reset options like database-only, file-only, or full reset, with corresponding preservation logic. It also includes backup functionality to export database data and copy generated files before deletion.

## Key Functions

### ``__init__()``

Initializes Redis connection with error handling.

### ``get_reset_options()``

Returns available reset options and current data counts (users, worlds, elements, etc.) from the database and Redis.

### ``create_backup()``

Creates a timestamped backup directory containing database JSON export and copied generated stories files.

### ``_export_database_data()``

(Internal) Exports all database records to a JSON file (not shown in snippet but implied via `create_backup`).

## Usage

1. **Initialize**: Create an instance of `ResetService`.
2. **Get Options**: Call `get_reset_options()` to see available reset strategies.
3. **Backup**: Use `create_backup()` to save data before resetting.
4. **Reset**: Implement logic to execute the chosen reset option (e.g., delete files, truncate tables, or clear Redis).

## Dependencies

> ``os``
> ``shutil``
> ``logging``
> ``typing``
> ``datetime``
> ``flask``
> ``redis``
> ``models.db``
> ``User``
> ``World``
> ``WorldElement``
> ``Timeline``
> ``TimelineEvent``
> ``StorySession``
> ``AuditLog``
> ``config.get_redis_url`.`

## Related

- [[Database Schema Documentation]]
- [[Redis Configuration Guide]]
- [[Backup Procedures]]

>[!INFO] Critical Backup Path
> The backup directory path (`.taskmaster/backups/`) is hardcoded. Ensure this directory exists and is writable to avoid failures.

>[!WARNING] Database Export Risk
> `_export_database_data()` (not shown) exports raw SQL records to JSON. Ensure the output file is securely stored or deleted after backup to prevent data leaks.
