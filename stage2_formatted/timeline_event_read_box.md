**Tags:** #database-query, #data-fetching, #filtering, #sqlalchemy, #event-processing
**Created:** 2026-01-13
**Type:** documentation

# timeline_event_read_box

## Summary

```
Handles reading and filtering of `TimelineEvent` records from a database with configurable sorting and counting.
```

## Details

> This box implements a SQLAlchemy-based query processor for fetching `TimelineEvent` records. It accepts optional filters (e.g., `timeline_id`, `world_id`) and an `order_by` field (defaulting to `event_date`). The query dynamically applies filters, counts matching records, orders results, and serializes them into dictionaries. Error handling logs exceptions and returns a failure response.

## Key Functions

### ``__init__``

Initializes the box with a default name and description.

### ``execute``

Orchestrates the query execution:

## Usage

1. **Input**:
   ```json
   {
     "filters": {"timeline_id": 5, "world_id": 35},
     "order_by": "event_date"
   }
   ```
2. **Output**:
   ```json
   {
     "events": [...],  // List of event dictionaries
     "count": 10       // Total matching records
   }
   ```
3. **Error Handling**: Logs exceptions and returns a `success=False` response with details.

## Dependencies

> ``..core.box_interface``
> ``models.db``
> ``models.TimelineEvent``
> ``logging``
> ``typing.Dict``
> ``typing.Any``

## Related

- [[`Box` interface documentation]]
- [[`TimelineEvent` model documentation]]

>[!INFO] Dynamic Filtering
> Supports filtering by `timeline_id`, `world_id`, `user_id`, or `event_type` via the `filters` input.

>[!WARNING] Ordering Safety
> Only applies `order_by` if the specified field exists in `TimelineEvent`; otherwise, defaults to `event_date`.
