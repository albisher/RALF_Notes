**Tags:** #database-query, #filtering, #orm-query, #api-box, #custom-generator
**Created:** 2026-01-13
**Type:** documentation

# custom_generator_read_box

## Summary

```
Handles reading and filtering CustomGenerator records from a database with configurable sorting and error handling.
```

## Details

> This `CustomGeneratorReadBox` class implements a box interface for querying and filtering records from the `CustomGenerator` model in a SQLAlchemy-based database. It accepts filter criteria (e.g., `user_id`, `type`) and an optional `order_by` field (defaulting to `created_at`). The box constructs a SQLAlchemy query dynamically based on provided filters, applies sorting, and returns a structured output containing matched records and their count. Error handling logs exceptions and returns a failure response.

## Key Functions

### ``execute(input_data`

BoxInput) -> BoxOutput`**: Orchestrates the entire query process—filtering, ordering, execution, and serialization—returning either successful results or an error message.

### ``__init__(name='custom_generator_read')``

Initializes the box with a default name and description, inheriting from the parent `Box` class.

## Usage

1. **Input**:
   ```python
   {
       'filters': {'user_id': 4, 'type': 'physical_form'},  # Optional filters
       'order_by': 'created_at'  # Optional, defaults to 'created_at'
   }
   ```
2. **Output**:
   ```python
   {
       'generators': [dicts of matched records],
       'count': int  # Total matching records
   }
   ```
3. **Example Call**:
   ```python
   box = CustomGeneratorReadBox()
   result = box.execute(BoxInput(data={'filters': {...}}))
   ```

## Dependencies

> ``..core.box_interface``
> ``models.db``
> ``models.CustomGenerator``
> ``logging``

## Related

- [[SQLAlchemy Query Patterns]]
- [[Box Interface Documentation]]

>[!INFO] Dynamic Filtering
> Filters are applied conditionally based on keys in the `filters` dict (e.g., `id`, `user_id`). Missing keys are ignored.

>[!WARNING] Ordering Limitation
> Only fields defined in `CustomGenerator` (e.g., `created_at`) can be used for ordering. Invalid `order_by` defaults to `created_at`.
