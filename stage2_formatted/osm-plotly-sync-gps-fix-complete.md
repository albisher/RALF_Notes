**Tags:** #gps-preset, #vue-js, #error-handling, #osm-integration, #fix-debugging, #coordinate-sync
**Created:** 2026-01-12
**Type:** code-fix

# 

## Summary

```
Fixes GPS preset dropdown value mismatch causing Vue.js errors and failed OSM building loading by adding robust error handling for display-text vs. key mismatches.
```

## Details

> The fix addresses a Vue.js dropdown selection issue where selecting presets like "🏠 Home (Kuwait)" failed because the backend expected keys (`"home"`/`"paaet"`) instead of display text. The solution includes:
> 1. **Automatic conversion** of display text to preset keys in `onGpsPresetChange()`.
> 2. **Validation** of preset keys before updating coordinates.
> 3. **Graceful reset** of invalid selections to empty state.

## Key Functions

### ``onGpsPresetChange()``

Handles dropdown selection with error detection and conversion logic.

### ``updatePresetSelection()``

Validates preset keys before applying changes.

### `Vue watcher (attempted)`

Monitors invalid selections and resets them (partial implementation).

## Usage

After applying the fix, users can now select GPS presets (e.g., "Home" or "PAAET") without errors. The system automatically:
1. Converts display text to keys if mismatched.
2. Updates coordinates and triggers OSM loading.
3. Emits events (e.g., `enable-osm-view-for-preset`) for downstream logic.

## Dependencies

> `Vue.js`
> `OSM API`
> `Plotly.js (for map rendering)`
> ``simulation/frontend` module.`

## Related

- [[header-component]]
- [[`osm-map-coordinate-handling`]]

>[!INFO] **Key Logic**
> The fix dynamically checks if `selectedGpsPreset` is a valid key or display text. If display text is provided (e.g., `"🏠 Home (Kuwait)"`), it maps it to the correct key (e.g., `"home"`) before proceeding.

>[!WARNING] **Edge Case Handling**
> If neither a valid key nor display text is found, the preset selection is reset to an empty string, preventing crashes. This ensures robustness for malformed inputs.
