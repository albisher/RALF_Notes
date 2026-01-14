**Tags:** #http-methods, #api-integration, #backend-frontend-mismatch, #data-formatting, #time-system-management
**Created:** 2026-01-14
**Type:** code-fix

# time-system-fixes-20251121

## Summary

```
Fixes time system save errors by correcting HTTP method, request body structure, and key naming conventions between frontend and backend APIs.
```

## Details

> This file documents fixes for time system save failures caused by mismatched HTTP methods, incorrect request body formatting, and inconsistent key naming conventions (camelCase vs snake_case) between the frontend (`ui-beta`) and backend APIs. The fixes ensure proper data flow from frontend modifications to backend persistence, resolving HTTP 405 errors and enabling correct time system calculations.

## Key Functions

### ``updateTimeSystem` (worlds_api_box.js)`

Handles HTTP POST request with corrected body structure and key conversion.

### ``handleWorldChanged` (WorkflowPage.vue)`

Loads and converts backend snake_case time system data to frontend camelCase for display.

### `Backend `/api/worlds/<int`

world_id>/time-system` (app.py)**: Processes POST requests for time system updates, validating and storing data in snake_case format.

## Usage

1. **Save Time System**: Modify settings in the Time System tab, then click "Save." The frontend now sends a properly formatted POST request with the correct method and data structure.
2. **Load Time System**: After refreshing, the frontend converts backend snake_case data to camelCase for user-friendly display.

## Dependencies

> ``axios` (or similar HTTP client)`
> ``json` parsing libraries`
> `backend Flask route handler (`app.py`)`
> ``World` model class.`

## Related

- [[backend-api-documentation]]
- [[time-system-specification]]

>[!INFO] Critical Fix
> The HTTP method change from PUT to POST resolves the 405 error by aligning with the backend’s expected method. This prevents silent failures during saves.

>[!WARNING] Backward Compatibility Risk
> The key naming conversion (snake_case ↔ camelCase) ensures backward compatibility but requires careful testing if existing frontend state relies on either format. Default values should handle missing keys gracefully.
