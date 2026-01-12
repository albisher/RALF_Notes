**Tags:** #reactivity, #ui-updates, #vue, #spawn-logic, #socket-io, #data-sync
**Created:** 2026-01-12
**Type:** code-notes

# api-methods.js

## Summary

```
Fixes UI lag during drone spawning by ensuring real-time updates via visualization data refresh and Vue reactivity.
```

## Details

> The `spawnDrone()` function in `api-methods.js` was modified to:
> 1. Call `fetchVisualizationData()` to update visualization data immediately after spawning a drone.
> 2. Use `$nextTick` with `$forceUpdate()` to enforce Vue reactivity, ensuring UI components like dropdowns and legends reflect changes instantly.
> This prevents stale UI states by syncing drone data with visualizations and forcing a refresh of dependent components.

## Key Functions

### ``spawnDrone()``

Core drone spawning logic with forced UI updates.

### ``fetchVisualizationData()``

Updates visualization data to match the drones array.

### ``$nextTick(() => { this.$forceUpdate() })``

Forces Vue reactivity to propagate UI changes.

## Usage

Call `spawnDrone()` to spawn a drone, which now triggers automatic UI updates via `fetchVisualizationData()` and reactivity hooks.

## Dependencies

> `Vue.js (for reactivity)`
> `Socket.IO (for real-time drone updates)`
> ``app-data.js` (shared visualization logic).`

## Related

- [[app]]
- [[app-layout5]]
- [[app-data]]
- [[nav-sidebar-component]]

>[!INFO] Important Note
> The `$forceUpdate()` call bypasses Vue’s default reactivity checks, which may cause temporary UI inconsistencies if not paired with proper state management. Ensure `fetchVisualizationData()` updates data atomically before forcing updates.


>[!WARNING] Caution
> Overusing `$forceUpdate()` can degrade performance in complex UIs. This fix is targeted to minimize such cases by syncing data first and then refreshing only necessary components.
