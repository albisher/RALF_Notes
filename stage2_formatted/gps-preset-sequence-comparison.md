**Tags:** #gps-preset, #sequence-analysis, #backend-api, #frontend-flow, #async-await, #event-emission
**Created:** 2026-01-12
**Type:** code-notes

# 

## Summary

```
Compares GPS preset selection workflows for "Random," "Home," and "PAAET" presets, highlighting backend API interactions, state updates, and asynchronous operations.
```

## Details

> This document contrasts the execution flow of selecting random vs. predefined ("Home" or "PAAET") GPS presets in a logging sidebar component. The **Random** preset triggers a backend API call (`GET /api/prepare?force_random=true`) to generate coordinates dynamically, while predefined presets use hardcoded values from a local `gpsPresets` object. Key differences include:
> - Random presets set `is_random = true` in state and await backend responses for map/weather updates.
> - Predefined presets skip the backend API but lack proper async handling for `updateGpsPosition()`, risking timing inconsistencies.

## Key Functions

### ``onGpsPresetChange()``

Core logic in `logs-sidebar-component.js` (lines 742–830) handling preset selection.

### ``updateGpsPosition()``

Emits events to load map data (buildings/OSM tiles) but is non-awaited for predefined presets.

### ``updateOSMMiniMap()``

Awaited for both flows to update mini-map crosshair.

### ``fetch-weather-from-gps``

Emitted after all GPS updates complete.

## Usage

1. **Random Preset**: Trigger `onGpsPresetChange()` with `force_random=true` to fetch dynamic coordinates.
2. **Predefined Preset**: Select "Home" or "PAAET" from UI, relying on local `gpsPresets` object.
3. **Critical Timing**: Ensure `updateGpsPosition()` is awaited for seamless map updates (issue noted for predefined presets).

## Dependencies

> `- `app-data.js` (event handlers for `update-gps-position` and `mini-map-loaded`).
- Backend API (`/api/prepare` endpoint for random presets).
- OSM tile service (for mini-map updates).`

## Related

- [[gps-preset-objects]]
- [[backend-api-docs]]
- [[event-emission-handlers]]

>[!INFO] **Random Flow Strengths**
> Backend-generated coordinates ensure consistency across sessions, while `is_random` flag aids UI differentiation.

>[!WARNING] **Predefined Flow Risk**
> Non-awaited `updateGpsPosition()` may cause lag or misaligned map updates, especially with OSM building loads. Fix by wrapping in `await`.
