**Tags:** #database, #link-management, #box-component, #security, #audit-trail
**Created:** 2026-01-13
**Type:** code-component

# link_write_box

## Summary

```
Handles creation of new Link records in a database with input validation and transaction management.
```

## Details

> The `LinkWriteBox` class implements a box interface for creating new `Link` records in a database. It validates required fields (`user_id`, `source_hash`, `target_hash`, `link_type`) before persisting the record. The `execute()` method processes input data, performs database operations (commit/rollback), and returns a serialized link object with metadata. Error handling includes logging and rollback on failure.

## Key Functions

### ``LinkWriteBox``

Core class for link creation logic.

### ``execute()``

Validates input, creates a new `Link` record, and commits/rollbacks transactions.

### ``Link` model`

Database model representing a link with fields like `user_id`, `source_hash`, `target_hash`, etc.

## Usage

1. Instantiate `LinkWriteBox`.
2. Call `execute()` with `BoxInput` containing `link_data` (dict) and `user_id`.
3. Handle `BoxOutput` (success/failure) to retrieve the created link or error message.

## Dependencies

> ``..core.box_interface``
> ``models.db``
> ``models.Link``
> ``logging``

## Related

- [[core]]
- [[models]]
- [[models]]

>[!INFO] Required Fields
> All `link_data` must include `source_hash`, `target_hash`, and `link_type`; `user_id` is mandatory for security.

>[!WARNING] Transaction Safety
> Database commits/rollbacks ensure atomicity. Caller must handle exceptions externally if needed.
