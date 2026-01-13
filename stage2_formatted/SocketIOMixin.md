**Tags:** #Real-time, #SocketIO, #EventHandling, #WebSocket, #ReactiveUI, #Simulation, #DataSync
**Created:** 2026-01-13
**Type:** code-notes

# SocketIOMixin

## Summary

```
Manages Socket.IO event listeners for real-time updates in a simulation application.
```

## Details

> `SocketIOMixin` is a mixin object designed to handle Socket.IO event listeners, enabling real-time status, drone, visualization, and log updates. It checks for Socket.IO availability and falls back to HTTP polling if Socket.IO is unavailable. The mixin initializes listeners for `status-update` and `drones-update` events, updating internal state variables like `status.running`, `simTime`, and drone positions. It also integrates with OSM views to highlight target buildings and ensures time synchronization only when the simulation is running.

## Key Functions

### `setupSocketIOListeners()`

Sets up Socket.IO event listeners for real-time updates. Validates Socket.IO availability and initializes listeners for `status-update` and `drones-update` events.

### `status.running`

Tracks whether the simulation is currently running.

### `status.simTime`

Stores the current simulation time.

### `status.targetBuilding`

Stores the target building ID for visualization updates.

## Usage

1. Attach `SocketIOMixin` to a Vue.js component or similar framework as a mixin.
2. Call `setupSocketIOListeners()` to initialize event listeners.
3. Use internal state variables (`status`, `currentTime`) to react to real-time updates.

## Dependencies

> `window.socketIOBox`
> `window.loggingBox`
> `window.osmIntegrationBox`
> `window.socketIOBox.socket (Socket.IO client)`
> `this.status (internal state)`
> `this.maxSimTime (internal state)`
> `this.currentTime (internal state)`
> `this.timeTravelMode (internal state)`

## Related

- [[SocketIOBox]]
- [[OSMIntegrationBox]]
- [[LoggingBox]]

>[!INFO] Critical Fallback
> If `window.socketIOBox` or `window.socketIOBox.socket` is unavailable, the code logs a warning and switches to HTTP polling mode, disabling real-time functionality.


>[!WARNING] Dependency Risk
> Missing `window.osmIntegrationBox` or `window.loggingBox` may cause silent failures in highlighting buildings or logging debug messages. Always ensure these dependencies are initialized before calling `setupSocketIOListeners()`.
