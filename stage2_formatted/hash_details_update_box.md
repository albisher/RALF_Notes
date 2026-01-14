**Tags:** #database-update, #security-check, #hash-details, #orm-update
**Created:** 2026-01-13
**Type:** documentation

# hash_details_update_box

## Summary

```
Handles secure updates to existing `HashDetails` records with change tracking.
```

## Details

> This box validates user ownership, applies specified field updates, and logs changes for `HashDetails` records. It supports selective updates to fields like `fields`, `custom_name`, `custom_value`, `tags`, and `story_references`, while enforcing `user_id` and `hash_detail_id` requirements. Changes are tracked before/after updates, and the `updated_at` timestamp is refreshed.

## Key Functions

### ``execute(input_data)``

Core logic—validates input, updates record, and returns serialized output with changes.

### ``HashDetailsUpdateBox.__init__()``

Initializes the box with default name and description.

### ``updatable_fields``

List of fields (`fields`, `custom_name`, etc.) that can be updated via `updates` dict.

## Usage

1. Call with `input_data` containing:
   - `hash_detail_id` (int): Target record ID.
   - `updates` (dict): Field-value pairs to modify.
   - `user_id` (int): User ID for access control.
2. Returns `BoxOutput` with:
   - `success`: Boolean.
   - `data`: Updated record (serialized) and tracked changes.
   - `error`: Message if validation fails.

## Dependencies

> ``..core.box_interface``
> ``models.db``
> ``models.HashDetails``
> ``datetime``

## Related

- [[`Box` interface documentation]]
- [[`HashDetails` model documentation]]

>[!INFO] Change Tracking
> Changes to updatable fields are logged in `changes` dict (e.g., `{'fields': {'before': old, 'after': new}}`).

>[!WARNING] Rollback on Error
> Database transactions are rolled back on exceptions to prevent partial updates.
