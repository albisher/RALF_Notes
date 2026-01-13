**Tags:** #Vue, #mixin, #drone, #state-management, #api-integration, #OOP, #computed, #async-io
**Created:** 2026-01-13
**Type:** code-notes

# DroneMixin

## Summary

```
Provides drone functionality as a Vue component mixin for state management and API interactions.
```

## Details

> `DroneMixin` is a Vue.js mixin designed to encapsulate drone-related logic, including state management, API communication, and drone operations. It leverages the **mixin pattern** for code reuse, integrating `DroneState`, `DroneComputed`, and `DroneService` to handle drone lifecycle (e.g., fetching, spawning) and emits events for error handling or drone creation. The mixin initializes a `DroneService` instance dynamically from a global API endpoint (`window.apiCommunicationBox` or `window.apiBox`) and delegates drone operations (e.g., `fetchDrones`, `spawnDrone`) to it. Data is merged with `DroneState` to maintain local state consistency.

## Key Functions

### ``data()``

Initializes drone state and service, merging `DroneState` data.

### ``created()``

Checks for and initializes `DroneService` with the global API endpoint.

### ``fetchDrones()``

Asynchronously retrieves all drones from the API and updates local state via `DroneState.setDrones()`.

### ``updateDrones(force)``

Alias for `fetchDrones()`; forces an update if `force=true`.

### ``spawnDrone(type, position, options)``

Creates a new drone via `DroneService.spawnDrone()`, updates local state, and emits `drone-spawned`/`error` events.

## Usage

1. Import and use the mixin in a Vue component:
   ```javascript
   import DroneMixin from './DroneMixin.js';
   export default {
       mixins: [DroneMixin],
       methods: {
           // Override or extend mixin methods as needed
       }
   };
   ```
2. Trigger drone operations via `this.fetchDrones()` or `this.spawnDrone(type, position, options)`.
3. Listen for emitted events (`drone-spawned`, `error`) in parent components.

## Dependencies

> ``../state/DroneState.js``
> ``../computed/DroneComputed.js``
> ``../services/DroneService.js``

## Related

- [[Vue]]
- [[DroneState]]
- [[DroneComputed]]
- [[DroneService]]

>[!INFO] Dynamic API Initialization
> The mixin checks `window.apiCommunicationBox` or `window.apiBox` at runtime to avoid hardcoding API endpoints. If neither is found, it logs an error.

>[!WARNING] Error Handling
> All async operations (e.g., `fetchDrones`, `spawnDrone`) include try-catch blocks. Errors are logged and emitted via `$emit('error', message)`. Local state updates may fail silently if `DroneState` methods throw.
