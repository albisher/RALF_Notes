**Tags:** #swarm-control, #robotics, #pybullet, #mission-management, #ground-station
**Created:** 2026-01-13
**Type:** code-notes

# ground_master

## Summary

```
Centralized ground control for drone swarm observation and mission coordination.
```

## Details

> The `GroundMaster` class serves as a ground-based control station for a drone swarm, integrating sensor data from an observer camera and worker drones via PyBullet physics simulation. It manages mission phases (e.g., connection, transit, operating), processes GPS/waypoint data, and coordinates commands through a queue. The system tracks worker capabilities, preflight results, and applies machine learning for adaptive decision-making. Static physics settings ensure the ground station remains fixed.

## Key Functions

### ``__init__``

Initializes the ground station with PyBullet body ID, position, mission config, and observer camera. Sets up static physics, worker registries, and mission state variables.

### ``register_worker``

Adds a worker drone (e.g., `WorkerDrone`) to the swarm registry.

### ``process_sensor_data``

(Incomplete snippet) Likely processes raw sensor data (e.g., GPS, camera feeds) into structured mission commands (returns a dictionary of processed observations).

## Usage

1. Instantiate `GroundMaster` with:
   - `master_id` (PyBullet body ID for ground station),
   - `position` (3D coordinates),
   - `physics_client` (PyBullet connection handle),
   - `mission_config` (e.g., target distance to building),
   - `observer` (camera for visual/sensor data).
2. Register workers via `register_worker`.
3. Process mission data (e.g., GPS updates) via `process_sensor_data` (extend logic for full implementation).

## Dependencies

> ``numpy``
> ``pybullet``
> ``.base_drone``
> ``.worker_drone``
> ``.observer_camera``
> ``.mission_config``
> ``.master_learning``

## Related

- [[`base_drone]]
- [[`worker_drone]]
- [[`mission_config]]

>[!INFO] Static Physics Note
> The `p.changeDynamics` call sets the ground station’s mass to 0, ensuring it remains stationary in PyBullet simulations.

>[!WARNING] Data Processing Incomplete
> The `process_sensor_data` method is truncated; full implementation must integrate worker sensor inputs (e.g., GPS, IMU) into mission commands.
