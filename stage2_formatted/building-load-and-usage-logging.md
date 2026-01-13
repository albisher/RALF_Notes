**Tags:** #logging, #backend-api, #data-tracking, #frontend-development, #debugging, #api-integration, #simulation-system
**Created:** 2026-01-13
**Type:** code-notes

# building-load-and-usage-logging

## Summary

```
Documentation outlining the implementation of comprehensive building load and usage logging for tracking backend API interactions and frontend visualization operations.
```

## Details

> This document describes the addition of detailed logging for building operations in a simulation frontend system. The solution addresses missing logs during page reloads by tracking three key phases: loading buildings from the backend API (`/api/buildings/list`), receiving buildings in visualization data (`/api/data`), and displaying buildings in plots. Logs include metadata like building counts, types, and simulation timestamps, ensuring full lifecycle visibility. The implementation spans `simulation/frontend/methods/api-methods.js` and `simulation/frontend/app-data.js`.

## Key Functions

### `refreshBuildings()`

Logs buildings loaded from `/api/buildings/list` with count and first 10 names.

### `fetchVisualizationData()`

Logs buildings received in visualization data with type breakdown and simulation time.

### `updatePlotsWithData()`

Logs buildings displayed in plots, excluding OSM hints, with filtered counts and layout mode.

## Usage

To use this logging:
1. Trigger the functions (`refreshBuildings`, `fetchVisualizationData`, `updatePlotsWithData`) during building lifecycle events.
2. Check logs in the **System Logs Panel** (System Monitoring Page) with filter `type: 'building_operation'`.

## Dependencies

> ``simulation/frontend/methods/api-methods.js``
> ``simulation/frontend/app-data.js``
> `backend API endpoints (`/api/buildings/list``
> ``/api/data`).`

## Related

- [[api-methods]]
- [[app-data]]
- [[backend-api-documentation]]

>[!INFO] Important Note
> Logs are structured as JSON objects with `source`, `type`, and `action` fields for easy filtering. Example:
> ```json
> { "source": "app-data.js", "type": "building_operation", "action": "load_buildings", "buildings_count": 42 }
> ```

>[!WARNING] Caution
> Ensure backend API endpoints (`/api/buildings/list`, `/api/data`) are accessible and return valid JSON. Errors during loading will be logged but may not halt execution.
