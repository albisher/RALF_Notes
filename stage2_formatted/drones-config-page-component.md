**Tags:** #Vue, #Drone-Systems, #Configuration-UI, #Swarm-Squads, #Reactivity
**Created:** 2026-01-13
**Type:** code-notes

# drones-config-page-component

## Summary

```
Manages drone and base configuration UI with reactive swarm/squad management and event-driven updates.
```

## Details

> This component renders a drone configuration page displaying a `drones-base-config-view-component` when `currentView` is set to `'drones-base-config'`. It handles state for drone swarms, squads, and base configurations via two-way data binding (`v-model`). The component emits events for actions like adding/deleting swarms/squads, editing configurations, and weather checks. It relies on external props (`masterControls`, `availableAddons`) and emits updates to parent components.

## Key Functions

### ``drones-config-page-component``

Main container for drone and base configuration UI.

### ``components``

Registers `drones-base-config-view-component` for rendering.

### ``props``

Defines reactive inputs (`currentView`, `baseConfig`, `swarms`, etc.).

### ``emits``

Handles event-driven interactions (e.g., `save-drone-configurations`, `add-new-swarm`).

## Usage

1. Set `currentView` to `'drones-base-config'` to activate the component.
2. Provide required props (`baseConfig`, `masterControls`) and optional ones (`swarms`, `namingConvention`).
3. Trigger events via `@emit` (e.g., `@save-drone-configurations`) to update parent state.

## Dependencies

> ``DronesBaseConfigViewComponent``
> `Vue 3 reactivity system (e.g.`
> ``v-model``
> ``$emit`).`

## Related

- [[Vue 3 Composition API]]
- [[DronesBaseConfigViewComponent]]

>[!INFO] Two-Way Binding
> Uses Vue’s `v-model` for dynamic updates between this component and its parent, ensuring real-time sync of `swarms`, `squads`, and `baseConfig`.

>[!WARNING] Event Overload
> Emits multiple events for the same action (e.g., `save-swarm`/`save-squad`), requiring careful parent handling to avoid conflicts.
