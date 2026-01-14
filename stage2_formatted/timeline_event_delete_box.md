**Tags:** #database-operation, #security-check, #event-management, #box-component
**Created:** 2026-01-13
**Type:** code-notes

# timeline_event_delete_box

## Summary

```
Handles secure deletion of a `TimelineEvent` record with validation and logging.
```

## Details

> This box validates input (`event_id` and `user_id`), checks ownership via SQL query, deletes the record from the database, and returns confirmation. It includes error handling, logging, and transaction rollback on failure.

## Key Functions

### ``execute(self, input_data`

BoxInput) -> BoxOutput`**: Core logic—validates inputs, checks ownership, deletes event, and logs success/failure.

### ``__init__(self, name='timeline_event_delete')``

Initializes the box with a default name and description.

## Usage

1. Pass `event_id` and `user_id` in `input_data.data`.
2. Call `execute()` to trigger deletion.
3. Handle `BoxOutput` (success/failure) in downstream logic.

## Dependencies

> ``..core.box_interface``
> ``models.db``
> ``models.TimelineEvent``
> ``logging``

## Related

- [[`core]]
- [[`models]]

>[!INFO] Ownership Check
> Uses `db.session.query` to verify `user_id` matches the event’s owner before deletion.

>[!WARNING] Transaction Safety
> Calls `db.session.rollback()` on any exception to prevent partial deletions.
