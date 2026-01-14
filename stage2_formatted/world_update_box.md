**Tags:** #database, #world-management, #update-operation, #security-check, #serialization
**Created:** 2026-01-13
**Type:** documentation

# world_update_box

## Summary

```
Handles secure updates to existing world records in a database with change tracking and validation.
```

## Details

> This `WorldUpdateBox` class implements a box interface for updating existing `World` records in a database. It validates input (requires `world_id` and `user_id`), checks ownership, and updates specified fields while tracking changes. Special logic handles `is_default` updates by unsetting other defaults. The update includes a timestamp and returns the modified world data along with a history of changes made.

## Key Functions

### ``execute(input_data`

BoxInput) -> BoxOutput`**: Core method that validates input, updates world records, and returns results.

### ``__init__(name='world_update')``

Initializes the box with a default name and description.

### ``updatable_fields``

List of allowed fields for updates (`name`, `description`, `world_type`, `status`, `is_default`, `time_system`).

## Usage

1. Call `WorldUpdateBox.execute()` with a `BoxInput` containing:
   - `world_id` (int): Target world ID.
   - `updates` (dict): Fields to update (e.g., `{'name': 'New Name'}`).
   - `user_id` (int): User ID for security checks.
2. Returns a `BoxOutput` with:
   - `success`: Boolean indicating success.
   - `data.world`: Updated world data (serialized).
   - `data.changes`: Dictionary of modified fields (before/after).
   - `error`: Message if validation fails.

## Dependencies

> ``..core.box_interface``
> ``models.db``
> ``models.World``
> ``logging``
> ``datetime``

## Related

- [[SQL database operations]]
- [[security validation in data boxes]]

>[!INFO] Change Tracking
> The `changes` dictionary records only fields that were modified, preserving the original values before updates.

>[!WARNING] Default Conflict
> Setting `is_default=True` automatically disables other worlds marked as default in the same user’s session.
