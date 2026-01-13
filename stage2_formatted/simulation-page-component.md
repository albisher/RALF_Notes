**Tags:** #VueJS, #SimulationUI, #ComponentArchitecture, #Sidebars, #EventHandling
**Created:** 2026-01-13
**Type:** code-notes

# simulation-page-component

## Summary

```
Main simulation visualization page component managing UI elements, sidebars, and event-driven interactions for a drone simulation.
```

## Details

> `SimulationPageComponent` is a Vue.js component that orchestrates the simulation interface by combining three sub-components: a sidebar for drone controls, a logs sidebar for communication tracking, and a visualization view for drone mapping. It uses a `currentView` state to dynamically render either a list or visualization mode, passing props like drone statuses, command forms, and log data to child components. Event handlers (`@start-simulation`, `@pause-simulation`, etc.) delegate user actions to parent logic, while the template structure ensures modular UI updates.

## Key Functions

### ``components``

Defines child components (`sidebar-component`, `logs-sidebar-component`, `visualization-view-component`) via Vue’s composition.

### ``template``

Conditionally renders the sidebar/logs and visualization based on `currentView` (e.g., `'list'` mode). Props like `:drones` and `:communication-log` feed data to child components.

### `Event delegation`

Emits events (e.g., `@spawn-drone`) to trigger parent logic for simulation control or log management.

## Usage

1. **Render**: Include `<simulation-page-component>` in a parent template.
2. **Props**: Pass state like `currentView`, `drones`, or `status` to enable dynamic UI updates.
3. **Events**: Handle emitted events (e.g., `@start-simulation`) in parent components to manage simulation lifecycle.

## Dependencies

> ``SidebarComponent``
> ``LogsSidebarComponent``
> ``VisualizationViewComponent` (Vue.js components)`
> `Vue’s `<template>` directive`
> `and event emission (`$emit`).`

## Related

- [[Vue]]
- [[Simulation UI Design Patterns]]

>[!INFO] Dynamic View Switching
> The `currentView` prop determines which UI section (`sidebar`, `logs`, or `visualization`) is active. Example: `currentView="list"` renders the sidebar and logs sidebars, while `currentView="visualization"` hides them.

>[!WARNING] Event Overload
> Excessive emitted events (e.g., `@toggle-section`) may clutter parent logic. Consider consolidating related actions (e.g., group commands under a single event like `@simulation-actions`).
