**Tags:** #javascript, #web-viewer, #layout-mode, #osm-integration, #plotly, #bugfix
**Created:** 2026-01-12
**Type:** code-notes

# app-data.js

## Summary

```
Fixes incorrect toggle behavior of OSM and Quad View buttons in a web-based simulation viewer.
```

## Details

> The bug occurred in `simulation/frontend/app-data.js` where the `onLayoutModeChange` method improperly enforced OSM view visibility based on both the mode and OSM state. The original logic allowed OSM views to persist even when switching to "Quad View" if OSM was previously enabled. The fix refines the logic to ensure OSM views only appear when explicitly selected (`mode === 'osm'`), while non-OSM modes (e.g., Quad View) disable OSM views regardless of prior state.

## Key Functions

### `onLayoutModeChange(mode)`

Handles state transitions between layout modes (OSM, Quad, 3D-only, 2D-only) and manages OSM view visibility.

### `onToggleOSMView()`

Toggles the OSM view state (enabled/disabled) asynchronously.

## Usage

To apply this fix:
1. Locate `simulation/frontend/app-data.js`.
2. Replace the conditional logic in `onLayoutModeChange` with the corrected version (removing redundant OSM checks).
3. Ensure `onToggleOSMView()` is implemented to handle OSM view state transitions.

## Dependencies

> `- `window.osmIntegrationBox` (external OSM integration component)
- Plotly.js (for rendering non-OSM views)
- Cesium/OSM libraries (for rendering OSM views)`

## Related

- [[app-data]]
- [[layout-mode-button-fix_original_issue]]

>[!INFO] Critical Logic Change
> The fix removes the incorrect `this.osmViewEnabled` check from the conditional, ensuring OSM views only render when `mode === 'osm'`. Non-OSM modes (e.g., Quad View) now force Plotly views by disabling OSM views explicitly.

>[!WARNING] Asynchronous Behavior
> `onToggleOSMView()` is called asynchronously. Ensure thread-safe updates to UI/rendering systems when toggling OSM views.
