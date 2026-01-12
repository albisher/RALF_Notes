**Tags:** #vuejs, #reactivity, #url-routing, #frontend-fix, #data-fetching, #session-analysis, #ml-learning
**Created:** 2026-01-12
**Type:** code-notes

# simulation/frontend/app.js

## Summary

```
Applies fixes for Vue.js frontend components to ensure proper rendering and data synchronization across navigation routes, particularly for drones control, session analysis, and ML learning data.
```

## Details

> The document details fixes for critical rendering and data synchronization issues in a Vue.js frontend application. The core problem was that components registered via URL routing (`currentView`) failed to render correctly when navigating directly to specific routes (`/dc`, `/sa`, `/ml`) due to unsynchronized reactivity. Fixes involved using `$nextTick()` to ensure `currentView` updates and triggers view-specific initialization (e.g., `loadDroneConfigurations()`, `loadSessions()`, `fetchMLLearningData()`) on initial load or route changes.

## Key Functions

### ``mounted()``

Initializes `currentView` sync with URL routing and triggers view-specific logic.

### ``$nextTick()``

Ensures Vue reactivity updates before rendering.

### ``urlRoutingBox.getCurrentView()``

Extracts the current route from the URL.

### ``loadDroneConfigurations()``

Loads drone configurations for the drones-control view.

### ``loadSessions()``

Loads session data for the session analysis view.

### ``fetchMLLearningData()``

Fetches ML learning data for the ML learning view.

### ``layoutNavBox.setCurrentView()``

Updates the UI layout based on the current view.

## Usage

To apply these fixes:
1. Navigate directly to routes like `/dc`, `/sa`, or `/ml` without triggering a full page reload.
2. The `$nextTick()` callback ensures `currentView` is updated and triggers the correct initialization function (e.g., `loadDroneConfigurations()` for `/dc`).
3. Data fetching (e.g., `fetchMLLearningData()`) is now guaranteed to execute on initial load or route changes.

## Dependencies

> ``urlRoutingBox``
> ``layoutNavBox``
> `Vue.js reactivity system`
> ``fetch` API (for data fetching).`

## Related

- [[url-routing-box]]
- [[layout-nav-box]]
- [[frontend-data-fetching-guidelines]]

>[!INFO] Critical Reactivity Issue
> The root cause was Vue’s reactivity not syncing with URL-based navigation. `$nextTick()` ensures `currentView` updates before rendering, preventing stale state.

>[!WARNING] Data Fetching Edge Case
> If `handleViewChange()` is not called explicitly (e.g., via programmatic navigation), the auto-fetch logic in `$nextTick()` ensures data loads correctly. Test edge cases where navigation happens outside Vue lifecycle hooks.
