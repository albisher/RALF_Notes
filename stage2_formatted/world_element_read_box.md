**Tags:** #database-query, #filtering, #orm-query, #data-processing, #box-pattern
**Created:** 2026-01-13
**Type:** documentation

# world_element_read_box

## Summary

```
Handles reading and filtering WorldElement records from a database using SQLAlchemy.
```

## Details

> This box class (`WorldElementReadBox`) implements a SQLAlchemy-based query processor for retrieving filtered and ordered `WorldElement` records from a database. It accepts filter criteria (e.g., `world_id`, `user_id`) and an optional `order_by` field (defaulting to `created_at`). The class constructs a query dynamically, applies filters, counts results, orders them, and serializes the results into dictionaries. Error handling logs exceptions and returns a failure response.

## Key Functions

### ``execute(input_data`

BoxInput) -> BoxOutput`**: Executes the query logic, processes input filters, orders results, and returns serialized data with a count.

### ``__init__(name='world_element_read')``

Initializes the box with a default name and description.

## Usage

1. Instantiate `WorldElementReadBox`.
2. Call `execute()` with a `BoxInput` containing:
   - `filters` (dict): Key-value pairs for filtering (e.g., `{'world_id': 35}`).
   - `order_by` (str, optional): Field to order by (default: `'created_at'`).
3. The output includes:
   - `elements`: List of dictionaries representing filtered results.
   - `count`: Total matching records.

## Dependencies

> ``..core.box_interface``
> ``models.db``
> ``models.WorldElement``
> ``logging``
> ``typing.Dict``
> ``typing.Any``

## Related

- [[SQLAlchemy Query Patterns]]
- [[Box Pattern Design]]

>[!INFO] Dynamic Query Construction
> Filters are applied conditionally based on keys in the input `filters` dict, ensuring only relevant conditions are added to the query.

>[!WARNING] Error Handling
> All exceptions are logged with `exc_info=True` and returned as a failure response with a descriptive error message. Avoid bare `except` blocks to prevent masking critical issues.
