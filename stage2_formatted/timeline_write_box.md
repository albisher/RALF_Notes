**Tags:** #database, #timeline, #data-validation, #security, #audit
**Created:** 2026-01-13
**Type:** documentation

# timeline_write_box

## Summary

```
Handles creation of new timeline records with input validation and security checks.
```

## Details

> This `TimelineWriteBox` class implements a box interface for creating new timeline entries in a database. It validates required fields (e.g., `world_id`, `name`), checks user-world ownership, and ensures proper database transaction handling. The class logs success/failure events and returns serialized timeline data or an error message.

## Key Functions

### ``__init__(self, name='timeline_write')``

Initializes the box with a default name and description.

### ``execute(self, input_data`

BoxInput) -> BoxOutput`**: Core method that:

## Usage

1. Pass `timeline_data` (dict with required fields: `world_id`, `name`) and `user_id` via `input_data`.
2. Call `execute()` to create a new timeline.
3. Handle `BoxOutput` response (success/error) and serialized result.

## Dependencies

> ``..core.box_interface``
> ``models.db``
> ``models.Timeline``
> ``models.World``
> ``logging``

## Related

- [[`box_interface]]
- [[World classes)]]

>[!INFO] Required Fields
> Mandatory fields (`world_id`, `name`) must be provided in `timeline_data`; omitting them triggers validation errors.

>[!WARNING] Transaction Rollback
> Database transactions fail silently if an exception occurs; always check `success` flag in `BoxOutput` to avoid partial commits.
