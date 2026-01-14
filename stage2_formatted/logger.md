**Tags:** #logging, #utility-class, #production-safe, #console-replacement, #error-handling
**Created:** 2026-01-13
**Type:** code-library

# logger

## Summary

```
A production-safe logger utility that replaces `console.log`/`console.error` with memory-based logging in non-development environments.
```

## Details

> This `Logger` class provides a controlled logging mechanism that:
> 1. **Lazy-loads** environment checks (development mode) to avoid initialization order issues.
> 2. **Replaces** `console` methods with in-memory storage, ensuring no leaks in production.
> 3. **Sanitizes** error objects to extract meaningful messages (e.g., `Error.message` or `error.toString()`).
> 4. **Limits logs** to 100 entries to prevent memory bloat.
> 5. Supports filtering/log retrieval via `getLogs(level, limit)` and `clear()`.

## Key Functions

### ``Logger()``

Constructor initializes in-memory logs and lazy-loaded dev-mode detection.

### ``isDevelopment``

Lazy property checks if the app runs in development (via config or `window.location` fallback).

### ``_checkDevelopment()``

Determines dev mode by inspecting `config.isDevelopment()` or hostname.

### ``_addLog(level, message, data)``

Core method appends logs to `this.logs` (truncates if >100 entries) and conditionally logs to console.

### ``info(message, data)``

Logs an informational message.

### ``warn(message, data)``

Logs a warning.

### ``error(message, error)``

Logs an error with sanitized error details (e.g., `Error.message` or `error.toString()`).

### ``debug(message, data)``

Conditionally logs debug info (only in dev mode).

### ``getLogs(level, limit)``

Returns recent logs (optionally filtered by `level` and limited to `limit` entries).

### ``clear()``

Empties the in-memory log buffer.

## Usage

1. **Import** the logger:
   ```js
   import { Logger, logger } from './logger';
   ```
2. **Use methods**:
   ```js
   logger.info("App started");
   logger.warn("Disk space low", { disk: 10 });
   logger.error("Failed to load user", new Error("Network timeout"));
   ```
3. **Retrieve logs**:
   ```js
   const recentErrors = logger.getLogs("error", 5);
   ```

## Dependencies

> ``../services/config.js` (optional config for dev mode detection).`

## Related

- [[Logger Usage Guide]]
- [[Production Logging Best Practices]]

>[!INFO] Lazy Dev-Mode Check
> Avoids circular dependencies by deferring `isDevelopment` until first access. Falls back to `window.location` if `config` is unavailable.

>[!WARNING] Memory Limits
> Logs older than 100 entries are discarded. For critical logs, consider external storage (e.g., file/database).
