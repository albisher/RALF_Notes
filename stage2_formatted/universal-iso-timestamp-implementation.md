**Tags:** #timestamp, #iso-8601, #utc, #backend-frontend, #timezone, #logging, #simulation
**Created:** 2026-01-13
**Type:** code-notes

# universal-iso-timestamp-implementation

## Summary

```
Standardizes timestamp logging across backend and frontend to use UTC-based ISO 8601 format for consistency and interoperability.
```

## Details

> This implementation refactors timestamp generation in a simulation system to enforce UTC-based ISO 8601 format across all components. Previously, timestamps were displayed in `HH:MM:SS.mmm` format with local timezone offsets, causing inconsistencies. The solution ensures all timestamps include timezone information (`+00:00`) and adhere to ISO 8601 standards, improving reliability and compatibility with external systems.

## Key Functions

### ``datetime.now(timezone.utc).isoformat()``

Generates UTC-based ISO timestamps in backend components.

### ``formatLogTime()` (frontend)`

Converts local timestamps to ISO format for display, preserving timezone awareness.

### ``toISOString()` (frontend logging)`

Ensures logs are rendered in full ISO 8601 format.

## Usage

1. **Backend**: Replace all `datetime.now()` calls with `datetime.now(timezone.utc)` to enforce UTC timestamps.
2. **Frontend**: Use `formatLogTime()` to conditionally return ISO timestamps, ensuring consistency with backend output.
3. **Logging**: All logs now include timezone indicators (e.g., `+00:00`), making them universally interpretable.

## Dependencies

> ``pytz``
> ``datetime``
> ``timezone` (Python standard library)`
> ``js-date` (frontend libraries for timestamp handling).`

## Related

- [[logging_box]]
- [[logs-sidebar-component]]
- [[system-monitoring-page-component]]

>[!INFO] Important Note
> UTC timestamps ensure global consistency, avoiding ambiguity from local timezones. Always use `timezone.utc` for backend operations.

>[!WARNING] Caution
> Overlooking timezone handling may lead to misaligned logs or parsing errors in external systems. Test edge cases (e.g., DST transitions) to validate ISO format compliance.
