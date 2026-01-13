**Tags:** #Vue, #UI-Component, #MasterControls, #SessionManagement, #Configuration
**Created:** 2026-01-13
**Type:** code-notes

# master-controls-view-component

## Summary

```
Vue-based UI component for master command controls, managing sessions, GPS settings, and configuration status.
```

## Details

> This component renders a Vue.js template for a "Master Controls" view, primarily handling session management and configuration UI elements. It displays a dropdown for session selection (via header) and a dropdown for GPS mode selection (simulation, current location, or custom coordinates). The component emits events (e.g., `gps-mode-change`) when user interactions occur. The template uses inline styles for layout, responsive padding, and dark-themed UI elements. The `currentView` prop determines visibility, and `masterControls` data is dynamically rendered based on its state.

## Key Functions

### ``template``

Renders the UI structure with session header, GPS dropdown, and conditional coordinate inputs.

### ``v-model` bindings`

Syncs dropdown selections (e.g., `masterControls.gpsMode`) with parent state.

### ``@change` event`

Triggers `gps-mode-change` emission when GPS mode is updated.

### `Conditional rendering`

Displays coordinate inputs only for "simulation" or "custom" GPS modes.

## Usage

1. Import and use as a Vue component with `currentView` prop set to `'master'`.
2. Bind `masterControls` data to parent state (e.g., `masterControls.gpsMode`, `masterControls.configured`).
3. Listen for emitted events (e.g., `gps-mode-change`) in parent components.

## Dependencies

> `Vue.js (for reactivity and template binding)`
> `Vuex/Pinia (likely for `masterControls` state management).`

## Related

- [[Vue]]
- [[Session Management Pattern]]
- [[Dark-Themed UI Design]]

>[!INFO] State Dependency
> The component relies on external state (`masterControls`) for dynamic UI updates (e.g., showing/hiding coordinate inputs). Ensure parent state is properly initialized before rendering.

>[!WARNING] Event Emission
> Emitted events (e.g., `gps-mode-change`) must be handled by parent components to propagate changes to the application state. Missing listeners may cause stale UI.
