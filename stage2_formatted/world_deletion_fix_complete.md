**Tags:** #database-error-handling, #audit-logging, #foreign-key-constraints, #transaction-management, #world-deletion, #error-prevention
**Created:** 2026-01-14
**Type:** documentation

# world_deletion_fix_complete

## Summary

```
Fixes a 500 error during world deletion by preventing foreign key constraint violations in audit logging during deletion.
```

## Details

> This document details a complete fix for a 500 error encountered when attempting to delete worlds from the UI. The root cause was a foreign key constraint violation in the audit service, where audit logs were created after the world was deleted, referencing a non-existent world ID. The solution temporarily disables auditing during deletion, cleans up all related records (audit logs, story sessions, world elements, and timelines), and ensures proper transaction rollback and auditing restoration. Testing confirmed successful deletion with complete cleanup of associated data.

## Key Functions

### `delete_world`

Handles world deletion with auditing disable/enable.

### `audit_service.disable_auditing()`

Temporarily stops audit log creation.

### `audit_service.enable_auditing()`

Restores audit log creation after deletion.

### `World.query.filter_by()`

Retrieves world data for deletion.

### `AuditLog.query.filter_by()`

Deletes audit logs referencing the world.

### `StorySession.query.filter_by()`

Deletes story sessions for the world.

### `WorldElement.query.filter_by()`

Deletes world elements (with cascading to timeline events).

### `Timeline.query.filter_by()`

Deletes timelines (with cascading to timeline events).

## Usage

1. Call the `/api/worlds/<world_id>` DELETE endpoint with proper authentication.
2. The endpoint temporarily disables auditing, cleans up related records, and re-enables auditing.
3. Ensure proper error handling and transaction management are in place for database operations.

## Dependencies

> `SQLAlchemy`
> `Flask`
> `psycopg2 (PostgreSQL adapter)`
> `JWT library`
> `audit_service module`
> `models (World`
> `AuditLog`
> `StorySession`
> `WorldElement`
> `Timeline).`

## Related

- [[World Deletion API Design]]
- [[Audit Service Implementation]]
- [[Database Schema for Worlds]]
- [[Error Handling Best Practices]]

>[!INFO] Critical Audit Disabling
> The solution disables auditing during deletion to prevent foreign key constraint violations. This is a temporary measure and restores auditing afterward to maintain data integrity and audit trails.


>[!WARNING] Manual Cleanup Required
> Audit logs and story sessions must be explicitly deleted before deletion to avoid orphaned records. The solution handles cascading deletions for WorldElement and Timeline but requires manual cleanup for AuditLog and StorySession.
