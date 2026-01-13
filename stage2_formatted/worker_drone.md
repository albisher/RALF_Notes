**Tags:** #legacy, #drone, #swarm, #deprecated, #gps, #battery, #learning, #pybullet
**Created:** 2026-01-13
**Type:** code-notes

# worker_drone

## Summary

```
Legacy worker drone class implementing basic learning behavior for following master commands in a drone swarm.
```

## Details

> This file defines a `WorkerDrone` class that inherits from `BaseDrone` and implements simple learning to execute commands like `move_to`, `hover`, or `follow`. It includes GPS tracking, battery management, and performance metrics. The class tracks positional errors, command history, and connection status to a master drone. The drone uses a `GPSTracker` for relative navigation and a `BatteryModel` to simulate energy consumption. The initialization sets up basic parameters like accuracy (1cm), target height (1.0m), and learning rate (0.1). The drone processes commands by updating its target position and height, with error history stored for performance analysis.

## Key Functions

### ``__init__``

Initializes drone with ID, position, physics client, and worker-specific attributes (e.g., `worker_id`). Sets up GPS tracker, battery model, and learning parameters.

### ``receive_command``

Parses incoming command dictionary (e.g., `move_to`, `hover`, `follow`) and updates target state (position/height) based on command type.

### ``get_position``

(Inherited from `BaseDrone`) Returns current drone position (assumed to be called elsewhere).

### ``base_position``

(Inherited) Base reference position for relative GPS tracking.

## Usage

1. Instantiate `WorkerDrone` with drone ID, initial position, physics client, and worker ID.
2. Call `receive_command` with a dictionary containing command type (e.g., `move_to`) and target parameters.
3. Monitor `successful_commands`/`failed_commands` for performance tracking.

## Dependencies

> ``.base_drone``
> ``.gps_tracker``
> ``.battery_model``
> ``numpy``
> ``pybullet``

## Related

- [[MIGRATION_GUIDE]]
- [[worker_drone_boxed]]

>[!INFO] Important Note
> This class is **deprecated**—use `worker_drone_boxed.py` instead, which adheres to a boxed architecture for better modularity and scalability.

>[!WARNING] Caution
> Do not use this file in new projects. It lacks modern design patterns and is incompatible with updated dependencies. Refer to the migration guide for updates.
