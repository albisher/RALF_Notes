**Tags:** #multi-agent, #simulation, #pettingzoo, #pybullet, #drone, #parallel_env
**Created:** 2026-01-13
**Type:** code-notes

# pettingzoo_env_box

## Summary

```
Wraps PyBullet multi-drone simulation into a PettingZoo-compatible environment box for agent-based reinforcement learning.
```

## Details

> This file implements `PyBulletMultiDroneEnv`, a PettingZoo `ParallelEnv` wrapper that converts PyBullet’s multi-agent drone simulation into a PettingZoo interface. It handles agent actions (motor thrusts) as input and returns observations (state vectors including position, velocity, orientation, target error, and wind) alongside rewards, done flags, and info dictionaries. The environment initializes drones, simulates their interactions with a base and building, and supports both headless and GUI rendering modes.
> 
> The class inherits from `ParallelEnv` and defines action/observation spaces for each drone. PyBullet physics (e.g., gravity, time step) is configured, and a plane is loaded as a base. The `MLControllerBox` and other dependencies (e.g., `BaseDrone`, `ScenarioGenerator`) are referenced but not directly instantiated here.

## Key Functions

### ``PyBulletMultiDroneEnv.__init__``

Initializes drone count, positions, and PyBullet physics client. Sets up action/observation spaces and loads the simulation environment.

### ``self.action_spaces``

Defines a 4D box (0.0–1.0) for each drone’s motor thrusts.

### ``self.observation_spaces``

Defines a 16D box (floating-point) for each drone’s state (position, velocity, orientation, target error, wind).

### ``p.connect()``

Configures PyBullet client (direct or GUI mode).

### ``p.loadURDF()``

Loads the plane URDF as the drone base.

## Usage

1. Instantiate the environment with `PyBulletMultiDroneEnv(num_drones=4)`.
2. Call `reset()` to initialize the simulation.
3. Provide actions via `step(actions_dict)` where `actions_dict` maps agent IDs to motor thrusts (e.g., `{f"drone_0": [0.5, 0.5, 0.5, 0.5]}`).
4. Retrieve observations, rewards, and done flags from the return tuple.

## Dependencies

> ``pettingzoo``
> ``pybullet``
> ``pybullet_data``
> ``numpy``
> ``gymnasium``
> ``..base_drone``
> ``..learning_drone``
> ``..ml_controller_box``
> ``..scenario_generator``
> ``..weather_system``

## Related

- [[`pettingzoo` documentation]]
- [[`PyBullet` documentation]]
- [[`BaseDrone` class]]
- [[`MLControllerBox` class]]

>[!INFO] Single Responsibility
> This class **only** bridges PyBullet’s multi-agent simulation to PettingZoo’s interface. It does not handle drone physics, weather, or scenario generation—those are delegated to other modules (e.g., `ScenarioGenerator`, `WeatherSystem`).

>[!WARNING] Physics Client Mode
> Use `headless=True` for performance; `headless=False` enables GUI rendering but increases latency. Direct mode (`p.DIRECT`) is faster but lacks visual feedback.
