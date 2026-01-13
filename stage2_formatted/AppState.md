**Tags:** #Vue, #StateManagement, #ApplicationState, #UIState, #SimulationState, #SingleResponsibility
**Created:** 2026-01-13
**Type:** code-notes

# AppState

## Summary

```
Manages core application state for UI, layout, and simulation in a Vue.js-based application.
```

## Details

> `AppState` is a utility class implementing a **single responsibility principle** to encapsulate all core application-level state, including view settings, UI expansions, simulation status, and command/logs management. It leverages Vue.js conventions (e.g., `data()`) and provides methods to reset, toggle, and update state dynamically. The class enforces a fixed layout mode (`quad`) and enforces default expanded sections (e.g., `sessions`, `command`). State includes nested objects for UI sections, simulation workflows, and command/logs tracking.

## Key Functions

### ``getDefaultState()``

Returns a static default state object with all UI/simulation configurations.

### ``data()``

Mimics Vue’s `data()` function, returning the default state for Vue component initialization.

### ``reset(vueInstance)``

Resets the Vue component’s state to defaults by copying the default state object.

### ``toggleSection(vueInstance, sectionName)``

Toggles the visibility of a UI section (e.g., `logsSidebarHidden`, `sessions`) by flipping its boolean value.

## Usage

1. **Initialize**: Use `AppState.data()` in a Vue component’s `data()` function to inject default state.
2. **Reset**: Call `AppState.reset(vueInstance)` to revert to defaults.
3. **Toggle Sections**: Call `AppState.toggleSection(vueInstance, "sectionName")` to expand/collapse UI sections.
4. **Update Status**: Manually update state properties (e.g., `vueInstance.status.running = true`) for dynamic changes.

## Dependencies

> `Vue.js (for reactivity and component state management).`

## Related

- [[Vue]]
- [[Core UI Component Architecture]]

>[!INFO] Default Layout Enforcement
> The `layoutMode` is hardcoded to `'quad'` (no other modes allowed), and `osmViewEnabled` defaults to `false`. This ensures consistency across app instances.

>[!WARNING] Vue Instance Dependency
> `reset()` and `toggleSection()` require a Vue component instance (`vueInstance`). Ensure the instance exists before calling these methods to avoid errors.
