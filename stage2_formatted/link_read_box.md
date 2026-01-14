**Tags:** #database-query, #filtering, #orm-query, #api-box, #link-data-processing
**Created:** 2026-01-13
**Type:** documentation

# link_read_box

## Summary

```
Handles reading and filtering Link records from a database with configurable sorting and error handling.
```

## Details

> The `LinkReadBox` class implements a box interface for querying and filtering `Link` records from a SQLAlchemy database. It accepts optional filters (e.g., `user_id`, `link_type`) and an `order_by` field (defaulting to `created_at`). The box constructs a query dynamically, applies filters, counts results, orders them, and returns structured data (list of dictionaries + total count). Error handling logs exceptions and returns a failure response.

## Key Functions

### ``execute(input_data`

BoxInput) -> BoxOutput`**: Orchestrates the query execution, filtering, ordering, and serialization.

### ``__init__(name='link_read')``

Initializes the box with a default name and description.

## Usage

```python
# Example usage:
box = LinkReadBox()
input_data = BoxInput(data={
    'filters': {'user_id': 4, 'link_type': 'physical_personality'},
    'order_by': 'created_at'
})
output = box.execute(input_data)
print(output.data)  # Returns {'links': [...], 'count': X}
```

## Dependencies

> ``..core.box_interface``
> ``models.db``
> ``models.Link``
> ``logging``
> ``typing.Dict``
> ``typing.Any``

## Related

- [[SQLAlchemy Query Patterns]]
- [[Box Interface Design]]

>[!INFO] Dynamic Filtering
> Filters are applied conditionally based on keys in the `filters` dict (e.g., `id`, `user_id`). Missing keys are ignored.

>[!WARNING] Ordering Limitation
> Only fields defined in the `Link` model are supported for ordering. Invalid `order_by` values default to `created_at`.
