**Tags:** #duplicate-log-fix, #logging-system, #frontend-improvement, #socketio, #duplicate-detection
**Created:** 2026-01-13
**Type:** code-notes

# duplicate-logs-fix

## Summary

```
Fixes duplicate logs in the System Monitoring page by enhancing duplicate detection and message handling across multiple frontend components.
```

## Details

> This fix addresses multiple issues causing duplicate logs in the frontend system monitoring page. The solution involves adding robust duplicate detection logic across several files (`logging-box.js`, `app-data.js`, `log-format-converter.js`, and `system-monitoring-page-component.js`). The core improvements include:
> - Ensuring logs are checked for duplicates before insertion into `communicationLog`.
> - Including message content in duplicate detection keys to prevent false positives.
> - Standardizing log message display by adding the `message` field at the top level.
> - Updating log ID generation to use `timestamp` instead of `sim_time` for reliability.

## Key Functions

### ``_logToUI()` (simulation/frontend/boxes/logging-box.js)`

Added duplicate checking before log insertion, ensuring logs include a `log.id` and `message` at the top level.

### ``log-update` and `communication-log-update` listeners (simulation/frontend/app-data.js)`

Enhanced duplicate detection to include `message` and switch from `sim_time` to `timestamp` for uniqueness.

### ``generateLogId()` (simulation/frontend/utils/log-format-converter.js)`

Modified to generate IDs using `timestamp` and `message` for consistency.

### `Duplicate detection logic (simulation/frontend/pages/system-monitoring-page-component.js)`

Improved hashing to include message content from nested log structures.

## Usage

To apply this fix, ensure the following files are updated as described:
1. Update `_logToUI()` in `logging-box.js` to include duplicate checks and message fields.
2. Modify Socket.IO listeners in `app-data.js` to use `timestamp` and include `message` in duplicate keys.
3. Update `log-format-converter.js` to include `message` and `level` at the top level of log objects.
4. Adjust duplicate detection in `system-monitoring-page-component.js` to handle nested messages.

## Dependencies

> ``simulation/frontend/boxes/logging-box.js``
> ``simulation/frontend/app-data.js``
> ``simulation/frontend/utils/log-format-converter.js``
> ``simulation/frontend/pages/system-monitoring-page-component.js``
> `Socket.IO library.`

## Related

- [[logging-box]]
- [[app-data]]
- [[log-format-converter]]
- [[system-monitoring-page-component]]

>[!INFO] Important Note
> The fix ensures logs are now uniquely identified by combining `from`, `to`, `timestamp`, `type`, and `message` in the duplicate detection key. This prevents false duplicates caused by similar but distinct log entries.

>[!WARNING] Caution
> Ensure backward compatibility is tested after applying these changes, as modifying log structure (e.g., adding `message` at the top level) may affect existing frontend logic that relies on the old structure.
