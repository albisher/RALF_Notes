**Tags:** #database-update, #card-management, #security-check, #transaction-logging
**Created:** 2026-01-13
**Type:** documentation

# card_update_box

## Summary

```
Handles secure updates to existing Card records in a database with change tracking.
```

## Details

> The `CardUpdateBox` class implements a secure, transactional update mechanism for existing Card records. It validates input, checks user ownership, tracks modified fields, and ensures atomicity via database commits/rollbacks. The system supports partial updates to predefined fields while maintaining auditability through before/after comparisons.

## Key Functions

### ``execute(input_data`

BoxInput) -> BoxOutput`**: Core method that processes updates, validates permissions, and returns the updated card with change history.

### ``__init__(name='card_update')``

Initializes the box with a default name and description.

### ``updatable_fields``

Hardcoded list of allowed fields for modification (e.g., `card_name`, `image_url`).

## Usage

1. Call `CardUpdateBox.execute()` with a `BoxInput` containing:
   - `card_id` (int): Target card identifier.
   - `updates` (dict): Field-value pairs to modify.
   - `user_id` (int): User ID for permission checks.
2. Handle the returned `BoxOutput` (success/failure + data).

## Dependencies

> ``..core.box_interface``
> ``models.db``
> ``models.Card``
> ``logging``
> ``typing``
> ``datetime``

## Related

- [[Card Model Documentation]]
- [[Box Interface Specification]]

>[!INFO] Change Tracking
> The `changes` dict records only modified fields with `before/after` values, enabling audit trails.

>[!WARNING] Timestamp Handling
> String timestamps (e.g., ISO format) must be explicitly converted to `datetime` objects for updates.
