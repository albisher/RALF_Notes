**Tags:** #drone-service, #business-logic, #api-integration, #dependency-injection, #async-io
**Created:** 2026-01-13
**Type:** code-notes

# DroneService

## Summary

```
Handles drone operations via HTTP API with OOP principles and dependency injection.
```

## Details

> `DroneService` implements a class-based service for drone management, abstracting HTTP communication via `APIBox` (dependency-injected). It encapsulates drone lifecycle methods (fetching, spawning, commanding) with error handling and logging. The service follows single responsibility by delegating API calls to `APIBox`, ensuring modularity.

## Key Functions

### ``constructor(apiBox)``

Initializes service with required `APIBox` dependency, validating its presence.

### ``getAllDrones()``

Asynchronously retrieves drone list from `/api/drones`, returning an array or empty array on failure.

### ``spawnDrone(type, position, options)``

Spawns a drone via `/api/spawn`, using provided type/position and defaults vendor to `'simulation'`.

### ``sendCommand(droneName, commandType, parameters)``

Executes drone commands (e.g., `move_to`) via `/api/command`, merging parameters dynamically.

### ``moveDroneToPosition()``

Alias for `sendCommand` with `commandType="move_to"`, simplifying position-based commands.

## Usage

```javascript
const apiBox = new APIBox(); // Assume configured elsewhere
const droneService = new DroneService(apiBox);

// Fetch all drones
await droneService.getAllDrones();

// Spawn a drone
await droneService.spawnDrone('scout', [1, 2, 3], { vendor: 'dji' });

// Send a command
await droneService.sendCommand('drone1', 'move_to', { target: [0, 0, 0] });
```

## Dependencies

> ``../../boxes/generic/APIBox.js``

## Related

- [[DroneAPISpec]]
- [[APIBoxImplementation]]

>[!INFO] Dependency Validation
> Throws `Error` if `APIBox` is not provided during construction.

>[!WARNING] Error Handling
> Logs errors to `console` before re-throwing, which may mask silent failures in production.
