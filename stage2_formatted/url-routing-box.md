**Tags:** #url-routing, #sidebar-navigation, #event-driven, #hash-based-routing, #state-management
**Created:** 2026-01-13
**Type:** code-notes

# url-routing-box

## Summary

```
Handles URL routing for sidebar navigation with state synchronization via hash-based and path-based routing.
```

## Details

> The `URLRoutingBox` class manages URL-to-view mappings for a sidebar navigation system. It maintains two bidirectional maps: `routeMap` (view IDs to paths) and `pathToViewMap` (paths to view IDs). The class initializes by parsing the current URL (supports both hash-based and path-based routing) and listens for browser events (`popstate`, `hashchange`) to update the navigation state dynamically. It synchronizes the `currentView` and `currentPath` based on the parsed URL and emits a `route-change` event to notify the application of navigation updates.

## Key Functions

### `constructor()`

Initializes routing maps, sets default state, and listens for URL changes.

### `handleHashChange(event)`

Parses hash changes (e.g., `#/sm`) and updates the navigation state if a valid route is found.

### `initializeFromURL()`

Determines the current route from the URL (hash or path) and updates internal state.

### `pathToView(path)`

Maps a URL path to a view ID (helper method for route resolution).

## Usage

1. Instantiate `URLRoutingBox` to initialize routing.
2. Listen for the `route-change` event to handle navigation updates in the app.
3. Use `this.currentView` and `this.currentPath` to track the current state.

## Dependencies

> ``URL``
> ``CustomEvent` (built-in browser APIs)`

## Related

- [[URL Routing Patterns]]
- [[Event-Driven Navigation Systems]]

>[!INFO] Hash vs. Path Routing
> The class supports both hash-based (`#/sm`) and path-based (`/sm`) routing. Hash-based routing is more common for single-page apps (SPAs) due to SEO limitations.

>[!WARNING] Default Fallback
> If no valid route is found, it defaults to `'list'` (simulation view). Avoid hardcoding paths to prevent unexpected behavior.
