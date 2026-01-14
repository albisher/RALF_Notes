**Tags:** #database-operation, #security-check, #link-management, #transaction-handling
**Created:** 2026-01-13
**Type:** documentation

# link_delete_box

## Summary

```
Handles secure deletion of Link records from a database with input validation and ownership verification.
```

## Details

> The `LinkDeleteBox` class implements a box interface for deleting Link records from a database. It validates required inputs (`link_id` and `user_id`), checks ownership via SQL query, and performs a transactional delete. If successful, it logs the deletion and returns the deleted link ID and confirmation message; otherwise, it returns an error. The class uses SQLAlchemy’s `db.session` for database operations and includes rollback on failure.

## Key Functions

### ``LinkDeleteBox``

Core class encapsulating link deletion logic.

### ``execute()``

Handles the deletion workflow with input validation, ownership check, and transaction management.

### ``__init__()``

Initializes the box with a default name and description.

## Usage

1. Instantiate `LinkDeleteBox` (e.g., `box = LinkDeleteBox()`).
2. Call `execute()` with a `BoxInput` object containing `link_id` and `user_id`.
3. Handle the returned `BoxOutput` (success/error status, data, or error message).

## Dependencies

> ``..core.box_interface``
> ``models.db``
> ``models.Link``
> ``logging``

## Related

- [[`core]]
- [[`models]]
- [[`models]]

>[!INFO] Input Validation
> Always checks for `link_id` and `user_id` presence before proceeding; missing values trigger immediate error.

>[!WARNING] Transaction Safety
> Uses `db.session.commit()`/`rollback()` to ensure atomicity; failures abort the operation.
