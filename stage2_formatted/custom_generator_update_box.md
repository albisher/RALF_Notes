**Tags:** #database-update, #custom-generator, #security-check, #orm-update
**Created:** 2026-01-13
**Type:** documentation

# custom_generator_update_box

## Summary

```
Handles secure updates to existing custom generator records via a database box interface.
```

## Details

> This box implements a secure, transactional update mechanism for `CustomGenerator` records. It validates input fields (`generator_id`, `user_id`), checks ownership, and applies specified updates to select fields (`name`, `description`, `type`, etc.) while tracking changes. The update includes an `updated_at` timestamp and returns the modified record, change history, and success status.

## Key Functions

### `execute`

Core logic to validate input, verify ownership, apply updates, and commit changes.

### `CustomGeneratorUpdateBox`

Inherits from `Box` to integrate with the box interface system.

### `updatable_fields`

List of allowed fields for updates (hardcoded in the class).

## Usage

1. Call with required fields: `generator_id`, `updates` (dict of field-value pairs), and `user_id`.
2. Example input:
   ```json
   {
     "generator_id": 123,
     "updates": {"name": "New Name", "is_active": false},
     "user_id": 456
   }
   ```
3. Returns:
   - `success`: Boolean (True on success).
   - `data.generator`: Serialized updated record.
   - `data.changes`: Tracked field differences.
   - `error`: Message if validation fails.

## Dependencies

> ``..core.box_interface``
> ``models.db``
> ``models.CustomGenerator``
> ``datetime``

## Related

- [[Database ORM Models]]
- [[Box Interface System]]

>[!INFO] Change Tracking
> Changes are logged in `changes` dict as `{'before': old_value, 'after': new_value}` for each updated field.

>[!WARNING] Rollback on Error
> If an exception occurs, the database session is rolled back to maintain consistency.
