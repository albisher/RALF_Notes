**Tags:** #Storage-API, #Abstraction-Layer, #LocalStorage, #SessionStorage, #Cookies, #OOP, #Serialization
**Created:** 2026-01-13
**Type:** code-notes

# StorageBox

## Summary

```
Unified storage abstraction layer for localStorage, sessionStorage, and cookies with configurable serialization and versioning.
```

## Details

> `StorageBox` is a class-based abstraction that provides a consistent interface for managing data across different storage backends (localStorage, sessionStorage, or cookies). It supports customizable serialization/deserialization via provided functions, versioning for schema compatibility, and optional encryption. The class first checks storage availability before proceeding, ensuring graceful degradation if a backend fails. Data keys are prefixed for namespace isolation, and the system handles key-value operations (set/get/remove/clear) uniformly.

## Key Functions

### `constructor(config)`

Initializes the storage box with type, prefix, version, and serialization functions.

### `_checkAvailability()`

Tests if the selected storage backend is accessible via a temporary key.

### `_getStorage()`

Dynamically selects the appropriate storage backend (local/session/cookie).

### `_getCookieStorage()`

Implements cookie-specific storage methods (set/get/remove).

### `setItem(key, value)`

Serializes and stores a key-value pair in the selected storage.

### `getItem(key)`

Retrieves and deserializes a value by key.

### `removeItem(key)`

Clears a specific key-value pair.

### `clear()`

Empties the entire storage backend.

## Usage

```javascript
// Basic usage (localStorage)
const box = new StorageBox({ type: 'local', prefix: 'user_' });
box.setItem('prefs', { theme: 'dark' });
const data = box.getItem('prefs');

// Cookie usage
const cookieBox = new StorageBox({ type: 'cookie', prefix: 'auth_' });
cookieBox.setItem('token', 'abc123');
```

## Dependencies

> ``localStorage``
> ``sessionStorage``
> ``document.cookie` (browser APIs)`
> `no external libraries.`

## Related

- [[StorageAbstractionPatterns]]
- [[BrowserStorageAPIs]]

>[!INFO] Storage Backend Selection
> The class automatically falls back to `localStorage` if `sessionStorage` or cookies are unavailable, ensuring compatibility across browsers.

>[!WARNING] Cookie Limits
> Cookies are limited to ~4KB per cookie and ~4096 cookies per domain. Prefixing keys helps mitigate collisions.
