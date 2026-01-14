**Tags:** #database-query, #data-fetching, #filtering, #eager-loading, #event-integration
**Created:** 2026-01-13
**Type:** documentation

# timeline_read_box

## Summary

```
Handles reading and filtering Timeline records from a database with optional event inclusion and counting.
```

## Details

> The `TimelineReadBox` class implements a box interface for querying and processing Timeline records from a database. It supports filtering by various fields (e.g., `world_id`, `user_id`), ordering by `created_at`, and optionally includes related events via eager loading. The class constructs SQLAlchemy queries dynamically based on input filters, executes them, and returns structured data (timelines with events) along with a count of matching records. Error handling logs exceptions and returns a failure response.

## Key Functions

### ``__init__(self, name='timeline_read')``

Initializes the box with a default name and description.

### ``execute(self, input_data`

BoxInput) -> BoxOutput`**: Core method that:

## Usage

1. Instantiate `TimelineReadBox` (e.g., `box = TimelineReadBox()`).
2. Call `execute()` with a `BoxInput` object containing:
   - `filters` (dict): Key-value pairs for filtering (e.g., `{'world_id': 35}`).
   - `order_by` (str): Field to order by (default: `'created_at'`).
   - `include_events` (bool): Include nested events (default: `True`).
3. Output includes:
   - `timelines`: List of dictionaries with filtered records and events.
   - `count`: Total matching records.

## Dependencies

> ``..core.box_interface``
> ``models.db``
> ``models.Timeline``
> ``models.Event` (SQLAlchemy ORM components).`

## Related

- [[core]]
- [[Timeline]]
- [[Event]]

>[!INFO] Dynamic Query Filtering
> Filters are applied conditionally based on keys in the `filters` input (e.g., `world_id`, `user_id`). Missing keys are ignored.

>[!WARNING] Ordering Limitation
> Only fields directly accessible via `Timeline` (e.g., `created_at`) are supported for ordering. Invalid fields raise an error.
