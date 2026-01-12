**Tags:** #plotly, #3d-visualization, #quad-view, #sync-fix, #hard-refresh, #javascript, #async-await
**Created:** 2026-01-12
**Type:** code-notes

# sim/prepareScene

## Summary

```
Fixed quad-view hard refresh issues by ensuring Plotly plots initialize and update synchronously across all four views.
```

## Details

> The `prepareScene()` method was modified to conditionally enable OSM (OpenStreetMap) views based on layout mode. Previously, it unconditionally set `osmViewEnabled = true`, which caused 2D Top and 3D Isometric plots to fail initialization during hard refresh because `initializePlots()` checked `!this.osmViewEnabled` before proceeding. The fix ensures OSM is disabled in quad view, allowing all Plotly plots to initialize properly.

## Key Functions

### `prepareScene()`

Adjusts `osmViewEnabled` based on layout mode to prevent OSM interference in quad view.

### `initializePlots()`

Now initializes all four Plotly plots in parallel for quad view using `Promise.all()` to maintain synchronization.

### `updatePlotsWithData()`

Updates 2D Top and 3D Isometric plots in parallel for quad view to ensure consistent state.

## Usage

To apply this fix:
1. Ensure the layout mode is set to `'quad'` before calling `prepareScene()`.
2. Call `initializePlots()` and `updatePlotsWithData()` after `prepareScene()` to ensure all plots initialize and update synchronously.

## Dependencies

> ``Promise.all``
> ``async/await` (built-in JavaScript features)`
> `Plotly.js library (for rendering plots).`

## Related

- [[initializePlots]]
- [[updatePlotsWithData]]

>[!INFO] Important Note
> The fix ensures that `osmViewEnabled` is explicitly set to `false` in quad view, preventing OSM from interfering with Plotly plot initialization.

>[!WARNING] Caution
> Ensure `initializePlots()` and `updatePlotsWithData()` are called after `prepareScene()` to avoid partial initialization or out-of-sync updates.
