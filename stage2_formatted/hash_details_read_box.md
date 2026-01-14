**Tags:** #database-query, #filtering, #pagination, #orm-query, #box-pattern
**Created:** 2026-01-13
**Type:** code-notes

# hash_details_read_box

## Summary

```
Handles reading and filtering HashDetails records from a database using SQLAlchemy.
```

## Details

> This `HashDetailsReadBox` class implements a box pattern for querying and filtering `HashDetails` records from a SQLAlchemy database. It accepts configurable filters (e.g., `user_id`, `asset_type`), applies sorting, and supports pagination via `limit`/`offset`. The output includes serialized records and a total count of matching results. Error handling logs exceptions and returns a failure response.

## Key Functions

### ``__init__``

Initializes the box with a default name and description.

### ``execute``

Orchestrates the query execution:

### `Orders results by a specified field (default`

`created_at`).

## Usage

```python
box = HashDetailsReadBox()
input_data = {
    'filters': {'user_id': 4, 'asset_type': 'character'},
    'order_by': 'created_at',
    'limit': 10,
    'offset': 0
}
output = box.execute(BoxInput(data=input_data))
```
- **Input**: A dictionary with optional filters, ordering, and pagination keys.
- **Output**: A `BoxOutput` containing:
  - `hash_details`: List of dictionaries (serialized records).
  - `count`: Total matching records.
  - `limit`/`offset`: Applied pagination values.

## Dependencies

> ``..core.box_interface``
> ``models.db``
> ``models.HashDetails``
> ``logging``
> ``typing.Dict``
> ``typing.Any``

## Related

- [[SQLAlchemy Query Patterns]]
- [[Box Pattern Design]]

>[!INFO] Dynamic Field Handling
> Uses `getattr` to safely apply ordering by any `HashDetails` attribute, defaulting to `created_at` if invalid.

>[!WARNING] Error Handling
> Logs exceptions with `exc_info=True` for debugging but returns a generic error message to avoid exposing stack traces.
