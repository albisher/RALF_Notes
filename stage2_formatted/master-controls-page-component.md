**Tags:** #Vue, #React, #UI-Component, #Game-UI, #Master-Control, #Event-Dispatcher
**Created:** 2026-01-13
**Type:** code-notes

# master-controls-page-component

## Summary

```
Handles master command and control UI rendering for a game application, managing sessions, replay, and system settings.
```

## Details

> This component is a Vue.js/Vue-like structure (likely a Vue Single File Component) that renders the **master controls view** for a game application. It acts as a container for `master-controls-view-component`, conditionally displaying it based on `currentView === 'master'`. It manages data flows via props (e.g., `sessions`, `status`) and emits events (e.g., session selection, replay controls) to handle interactions like loading sessions, toggling replay modes, or adjusting weather settings. The component is designed to decouple UI rendering from business logic, relying on emitted events for state updates.

## Key Functions

### ``MasterControlsPageComponent``

Orchestrates the master controls UI and dispatches events for session/replay management.

### ``components``

Registers `master-controls-view-component` as a child component.

### ``props``

Receives game state (e.g., `currentView`, `sessions`, `masterControls`).

### ``emits``

Handles 14+ event callbacks (e.g., `@load-sessions`, `@play-replay`) for external logic integration.

## Usage

1. **Pass required props** (e.g., `currentView`, `status`, `masterControls`) to render the component.
2. **Trigger events** via child components (e.g., `@select-session`) to update game state.
3. **Conditionally render** the master view only when `currentView === 'master'`.

## Dependencies

> ``MasterControlsViewComponent` (child component)`
> `Vue.js core (for reactivity and event handling).`

## Related

- [[Vue Single File Component Guide]]
- [[Game UI Architecture]]
- [[Session Management Component]]

>[!INFO] Event Emission
> Events like `@load-sessions` are emitted to parent components for state updates, ensuring modularity.

>[!WARNING] Prop Validation
> `currentView` and `masterControls` are marked `required`—missing them will trigger errors.
