**Tags:** #in-memory-cache, #hash-based-keying, #terrain-generation, #LRU-eviction
**Created:** 2026-01-13
**Type:** code-notes

# terrain_cache_box

## Summary

```
Implements an in-memory cache for terrain generation results to optimize performance by avoiding redundant computations.
```

## Details

> This `TerrainCacheBox` class uses a dictionary-based cache (`self._cache`) to store terrain data with SHA-256 hashed composite keys derived from `world_hash`, `world_type`, `width`, and `height`. The cache enforces a maximum size of 100 entries, employing a simple **Least Recently Used (LRU)** eviction policy by removing the oldest entry when the cache exceeds capacity. The system supports three operations: `"get"` (retrieves cached terrain), `"set"` (stores new terrain data), and `"clear"` (empties the cache entirely). Logging tracks cache hits/misses for debugging.

## Key Functions

### ``execute``

Dispatches operations (`get`, `set`, `clear`) based on input data.

### ``_get_cache_key``

Generates a SHA-256 hash from terrain parameters to create a unique cache key.

### ``_get``

Retrieves cached terrain data if the key exists; otherwise, returns `None`.

### ``_set``

Stores terrain data in cache, evicting the oldest entry if the cache is full.

### ``_clear``

Empties the cache and logs the number of cleared entries.

## Usage

1. Initialize `TerrainCacheBox` and call `execute` with a `BoxInput` containing:
   - `"operation"`: `"get"`, `"set"`, or `"clear"`.
   - For `"get"`: Include `world_hash`, `world_type`, `width`, `height`.
   - For `"set"`: Include `terrain` data (required).
2. Example:
   ```python
   cache = TerrainCacheBox()
   input_data = {"operation": "get", "world_hash": "123", "width": 128, "height": 128}
   result = cache.execute(input_data)
   ```

## Dependencies

> ``hashlib``
> ``logging``
> ``typing``
> ``..core.box_interface` (Box`
> `BoxInput`
> `BoxOutput)`

## Related

- [[`core]]
- [[`hashlib` documentation]]
- [[`typing` module for type hints]]

>[!INFO] Key Generation
> The cache key is derived from `world_hash`, `world_type`, `width`, and `height` via SHA-256, ensuring uniqueness for identical terrain configurations.

>[!WARNING] LRU Limitation
> LRU eviction assumes FIFO order; if terrain data is frequently accessed in non-sequential patterns, cache performance may degrade. Consider a more sophisticated eviction policy (e.g., LRU with timestamps) for critical applications.
