**Tags:** #Vue, #state-management, #drone-swarm, #data-structure, #communication-log, #simulation
**Created:** 2026-01-13
**Type:** code-notes

# app-data

## Summary

```
Manages core application state for a drone swarm simulation system, including UI layout, drone operations, and logging.
```

## Details

> This file defines a Vue.js-compatible data structure (`MainAppData`) for a drone swarm application. It centralizes state like drone positions, sensor data, and UI controls (e.g., `currentView`, `layoutMode`). The system uses modular components (e.g., `APICommunicationBox`) for communication channels and integrates with a planned Socket.IO backend for swarm coordination. Key features include:
> - **Drone management**: Tracks drones (`drones[]`), selected drone (`selectedDrone`), and status (`droneStatus`).
> - **Command handling**: Stores and processes drone commands (`commandForm`, `commandStatus`).
> - **Session management**: Manages simulation sessions (`status` object) with workflow states (e.g., `'initializing'`).
> - **Logging system**: Maintains logs for drones (`communicationLog`) and system events (e.g., `systemLogsManuallyCleared` flags).
> - **UI controls**: Configures layout modes (e.g., `'quad'`) and toggles for UI sections (e.g., `masterControls`).
> 
> The data is designed for modularity, allowing external components (e.g., UI or backend) to interact via computed properties or methods.

## Key Functions

### ``data()``

Initializes core application state (e.g., drone arrays, UI flags).

### ``status` object`

Tracks simulation state (e.g., `running`, `sessionWorkflowState`).

### ``spawnForm`/`commandForm``

Handles drone placement and command inputs.

### ``communicationLog``

Stores drone/sensor communication records.

## Usage

To use this data structure:
1. **Initialize**: Inject `MainAppData` into a Vue component’s `data()` or `provide/inject` for global access.
2. **Modify state**: Update fields like `drones` or `commandForm` to reflect actions (e.g., drone movement).
3. **React to changes**: Use Vue’s reactivity to update UI dynamically (e.g., `selectedDrone` triggers UI updates).
4. **Log data**: Append to `communicationLog` or system logs for debugging/tracking.

## Dependencies

> `Vue.js (for reactivity)`
> `potential Socket.IO (for swarm communication)`
> `Plotly/Cesium (for visualization`
> `indirectly via `osmViewEnabled`).`

## Related

- [[00-drone-swarm-communication-research]]
- [[drone-swarm-ui-layout]]

>[!INFO] State Management
> This data structure is **reactive**—changes to `drones`, `status`, or `commandForm` will trigger Vue’s reactivity system, updating dependent components (e.g., drone visualizations or UI controls). Ensure external code uses `this.$data` or Vue’s reactivity API to avoid stale references.

>[!WARNING] Manual Log Clearing
> Flags like `logsManuallyCleared` prevent unintended refreshes from repopulating cleared logs. Override these flags carefully to avoid data loss or inconsistent state. Use them sparingly in production.
