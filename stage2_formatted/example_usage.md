**Tags:** #drones, #gymnasium, #multi-agent, #lidar, #camera, #path_planning, #swarm, #openai, #environment_simulation
**Created:** 2026-01-13
**Type:** code-notes

# example_usage

## Summary

```
Demonstrates practical usage of drone simulation and sensor processing boxes in a swarm environment.
```

## Details

> This file provides example code snippets for using various components from the `swarm.boxes` module, including Gymnasium/PettingZoo-based drone environments, LiDAR and camera processing, and path planning. It follows object-oriented principles with single responsibility for each box type, enabling modular integration into drone swarm simulations. The examples cover initialization, observation generation, action sampling, and obstacle detection workflows.

## Key Functions

### `example_gymnasium_env()`

Demonstrates Gymnasium-based drone environment usage with reset, step, and action sampling.

### `example_pettingzoo_env()`

Shows multi-agent drone environment with PettingZoo integration for coordinated swarm behavior.

### `example_lidar_processor()`

Illustrates LiDAR box functionality including ray direction generation and obstacle detection.

### `example_camera_processor()`

Basic initialization of camera processor with resolution parameters.

### `example_path_planner()`

(Incomplete) Path planning component demonstration (missing implementation).

### `PyBulletDroneGymEnv`

Gymnasium-compatible drone environment wrapper for PyBullet physics engine.

### `PyBulletMultiDroneEnv`

Multi-agent drone environment for swarm simulations.

### `LiDARProcessorBox`

Processes LiDAR data to detect obstacles in point clouds.

### `CameraProcessorBox`

Handles camera sensor data processing (e.g., image capture parameters).

## Usage

1. Import the `example_usage` module or run directly
2. Select an example function to demonstrate specific functionality:
   - For single-agent drone simulation: `example_gymnasium_env()`
   - For multi-agent swarm: `example_pettingzoo_env()`
   - For sensor processing: `example_lidar_processor()` or `example_camera_processor()`
3. Customize parameters (e.g., drone count, sensor ranges) before execution
4. Observe outputs including observation shapes, rewards, and detected obstacles

## Dependencies

> `numpy`
> `swarm.boxes (local module)`
> `Gymnasium`
> `PettingZoo (for multi-agent environments)`

## Related

- [[boxes]]
- [[environment]]
- [[sensors]]
- [[drone_simulation_tutorial]]

>[!INFO] Single Responsibility Principle
> Each box class (e.g., `PyBulletDroneGymEnv`, `LiDARProcessorBox`) implements exactly one function: environment simulation or sensor processing, respectively. This modular design enables easy replacement or extension of components without affecting others.

>[!WARNING] Headless Mode Warning
> Headless mode (`headless=True`) disables GUI visualization. For debugging, set `headless=False` but ensure your system can handle rendering. Some environments may fail silently if the display backend isn't properly configured.

>[!INFO] Observation Shape Note
> Gymnasium environments return observations as NumPy arrays. The shape varies by box type (e.g., `(10,)` for LiDAR, `(640, 480, 3)` for camera). Always check `obs.shape` in examples to verify data format compatibility with your controller.
