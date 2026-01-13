**Tags:** #swarm-robotics, #coordination-algorithms, #drone-control, #centralized-control
**Created:** 2026-01-13
**Type:** code-notes

# master_controller

## Summary

```
Centralized drone swarm controller managing worker drones and camera observations.
```

## Details

> The `MasterController` class acts as the central processing unit for a drone swarm, coordinating between a master drone, worker drones, and an observer camera. It maintains a command queue, tracks mission phases (idle, learning, executing), and logs processing history. The class processes camera observations to extract worker drone positions, velocities, and distances from the master drone, then computes swarm metrics like centroid and positional spread.

## Key Functions

### ``register_worker(worker`

WorkerDrone)`**: Adds a worker drone to the swarm’s active list.

### ``process_observations()``

Parses camera data, calculates worker positions, velocities, and computes swarm-wide metrics (e.g., centroid, spread).

### ``__init__(master_drone, observer)``

Initializes the controller with a master drone and camera, setting up internal queues and tracking variables.

## Usage

1. Instantiate with a `BaseDrone` (master drone) and `ObserverCamera` object.
2. Call `register_worker()` to add worker drones.
3. Periodically call `process_observations()` to update swarm state from camera data.
4. Use `command_queue` and `mission_phase` to manage execution workflows.

## Dependencies

> `numpy`
> ``.base_drone``
> ``.worker_drone``
> ``.observer_camera``

## Related

- [[swarm_architecture]]
- [[drone_communication_protocol]]

>[!INFO] Critical State Tracking
> The `swarm_state` dictionary in `process_observations()` includes metrics like centroid and spread, which are essential for dynamic swarm coordination. Missing workers or invalid observations return a placeholder `{'status': 'no_observation'}`.

>[!WARNING] Distance Calculation
> Distance calculations use `np.linalg.norm()`, which assumes Euclidean distance. For non-Euclidean spaces (e.g., spherical coordinates), preprocess positions before calling this method.
