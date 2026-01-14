**Tags:** #database-operations, #audit-logging, #security-checks, #transaction-management, #foreign-key-handling
**Created:** 2026-01-13
**Type:** code-notes

# world_deletion_box

## Summary

```
Handles safe deletion of worlds and their associated data with audit logging and security checks.
```

## Details

> The `WorldDeletionBox` class implements a secure deletion mechanism for worlds and their related entities (cards, world elements, timelines, and events). It performs input validation, verifies user ownership, and ensures proper cleanup while preventing audit service conflicts. The code disables the audit service temporarily to avoid foreign key violations during deletion, then manually creates an audit log entry before deletion to preserve the world's state.

## Key Functions

### `execute`

Orchestrates the deletion workflow, including validation, audit logging, and cleanup.

### `WorldDeletionBox`

Core class inheriting from `Box` for modular box functionality.

### `audit_service.disable_auditing()`

Temporarily disables auditing to prevent race conditions during deletion.

### `AuditLog creation`

Manually records world state before deletion to maintain audit trail integrity.

## Usage

1. Instantiate `WorldDeletionBox` and call `execute()` with input data containing `world_id`, `user_id`, and optional `force` flag.
2. Input must include required fields; missing fields return an error.
3. The box verifies world ownership, counts deletable items, disables auditing, logs state, and performs deletions in a transactional manner.

## Dependencies

> ``..core.box_interface``
> ``models.db``
> ``models.World``
> ``models.Card``
> ``models.WorldElement``
> ``models.Timeline``
> ``models.TimelineEvent``
> ``models.AuditLog``
> ``audit_service``
> ``flask` (for request context)`
> ``logging``
> ``typing``

## Related

- [[Database Transaction Management Guide]]
- [[Audit Service Implementation]]
- [[Security Check Best Practices]]

>[!INFO] Critical Audit Workflow
> The code disables auditing *before* manually creating an audit log entry to prevent the audit service’s event listener from attempting to log during deletion, which would fail due to the world’s non-existent state in the database.

>[!WARNING] Audit Log Fallback
> If manual audit log creation fails, the deletion proceeds without logging, but this may reduce traceability for debugging. The `force` flag bypasses all checks, including audit logging.
