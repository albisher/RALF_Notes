**Tags:** #ui-improvement, #logging-system, #notification-management, #user-experience, #system-monitoring
**Created:** 2026-01-13
**Type:** documentation

# reduced-notifications-proper-logging

## Summary

```
Document outlining a redesign to reduce UI clutter by minimizing notifications for routine operations while ensuring critical events remain visible and all actions are properly logged.
```

## Details

> This document details a solution to address excessive notifications cluttering the UI, replacing them with targeted logging in dedicated log panels. The approach involves reducing notification frequency for routine operations (e.g., weather updates, building loads) while retaining longer notifications for critical events (e.g., errors, warnings). All logged events are categorized, searchable, and exportable, ensuring a complete audit trail.

## Key Functions

### ``simulation/frontend/methods/ui-methods.js``

Adjusts notification durations (5000ms → 3000ms for routine, 7000ms for critical).

### ``simulation/frontend/app-data.js``

Removes notifications for routine operations (weather, buildings, settings) while preserving user actions, errors, and warnings.

### `Log Panels`

Categorizes events (e.g., weather_operation, building_operation) for filtering and searchability.

## Usage

1. Apply duration adjustments in `ui-methods.js` for routine vs. critical events.
2. Remove routine notifications in `app-data.js` and log them to dedicated panels.
3. Ensure all logged events include metadata (e.g., coordinates, timestamps) for context.

## Dependencies

> `Obsidian: Frontend UI components (e.g.`
> `notification system`
> `log panel integration)`
> `backend data sources (e.g.`
> `weather API`
> `map data).`

## Related

- [[ui-components]]
- [[logging-system]]

>[!INFO] Important Note
> Routine operations (e.g., weather fetch) are now logged to the **System Logs** panel instead of triggering UI notifications, improving UI clarity.

>[!WARNING] Caution
> Critical events (e.g., errors) still show notifications (7s) to maintain user awareness—do not alter this behavior.
