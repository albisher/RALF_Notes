**Tags:** #Caching, #In-Memory, #PersistentStorage, #TTL, #LocalStorage, #SessionStorage, #OOP, #ReusableComponent
**Created:** 2026-01-13
**Type:** code-notes

# CacheBox

## Summary

```
A reusable, class-based caching system supporting memory, localStorage, or sessionStorage with configurable TTL and size limits.
```

## Details

> `CacheBox` implements a generic caching layer with a single responsibility: managing in-memory and persistent cache entries with configurable time-to-live (TTL) expiration. The class supports three storage backends (`memory`, `localStorage`, `sessionStorage`) and enforces optional size limits. It tracks cache statistics (hits/misses/sets/evictions) via a `stats` object. The implementation uses a hybrid approach: in-memory cache for fast access, falling back to persistent storage for larger datasets. Expired entries are automatically removed, and keys are prefixed for namespace isolation.

## Key Functions

### `constructor(config)`

Initializes the cache with default/overridden settings (TTL, storage type, prefix, max size).

### `get(key)`

Retrieves a cached value, checking memory first, then persistent storage. Returns `null` if expired/missing.

### `_getStorage()`

Private helper to dynamically select storage backend based on `storageType`.

### `_makeKey(key)`

Private helper to construct storage keys with a configurable prefix.

### `_isExpired(entry)`

Private helper to validate TTL expiration for cached entries.

## Usage

```javascript
const cache = new CacheBox({
    defaultTTL: 300000, // 5 minutes
    storageType: 'localStorage',
    prefix: 'myapp_',
    maxSize: 50
});

// Set a value with TTL
cache.set('user_prefs', { theme: 'dark' }, 10000); // Expires in 10s

// Retrieve a value
const prefs = cache.get('user_prefs'); // Returns cached object or null if expired
```

## Dependencies

> ``localStorage``
> ``sessionStorage` (browser APIs)`
> ``JSON.parse`/`JSON.stringify` (built-in).`

## Related

- [[CacheBox Usage Examples]]
- [[CacheBox API Reference]]

>[!INFO] Default TTL
> By default, `defaultTTL` is set to **5 minutes (300,000ms)**. Override this in `config` for project-specific needs.

>[!WARNING] LocalStorage Limitation
> `localStorage` has a **5MB limit per domain**. If `maxSize` is exceeded, older entries may be evicted silently. Monitor `stats.evictions` for warnings.
