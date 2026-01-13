**Tags:** #gymnasium, #pybullet, #drone_simulation, #environment_wrapper, #reinforcement_learning
**Created:** 2026-01-13
**Type:** code-notes

# gymnasium_env_box

## Summary

```
Wraps PyBullet drone simulation into a Gymnasium environment for RL tasks.
```

## Details

> This file implements a Gymnasium environment wrapper (`PyBulletDroneGymEnv`) for a drone simulation in PyBullet. It converts PyBullet’s native interface into a Gymnasium-compatible environment, enabling integration with reinforcement learning frameworks. The environment handles actions (motor thrusts) and returns observations (position, velocity, orientation, target error, wind) while managing PyBullet physics, weather, and scenario generation. The class initializes a drone simulation with configurable positions (base and building), action/observation spaces, and rendering options.

## Key Functions

### `PyBulletDroneGymEnv`

Main Gymnasium environment class wrapping PyBullet drone simulation.

### `scenario_generator`

Generates dynamic environments (e.g., obstacles, targets) based on drone positions.

### `weather_system`

Applies real-time weather conditions (wind, turbulence).

### `MLControllerBox`

Handles drone control logic (replaced legacy controller).

## Usage

1. Initialize the environment with positions and rendering options:
   ```python
   env = PyBulletDroneGymEnv(
       base_position=(0, 0, 0),
       building_position=(50, 0, 0),
       render_mode="human"  # or None for headless
   )
   ```
2. Step the environment with actions (e.g., motor thrusts):
   ```python
   obs, reward, done, info = env.step([0.5, 0.5, 0.5, 0.5])
   ```
3. Reset the environment for a new episode:
   ```python
   obs = env.reset()
   ```

## Dependencies

> ``gymnasium``
> ``pybullet``
> ``pybullet_data``
> ``numpy``
> ``..base_drone``
> ``..learning_drone``
> ``..scenario_generator``
> ``..weather_system``
> ``..ml_controller_box``

## Related

- [[gymnasium_drone_tutorial]]
- [[pybullet_drone_simulation_guide]]

>[!INFO] Single Responsibility
> This class **only** bridges PyBullet and Gymnasium; it does not manage drone physics or control logic. Dependencies like `scenario_generator` and `weather_system` are injected externally.

>[!WARNING] Physics Client Mode
> Use `headless=True` for performance; `headless=False` enables GUI rendering but increases latency. Avoid mixing modes in the same session.
