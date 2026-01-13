**Tags:** #logging, #sidebar, #debugging, #frontend, #phase-filtering, #data-limits, #fixes
**Created:** 2026-01-13
**Type:** code-notes

# disappearing-logs-fix

## Summary

```
Fixes disappearing logs in the right sidebar by adjusting phase filtering, log limits, and default visibility settings.
```

## Details

> This fix addresses a bug where logs vanished from the right sidebar due to overly aggressive phase-based filtering, inconsistent log limits, and default filtering enabled. The solution involves modifying three key files to ensure logs persist by:
> 1. Reducing phase filtering restrictions (e.g., increasing buffer from 10 to 100 logs).
> 2. Disabling phase filtering by default while allowing manual toggling.
> 3. Standardizing log limits across systems (from 200 to 1000 entries) to prevent truncation inconsistencies.

## Key Functions

### ``logging-phase-system.js``

Updated `isLogRelevant()` to include all INFO-level logs, COMMUNICATION_* types, and command/position_update logs; increased buffer to 100 logs.

### ``app-data.js``

Set `disablePhaseFiltering: true` to show all logs by default.

### ``logging-box.js``

Adjusted log limit to 1000 entries and changed removal logic to `slice(0, 1000)` for consistency.

## Usage

After applying these changes, logs should now persist in the sidebar by default. Users can still enable phase filtering manually if needed. Test thoroughly to confirm logs do not disappear unexpectedly and limits (1000 entries) are respected.

## Dependencies

> ``simulation/frontend/utils/logging-phase-system.js``
> ``simulation/frontend/app-data.js``
> ``simulation/frontend/boxes/logging-box.js``

## Related

- [[universal-iso-timestamp-implementation]]

>[!INFO] Important Note
> Phase filtering is now disabled by default, ensuring all logs appear unless explicitly toggled. Critical logs (INFO, COMMUNICATION_*, errors) remain visible even with phase filtering enabled.

>[!WARNING] Caution
> Overly aggressive filtering could still cause issues if not thoroughly tested. Ensure no edge cases (e.g., log overflow) remain after adjustments.
