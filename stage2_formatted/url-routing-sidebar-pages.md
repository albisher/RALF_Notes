**Tags:** #url-routing, #sidebar-navigation, #vuejs, #frontend-development, #web-routing
**Created:** 2026-01-12
**Type:** code-notes

# url-routing-sidebar-pages

## Summary

```
Implements URL routing for sidebar navigation in a Vue.js frontend application to enable URL updates and browser back/forward functionality.
```

## Details

> This implementation enables dynamic URL updates when navigating sidebar pages, ensuring the URL reflects the current view. The system maps predefined view IDs to URL paths, initializes from the current URL on page load, and handles browser back/forward navigation via the `popstate` event. It integrates with the Vue.js app to update the `currentView` and supports future sub-page navigation.

## Key Functions

### ``navigateToView(viewId, pushState)``

Updates URL and triggers navigation to a specified view.

### ``navigateToSubPage(viewId, subPage, pushState)``

Handles navigation to sub-pages (e.g., `/mc/gps`).

### ``pathToView(path)``

Converts URL paths (e.g., `/sa`) to view IDs.

### ``viewToPath(viewId)``

Converts view IDs (e.g., `analysis`) to URL paths.

### ``handlePopState(event)``

Manages browser back/forward navigation via `popstate` events.

### ``URLRoutingBox` initialization`

Loads and processes the current URL on app startup.

### ``handleViewChange` in `app.js``

Updates URL and `currentView` when sidebar navigation occurs.

## Usage

1. **Initialization**: Load `url-routing-box.js` before `logging-box.js` in `index.html`.
2. **Navigation**: Click sidebar items to update the URL and trigger navigation.
3. **Browser Navigation**: Back/forward buttons work via `popstate` event handling.
4. **Sub-Pages**: Add sub-paths (e.g., `/mc/gps`) using `navigateToSubPage`.

## Dependencies

> `Vue.js framework`
> ``simulation/frontend/boxes/url-routing-box.js``
> ``simulation/frontend/app.js``
> ``simulation/frontend/index.html``
> ``session-analysis-page-component.js`.`

## Related

- [[url-routing-box]]
- [[app]]
- [[index]]

>[!INFO] Important Note
> The `URLRoutingBox` maps predefined routes (e.g., `/sa` → `analysis`) and initializes `currentView` based on the current URL. Ensure all sidebar items match existing routes to avoid navigation errors.


>[!WARNING] Caution
> Sub-page navigation (e.g., `/mc/gps`) is not yet fully implemented but is planned. Test with future updates to avoid broken links.
