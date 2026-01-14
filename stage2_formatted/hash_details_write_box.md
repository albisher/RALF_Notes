**Tags:** #database, #hashing, #security, #data-validation, #orm, #transaction
**Created:** 2026-01-13
**Type:** code-notes

# hash_details_write_box

## Summary

```
Handles creation of new HashDetails records with validation and uniqueness checks.
```

## Details

> This `HashDetailsWriteBox` class implements a box interface for creating new records in a database via SQLAlchemy’s `HashDetails` model. It validates required fields (`user_id`, `seed`, `hash_value`, `asset_type`), checks for duplicate entries (same `user_id`, `seed`, and `asset_type`), and serializes the result into a structured dictionary. The operation is wrapped in a transaction, ensuring atomicity. Logging is used for auditing success/failure events.

## Key Functions

### ``execute(self, input_data`

BoxInput) -> BoxOutput`**: Core logic to validate input, check for duplicates, create the record, and return serialized output.

### ``HashDetailsWriteBox``

Wrapper class inheriting from `Box` for database interaction.

### ``BoxInput`/`BoxOutput``

Defined in `box_interface` for standardized input/output handling.

## Usage

1. Call `execute()` with `BoxInput` containing:
   - `user_id` (int)
   - `hash_data` (dict) with required fields (`seed`, `hash_value`, `asset_type`) and optional extras (`fields`, `custom_name`, etc.).
2. Returns `BoxOutput` with:
   - `success`: Boolean
   - `data`: Serialized record (e.g., `id`, `seed`, `asset_type`)
   - `error`: Message if validation fails.

## Dependencies

> ``..core.box_interface``
> ``models.db``
> ``models.HashDetails``
> ``logging``

## Related

- [[`box_interface]]
- [[`models]]
- [[`HashDetails` model definition]]

>[!INFO] Required Fields
> Mandatory fields (`user_id`, `seed`, `hash_value`, `asset_type`) must be provided in `hash_data`. Missing any will trigger a `success=False` response.

>[!WARNING] Duplicate Check
> The box prevents duplicate entries by querying the database for existing records with identical `user_id`, `seed`, and `asset_type`. Override this logic if uniqueness rules differ.
