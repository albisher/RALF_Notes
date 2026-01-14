**Tags:** #database, #custom_generator, #box_interface, #security, #validation, #ORM
**Created:** 2026-01-13
**Type:** code-notes

# custom_generator_write_box

## Summary

```
Handles creation of new custom generator records with input validation and database persistence.
```

## Details

> This box class (`CustomGeneratorWriteBox`) implements a database interaction for creating new `CustomGenerator` records. It validates required fields (user_id, generator_id, name, type, function_name) and checks for duplicate entries before persisting via SQLAlchemy. The `execute()` method processes input data, performs checks, and returns a serialized generator dictionary or error message.

## Key Functions

### ``execute(input_data)``

Core logic—validates input, checks for duplicates, creates record, and commits transaction.

### ``CustomGeneratorWriteBox``

Main class inheriting from `Box` for database interaction.

### ``BoxInput/BoxOutput``

Defines input/output schemas for the box interface.

## Usage

1. Pass `generator_data` (dict with required fields) and `user_id` via `input_data`.
2. Call `execute()` to create a new generator.
3. Handle `BoxOutput` success/error responses.

## Dependencies

> ``..core.box_interface``
> ``models.db``
> ``models.CustomGenerator``
> ``logging``
> ``typing``

## Related

- [[SQLAlchemy Core]]
- [[CustomGenerator Model]]
- [[Box Interface Documentation]]

>[!INFO] Required Fields
> All fields (`user_id`, `generator_id`, `name`, `type`, `function_name`) must be provided in `generator_data`; omitting any will trigger validation errors.

>[!WARNING] Duplicate Check
> The box prevents duplicate entries by querying `CustomGenerator` for existing records with matching `user_id` and `generator_id`. Ensure uniqueness before calling this box.
