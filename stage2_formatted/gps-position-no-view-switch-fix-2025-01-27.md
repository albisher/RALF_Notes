**Tags:** #javascript, #gps-integration, #map-view-switching, #osm, #preset-selection, #view-control
**Created:** 2026-01-12
**Type:** code-notes

# simulation/frontend/components/header-component.js

## Summary

```
Fixes automatic OSM view switching when selecting GPS positions, ensuring GPS info displays in the current view.
```

## Details

> The fix removes hardcoded logic that forced the map to switch to OSM when GPS positions were selected. Instead, it ensures GPS coordinates update the currently active view (Plotly or OSM) without altering the user’s selection. Key changes include removing forced map source changes, disabling automatic OSM view triggers, and updating only when OSM is already enabled.

## Key Functions

### ``this.masterControls.mapSource``

Controls the active map source (OSM/Plotly/Google).

### ``this.$emit('enable-osm-view-for-preset')``

Previously emitted an event to auto-enable OSM; now removed.

### ``onToggleOSMView()``

Logic for enabling/disabling OSM view; now only runs if explicitly triggered.

### ``window.osmIntegrationBox``

Conditional update for OSM views when already enabled.

## Usage

After applying fixes, users can select GPS positions (presets/custom/random) without the system auto-switching to OSM. The GPS info updates in the current view (e.g., Plotly remains Plotly, OSM remains OSM).

## Dependencies

> ``simulation/frontend/app-data.js``
> ``simulation/frontend` (frontend components)`
> ``osmIntegrationBox` (external OSM integration module).`

## Related

- [[app-data]]
- [[preset-selection]]

>[!INFO] Critical Logic Change
> The fix ensures **no forced map source updates** occur during GPS selection. Always check `this.masterControls.mapSource` before updating OSM views to avoid unintended view switches.

>[!WARNING] Backward Compatibility Risk
> If OSM integration relies on auto-enabled views, users may need manual OSM activation after GPS updates. Test edge cases where OSM is disabled but GPS coordinates are valid.
