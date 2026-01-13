**Tags:** #swarm-robotics, #sensor, #pybullet, #observation, #ground-station
**Created:** 2026-01-13
**Type:** code-notes

# observer_camera

## Summary

```
A ground-based observer camera class for tracking drones in a swarm using PyBullet physics simulation.
```

## Details

> The `ObserverCamera` class extends `BaseDrone` to create a stationary or mobile ground-based camera that observes drone swarm positions. It initializes with configurable FOV (60°), max observation range (50m), and orientation parameters (pitch -45°, yaw 0°). The `observe_swarm` method computes drone positions relative to the camera, checks if they fall within FOV and range, and returns structured observations including drone names, IDs, positions, velocities, and timestamps.

## Key Functions

### ``__init__``

Initializes the camera with PyBullet body ID, position, and observation parameters.

### ``observe_swarm``

Processes a list of `BaseDrone` objects, calculates relative positions, applies FOV/range checks, and returns observations as a dictionary.

## Usage

```python
camera = ObserverCamera(camera_id=1, position=(0, 0, 0), physics_client=physics_client)
drones = [drone1, drone2]  # List of BaseDrone objects
observations = camera.observe_swarm(drones)
```

## Dependencies

> `numpy`
> `pybullet`
> ``.base_drone` (custom module)`

## Related

- [[swarm_robotics_system]]
- [[base_drone]]

>[!INFO] Field of View (FOV) Limitation
> The FOV check is simplified and assumes a vertical cone centered on the camera's pitch angle. For precise tracking, consider implementing a more sophisticated FOV model (e.g., using trigonometric constraints for horizontal/vertical limits).

>[!WARNING] Distance Threshold
> If `max_range` is exceeded, drones are silently dropped from observations. Ensure the camera’s range is dynamically adjusted based on swarm density to avoid data loss.
