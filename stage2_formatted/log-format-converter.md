**Tags:** #logging, #data-transformation, #backend-frontend, #format-conversion, #timestamp-handling, #utilities
**Created:** 2026-01-13
**Type:** code-notes

# log-format-converter

## Summary

```
Converts logs between LoggingBox backend format and frontend communicationLog format for seamless integration.
```

## Details

> This utility handles bidirectional conversion between two log formats: the backend’s `LoggingBox` format and the frontend’s `communicationLog` format. It ensures timestamp normalization (ISO format) and preserves key fields like `from`, `to`, `type`, `message`, and `level` while maintaining backward compatibility. The converter also extracts nested `data` fields for compatibility.

## Key Functions

### ``loggingBoxToFrontend(logEntry)``

Converts a `LoggingBox` log entry into frontend-compatible format, adding ISO timestamps and restructuring fields.

### ``frontendToLoggingBox(frontendLog)``

Extracts core log details (e.g., `message`, `level`) from frontend logs, defaulting to fallback values if missing.

## Usage

1. Call `loggingBoxToFrontend(logEntry)` to transform backend logs into frontend format.
2. Call `frontendToLoggingBox(frontendLog)` to adapt frontend logs for backend processing.
3. Handle edge cases (e.g., missing fields) gracefully via fallbacks.

## Dependencies

> ``Date` (built-in JS)`
> `no external libraries.`

## Related

- [[none]]

>[!INFO] Timestamp Handling
> The converter normalizes timestamps to ISO format, converting Unix timestamps (seconds/milliseconds) to milliseconds-based `timestamp_ms` for compatibility.

>[!WARNING] Fallback Logic
> If `timestamp` is invalid, it defaults to the current time. Ensure backend logs include valid timestamps to avoid unexpected behavior.
