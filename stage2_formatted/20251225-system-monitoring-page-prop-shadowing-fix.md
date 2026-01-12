**Tags:** #Vue.js, #prop-shadowing, #Vue-components, #frontend-development, #debugging, #reactivity
**Created:** 2026-01-12
**Type:** code-notes

# system-monitoring-page-component.js

## Summary

```
Fixes Vue.js prop shadowing issue where `currentView` data property incorrectly overrode the prop value, preventing the System Monitoring page from rendering.
```

## Details

> The `SystemMonitoringPageComponent` failed to render because its `currentView` prop was shadowed by a data property with the same name. Vue.js treats data properties as higher priority than props, causing the component to ignore the prop value and check against `null` instead. The fix removed the redundant data property, ensuring the prop value is correctly used in conditional rendering (`v-if`).

## Key Functions

### ``SystemMonitoringPageComponent``

Main component that renders system monitoring panels; relies on `currentView` prop for conditional rendering.

### ``currentView` prop`

Determines which page/view to render; previously shadowed by a data property.

### ``v-if="currentView === 'system-monitoring'"``

Conditional rendering logic that was broken due to shadowing.

## Usage

1. Navigate to `/sm/` or trigger the component via sidebar.
2. The component now correctly renders when `currentView` matches `'system-monitoring'`.
3. Requires a hard refresh (`Ctrl+Shift+R` or `Cmd+Shift+R`) to apply changes.

## Dependencies

> `Vue.js (v3.x)`
> `Vue Router (for URL routing)`
> `Vuex (if used for state management).`

## Related

- [[app]]
- [[app-component]]
- [[url-routing-box]]

>[!INFO] Prop Shadowing Pitfall
> Vue.js prioritizes data properties over props when names conflict. Always verify that prop names do not shadow data properties to avoid silent rendering failures.

>[!WARNING] Hard Refresh Required
> Cache may prevent immediate visual updates. Use a hard refresh to ensure the latest code is loaded.
