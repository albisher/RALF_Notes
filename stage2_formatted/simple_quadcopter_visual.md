**Tags:** #pybullet, #quadcopter, #simulation, #visualization, #robotics, #docker, #3d, #physics, #matplotlib
**Created:** 2026-01-13
**Type:** code-notes

# simple_quadcopter_visual

## Summary

```
Simulates a quadcopter with visual output generation for Docker-based PyBullet simulations.
```

## Details

> This script creates a headless quadcopter simulation using PyBullet, designed to save frames/images instead of rendering a GUI. It initializes physics, loads a ground plane, and supports creating multiple quadcopters with configurable positions. The simulator tracks positions and velocities, applies thrust forces, and simulates LiDAR sensors. Visualization data is stored in a specified directory for later processing with Matplotlib.

## Key Functions

### ``VisualQuadcopterSimulator``

Main class initializing the simulation environment, physics server, and quadcopter setup.

### ``create_quadcopter``

Loads a URDF model (e.g., cube) as a quadcopter, configures its dynamics, and stores its ID and position.

### ``get_quadcopter_state``

Retrieves current state (position, orientation, velocity) of a quadcopter using PyBullet’s physics API.

### ``apply_thrust``

Applies thrust forces to a quadcopter’s motors via external force application.

### ``simulate_lidar``

Simulates a LiDAR sensor by emitting rays from the quadcopter’s position and orientation (incomplete snippet provided).

## Usage

1. Initialize the simulator with `VisualQuadcopterSimulator(num_quadcopters=2, save_dir="simulation_output")`.
2. Create quadcopters using `create_quadcopter(position=(x, y, z))`.
3. Apply thrust forces via `apply_thrust(quad_id, [thrust1, thrust2, thrust3, thrust4])`.
4. Simulate LiDAR with `simulate_lidar(quad_id, num_rays=16, max_range=100.0)`.
5. Visualization frames are saved to `save_dir/` (e.g., `simulation_output/frame_0001.png`).

## Dependencies

> `pybullet`
> `pybullet_data`
> `numpy`
> `matplotlib`
> `matplotlib.pyplot`
> `mpl_toolkits.mplot3d`
> `time`
> `os`

## Related

- [[PyBullet Documentation]]
- [[Matplotlib 3D Visualization Guide]]

>[!INFO] Headless Mode
> The simulator uses `matplotlib.use('Agg')` to avoid GUI rendering in Docker, saving frames to disk instead.

>[!WARNING] LiDAR Simulation Incomplete
> The `simulate_lidar` function snippet is truncated; full implementation would require ray casting logic to detect obstacles or surfaces.
