**Tags:** #Vue.js, #Simulation, #UI-Component, #Data-Visualization, #Sidebar, #Event-Dispatching
**Created:** 2026-01-13
**Type:** code-notes

# simulation-page-component-layout5

## Summary

```
Simplified Vue.js simulation page layout component for visualization without a full sidebar.
```

## Details

> This component (`SimulationPageComponentLayout5`) is a Vue.js template for a simulation page with a minimal sidebar toggle. It primarily renders a `visualization-view-component` when the sidebar is hidden (`logsSidebarHidden` is `true`), while the `logs-sidebar-component` is conditionally rendered only when the sidebar is visible. The layout uses Vue’s `<v-if>` directives to dynamically show/hide components based on the `currentView` and `logsSidebarHidden` state. Key props like `currentView`, `currentTime`, and `timeTravelMode` control the visualization behavior, while event handlers (`@time-slider-change`, `@toggle-sidebar`, etc.) manage interactions like time travel, log toggles, and sidebar visibility.
> 
> The component emits events to parent components for actions like toggling the sidebar, updating logs, or triggering UI resets (e.g., camera or legend adjustments).

## Key Functions

### ``visualization-view-component``

Displays simulation data with configurable layout modes, time controls, and OSM view support.

### ``logs-sidebar-component``

Conditionally renders a sidebar with communication logs, filters, and toggle controls for log sections.

### `Event Handlers`

Manages interactions like `@time-slider-change`, `@toggle-sidebar`, and `@export-logs` via `$emit`.

## Usage

1. **Conditional Rendering**: Use `currentView` and `logsSidebarHidden` to control component visibility.
2. **Data Flow**: Pass props like `currentTime`, `maxSimTime`, or `filteredLogs` to control visualization/logs behavior.
3. **Event Handling**: Trigger actions via emitted events (e.g., `@time-slider-change` updates parent state).

## Dependencies

> ``LogsSidebarComponent``
> ``VisualizationViewComponent``
> `Vue.js core (for reactivity and directives like `<v-if>`).`

## Related

- [[simulation-page-component]]
- [[visualization-view-component]]
- [[logs-sidebar-component]]

>[!INFO] Dynamic Component Switching
> The `v-if` directives ensure the sidebar (`logs-sidebar-component`) is hidden by default unless explicitly toggled via `logsSidebarHidden`. This avoids unnecessary rendering overhead.

>[!WARNING] State Management
> Ensure parent components handle emitted events (e.g., `@time-slider-change`) to maintain consistency across the simulation UI. Missing event listeners may cause stale data or UI glitches.
