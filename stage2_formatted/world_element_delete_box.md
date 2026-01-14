**Tags:** #database, #security, #deletion, #ORM, #authentication
**Created:** 2026-01-13
**Type:** documentation

# world_element_delete_box

## Summary

```
Handles secure deletion of WorldElement records with validation and logging.
```

## Details

> This box validates user ownership, checks for required inputs (`element_id` and `user_id`), and deletes a WorldElement record from the database using SQLAlchemy’s session management. It includes error handling for missing inputs, unauthorized access, and database exceptions, with logging for success/failure cases.

## Key Functions

### `execute`

Deletes a WorldElement record after validating ownership and input data.

### `WorldElementDeleteBox`

Base class inheriting from `Box` with initialization for deletion operations.

## Usage

1. Call with `element_id` and `user_id` in `input_data`.
2. Returns `BoxOutput` with `success`, `deleted_id`, and `message` on success; error details on failure.
3. Requires SQLAlchemy session (`db.session`) for database operations.

## Dependencies

> ``..core.box_interface``
> ``models.db``
> ``models.WorldElement``
> ``logging``

## Related

- [[SQLAlchemy Session Management]]
- [[Box Interface Documentation]]

>[!INFO] Input Validation
> Mandatory `element_id` and `user_id` must be provided; missing values trigger immediate rejection.

>[!WARNING] Security Risk
> Directly querying `WorldElement.query.filter_by()` exposes potential SQL injection if `element_id`/`user_id` are not sanitized (though this code assumes proper input handling).
