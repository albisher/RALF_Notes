**Tags:** #frontend, #logging, #time-travel, #sorting, #simulation, #reverse-order, #computed-property, #data-processing
**Created:** 2026-01-12
**Type:** code-notes

# app-data.js

## Summary

```
Modifies log ordering in a frontend application to display latest logs first in normal mode, preserving chronological order in time-travel replay mode.
```

## Details

> This implementation dynamically adjusts the order of logs in a sidebar based on the application's mode. When in **normal mode**, logs are sorted by `sim_time` in descending order (latest first), ensuring users can quickly view recent activity. In **time-travel mode**, logs revert to chronological order (oldest first) to maintain proper replay sequence. The change is encapsulated in a computed property (`filteredLogs`) that filters and sorts logs conditionally, ensuring backward compatibility with existing functionality.

## Key Functions

### ``filteredLogs()``

Computed property that returns filtered and sorted logs based on mode.

### ``sim_time``

Log entry timestamp field used for sorting.

### ``timeTravelMode``

Application state flag determining sorting logic.

## Usage

1. **Normal Mode**: Logs appear in reverse chronological order (latest at top).
2. **Time Travel Mode**: Logs appear in chronological order (oldest at top) after filtering by `currentTime`.
   - Requires `timeTravelMode` and `currentTime` to be set.

## Dependencies

> ``communicationLog` (internal data store)`
> ``currentTime` (time-travel reference)`
> ``timeTravelMode` (mode flag).`

## Related

- [[frontend (core frontend module)]]
- [[time-travel-mode-implementation (related time-travel logic).]]

>[!INFO] Conditional Sorting Logic
> The function dynamically switches between ascending and descending sort based on `timeTravelMode`. This ensures correct behavior for both live monitoring and replay scenarios.

>[!WARNING] Edge Case Handling
> Fallback (`|| 0`) for missing `sim_time` prevents runtime errors when sorting. Ensure all logs have a valid `sim_time` for accurate results.
