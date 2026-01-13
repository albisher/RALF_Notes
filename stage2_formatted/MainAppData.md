**Tags:** #VueJS, #StateManagement, #ModularArchitecture, #CompositionPattern, #DroneSimulation, #SingleResponsibility
**Created:** 2026-01-13
**Type:** code-notes

# MainAppData

## Summary

```
Centralized application data orchestrator consolidating state, computed properties, and mixins for a drone simulation application.
```

## Details

> `MainAppData` is a Vue.js-compatible object that consolidates all application state from modular state modules (e.g., `AppState`, `DroneState`) and computed properties (e.g., `DroneComputed`, `VisualizationComputed`). It replaces a monolithic `app-data.js` by adhering to the **Single Responsibility Principle**, reducing file size from 9,949 lines to under 200. The structure uses **composition** to merge state, computed properties, and mixins (e.g., `DroneMixin`, `SessionMixin`) via Vue’s built-in merge behavior. Core logic remains in specialized modules, while this file acts as a **glue layer** for data flow between modules.

## Key Functions

### ``data()``

Returns a merged object of all state modules (e.g., `AppState`, `DroneState`) using spread syntax.

### ``computed``

Combines computed properties from specialized modules (e.g., `DroneComputed`, `VisualizationComputed`).

### ``mixins``

Array of functional mixins (e.g., `DroneMixin`, `MasterControlsMixin`) for reusable logic (e.g., drone operations, UI utilities).

## Usage

1. Import `MainAppData` in a Vue component (e.g., `<script setup>`) and use it as a data source:
   ```js
   import MainAppData from './MainAppData.js';
   const { data, computed } = MainAppData;
   ```
2. Access merged state via `data()` (e.g., `this.data.drone.position`) or computed properties (e.g., `this.$data.computed.droneSpeed`).

## Dependencies

> ``../state/.*State.js``
> ``../computed/.*Computed.js``
> ``../mixins/.*Mixin.js``
> `Vue.js (for automatic merge of `data``
> ``computed``
> `and `mixins`).`

## Related

- [[Vue Composition API]]
- [[Modular State Management Patterns]]
- [[Drone Simulation Architecture]]

>[!INFO] State Merging
> Vue automatically merges `data`, `computed`, and `mixins` from `MainAppData` into the component’s lifecycle. Mixin data is resolved via Vue’s merge strategy, ensuring no conflicts.

>[!WARNING] Avoid Direct Manipulation
> Directly modifying `this.data` may break reactivity. Use state management libraries (e.g., Pinia) if deeper reactivity is needed.
