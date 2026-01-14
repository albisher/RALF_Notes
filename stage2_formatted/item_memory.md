**Tags:** #data-tracking, #time-series, #location-based, #state-management, #in-memory-storage
**Created:** 2026-01-13
**Type:** code-notes

# item_memory

## Summary

```
Tracks and queries items by location and time, storing state changes in a time-series manner.
```

## Details

> The `ItemMemoryBox` class manages item state changes at specific locations and timestamps, using a hybrid in-memory dictionary (`item_records`) to store records. It integrates with a `LocationTimeHashBox` to generate unique identifiers for location-time combinations. The system supports storing items, querying by location, time, or both, and retrieving full item histories via a hash key. Data is indexed by both `location_time_hash` and `item_hash` for efficient retrieval.

## Key Functions

### ``execute``

Routes operations (store/query) to appropriate internal methods based on input data.

### ``_store_item``

Validates input, generates hashes if needed, and appends item records to `item_records` under both `location_time_hash` and `item_hash` keys.

### ``_query_by_location``

Retrieves all items associated with a given `location_seed` by iterating through `item_records`.

### ``_query_by_time``

Filters items by `time_period` (simplified; full implementation may require parsing time ranges).

### ``_query_by_location_time``

Combines location and time filters for precise lookups.

### ``_get_item_history``

Returns all records for a given `item_hash` in chronological order.

## Usage

1. **Store an item**:
   ```python
   input_data = {
       "operation": "store",
       "item_hash": "abc123",
       "item_name": "ExampleItem",
       "item_state": {"value": 100},
       "location_seed": "room1",
       "time_period": "2023-01-01T00:00:00"
   }
   result = box.execute(input_data)
   ```
2. **Query by location**:
   ```python
   input_data = {"operation": "query_by_location", "location_seed": "room1"}
   result = box.execute(input_data)
   ```
3. **Retrieve history**:
   ```python
   input_data = {"operation": "get_item_history", "item_hash": "abc123"}
   result = box.execute(input_data)
   ```

## Dependencies

> ``..core.box_interface``
> ``.location_time_hash``
> ``logging``
> ``datetime``

## Related

- [[`LocationTimeHashBox`]]
- [[`Box` class in `core]]

>[!INFO] Indexing Strategy
> Records are stored under **two keys** in `item_records`:
> - `location_time_hash`: For fast location/time-based lookups.
> - `item_hash`: For retrieving full history of an item.
> This ensures both granular and broad queries work efficiently.


>[!WARNING] In-Memory Limitation
> Data is stored in-memory only. For persistence, replace `self.item_records` with a database (e.g., SQLite, Redis) or serialization (e.g., JSON/Pickle).
