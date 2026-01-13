**Tags:** #API, #fetch, #data-fetching, #real-time-updates, #time-travel, #state-management
**Created:** 2026-01-13
**Type:** code-notes

# api-methods

## Summary

```
Handles all API communication for real-time status updates, drone state, visualization data, and building lists.
```

## Details

> This module (`ApiMethods`) encapsulates all API-related operations, adhering to a single responsibility principle. It manages asynchronous API calls via `fetch` to retrieve real-time data, including status updates (e.g., simulation time, workflow state), drone states, visualization data (with optional signal filtering), and building lists. The code includes error handling for network issues, type mismatches, and gracefully defaults values (e.g., `null`/`false` for optional fields). Time-travel functionality is implemented via a `timeHistory` array, storing up to 1000 snapshots of simulation data.

## Key Functions

### ``updateStatus()``

Fetches real-time simulation status (e.g., `running`, `simTime`, `sessionId`) and updates internal state. Respects `timeTravelMode` to avoid overwriting time.

### ``updateDrones()``

Retrieves drone states from `/api/state` and initializes `drones` array if empty.

### ``fetchVisualizationData(signal = null)``

Asynchronously fetches simulation data with optional signal filtering. Stores data in `timeHistory` for time-travel replay.

### ``refreshBuildings()``

Loads saved buildings from `/api/buildings/list` and updates `savedBuildings`.

## Usage

Initialize `ApiMethods` as a class or object with required state properties:
```javascript
const api = new ApiMethods();
api.status = { running: false, simTime: 0 }; // Example state
api.timeHistory = []; // Initialize time history
```
Call methods asynchronously:
```javascript
await api.updateStatus();
await api.fetchVisualizationData("signal123");
```

## Dependencies

> ``fetch` (built-in browser/Node.js API)`
> ``console` (for error logging).`

## Related

- [[api-state-management]]
- [[time-travel-architecture]]

>[!INFO] Time History Management
> Data is stored in `timeHistory` as deep copies (`JSON.parse(JSON.stringify())`) to prevent external modifications. The array caps at 1000 entries via `shift()`.

>[!WARNING] Fetch Errors
> Ignores `TypeError`/`fetch` errors to avoid silent failures, but logs other errors (e.g., network timeouts) for debugging.
