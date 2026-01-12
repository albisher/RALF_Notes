**Tags:** #simulation, #automation, #drone, #programmatic-mode, #replay-data, #api-integration
**Created:** 2026-01-12
**Type:** code-notes

# programmatic-simulation-implementation

## Summary

```
Implements fully automated simulation execution with drone spawning, task assignment, and motion history recording for replayable data generation.
```

## Details

> This implementation enables fully programmatic simulation control by introducing configurable flags in the `__init__` method to enable automatic drone spawning, task assignment, and motion history recording. The system dynamically spawns drones (Scout, Tanker Mule, Tanker Lifeline) after a delay, assigns tasks via optimized mission planning, and records high-frequency motion data (240Hz) for replayable sessions. The simulation runs without manual intervention, generating structured replay data stored in JSON format.

## Key Functions

### ``run_simulation_thread()``

Orchestrates the simulation loop, triggering drone spawning and task assignment.

### ``_auto_scout_buildings()``

Automatically assigns scouting missions to mapped buildings every 5 seconds.

### ``_auto_clean_windows()``

Sends cleaning drones to buildings once mapped.

### ``update_visualization_data()``

Records drone motion history (position, velocity, orientation) at each simulation step.

### ``motion_history.json``

Stores replayable data in a rolling window (max 200 points per drone).

## Usage

1. **Enable Programmatic Mode**: Set `self.programmatic_mode = True` in initialization.
2. **Start Simulation**: Trigger via API (`POST /api/start`) or UI button.
3. **Replay Data**: Access saved `motion_history.json` in `training_sessions/{session_id}` for playback.

## Dependencies

> ``simulation/hmrs_simulation_live.py``
> ``api/start` (HTTP endpoint)`
> ``session_id` storage system (for replay data).`

## Related

- [[hmrs_simulation_live]]
- [[`api-integration]]
- [[`replay-data-guide]]

>[!INFO] Critical Configuration
> Ensure `auto_spawn_delay` (2.0s) aligns with drone registration timelines to avoid conflicts.

>[!WARNING] Data Retention
> Motion history uses a rolling window (200 points), so older data may be overwritten during replay sessions.
