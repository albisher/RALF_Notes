**Tags:** #Vue, #Vuex, #RouteHandling, #FrontendFix, #EventListeners, #BackendCompatibility
**Created:** 2026-01-12
**Type:** code-notes

# system-monitoring-route-change-fix-2025-01-27

## Summary

```
Fixes route change event handling for the system monitoring page to ensure proper data synchronization.
```

## Details

> This fix addresses issues where the `/sm/` monitoring page failed to update correctly due to mismatched event details between `SystemMonitoringBox` and `URLRoutingBox`. The root causes were:
> 1. Event detail inconsistency (`viewId` vs `view`).
> 2. Attempting to modify a prop (`currentView`) instead of using Vuex state.
> 
> The solution involved:
> - Updating the `SystemMonitoringBox` to handle both `viewId` and `view` for backward compatibility.
> - Removing incorrect prop assignment in `SystemMonitoringPageComponent` to avoid Vue errors.

## Key Functions

### ``SystemMonitoringBox``

Listens to route-change events and updates `monitoringState.currentView` with either `viewId` or `view`.

### ``URLRoutingBox``

Emits route-change events with `event.detail.viewId` (new) or `event.detail.view` (legacy).

### ``SystemMonitoringPageComponent``

Uses `currentView` as a prop (previously incorrectly modified as a data property).

## Usage

1. Navigate to `/sm/` or trigger a route change via the sidebar.
2. The monitoring page should now display correctly with updated data.
3. Verify via console logs or manual inspection of `monitoringState.currentView`.

## Dependencies

> `Vue.js`
> `Vuex`
> ``simulation/frontend/boxes/url-routing-box.js``
> ``simulation/frontend/app.js``

## Related

- [[system-monitoring-box]]
- [[system-monitoring-page-component]]
- [[url-routing-box]]
- [[app]]

>[!INFO] Event Compatibility
> The fix supports both `viewId` (new) and `view` (legacy) to maintain backward compatibility without breaking existing functionality.

>[!WARNING] Prop vs Data Property
> Avoid modifying props directly in Vue components. Use Vuex state or props for state management instead.
