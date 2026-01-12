**Tags:** #logging, #communication, #simulation, #backend, #frontend, #api, #data-tracking, #real-time-updates, #drone-systems, #position-logging, #command-logging
**Created:** 2026-01-12
**Type:** code-notes

# logging-and-communication-features

## Summary

```
Tracks drone communication, position, and command logs in a simulation environment for real-time debugging and analysis.
```

## Details

> This implementation verifies a user request to log time, position, and commands for all entities in the HMRS simulation view. The system captures bidirectional communication between drones and a master node, records positional updates at high frequency (240 Hz), and logs all commands sent to drones. The backend enhances the simulation engine with logging infrastructure, while the frontend provides a dynamic sidebar displaying these logs with color-coded categorization and real-time refreshes.

## Key Functions

### ``spawn_drone()``

Logs communication establishment (master ↔ drone handshake) with timestamps, drone type, and initial position.

### ``step()``

Logs position updates (x, y, z) and commands (move_to, hover, follow) with source/target positions, timestamps, and simulation time.

### ``/api/communication``

Enhanced endpoint to stream all messages (master ↔ drones, drone ↔ drone) and position data via secure JSON serialization.

### ``clean_data_for_json()``

Backend helper to serialize numpy arrays for JSON compatibility.

### `Communication Logs Sidebar`

Frontend UI for displaying logs with color-coded borders (orange for commands, green for status, blue for establishment).

## Usage

1. **Backend Activation**: Run the modified `hmrs_simulation_live.py` to enable logging.
2. **Frontend Integration**: Load the updated `index.html` in the simulation view.
3. **Logging Triggers**:
   - Drone spawn → Logs establishment messages.
   - Command execution → Logs commands with positions.
   - Position updates → Logs real-time coordinates.
4. **Frontend Interaction**:
   - View logs in the sidebar (collapsible).
   - Clear/refresh logs via UI buttons.

## Dependencies

> ``numpy``
> ``json` (for serialization)`
> ``simulation/hmrs_simulation_live.py` (backend core)`
> ``frontend/index.html` (frontend UI).`

## Related

- [[hmrs_simulation_live]]
- [[index]]
- [[drone-communication-protocol]]
- [[simulation-data-formats]]

>[!INFO] Important Note
> Logs include timestamps in **simulation time** (not wall-clock time) to align with the 240 Hz update rate. Ensure backend and frontend clocks are synchronized for accurate analysis.


>[!WARNING] Caution
> High-frequency logging (240 Hz) may consume significant memory. The log limit is capped at 200 entries to prevent overload. For long simulations, consider throttling or archiving older logs.
