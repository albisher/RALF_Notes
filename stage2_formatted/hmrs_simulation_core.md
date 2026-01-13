**Tags:** #simulation, #physics, #pybullet, #drone_swarm, #weather, #building_management, #core_logic
**Created:** 2026-01-13
**Type:** code-notes

# hmrs_simulation_core

## Summary

```
Core simulation engine for HMRS drone swarm, handling physics, drone management, and weather systems.
```

## Details

> This module implements the foundational simulation logic for a drone swarm system using PyBullet. It manages physics interactions, drone spawning, building mapping, and weather conditions in a standalone simulation environment. The class `HMRSSimulationCore` initializes a physics server, configures ground plane setup, and integrates components like a building mapper, weather system, and model loader. It supports both headless and GUI modes for PyBullet and includes logging capabilities via a `LoggingBox` if available.

## Key Functions

### ``__init__``

Sets up the simulation environment with physics server connection, ground plane, and core components (building mapper, weather system, model loader).

### ``HMRSSimulationCore``

Core simulation class encapsulating physics, drone management, and weather logic.

## Usage

Initialize the core simulation with `HMRSSimulationCore(headless=True)` to run in headless mode. The class manages physics, drone spawning, and environmental factors like weather. Extend or override methods for custom logic (e.g., drone behavior, weather effects).

## Dependencies

> `pybullet`
> `pybullet_data`
> `numpy`
> `datetime`
> `pathlib`
> `swarm.building_mapper`
> `swarm.hmrs_drone_spawner`
> `swarm.base_drone`
> `swarm.weather_system`
> `swarm.master_coordinator`
> `swarm.ml_scenario_manager`
> `swarm.model_loader`
> `swarm.boxes.logging_box`

## Related

- [[swarm]]
- [[swarm]]
- [[swarm]]
- [[swarm]]

>[!INFO] Physics Server Mode
> The simulation uses PyBullet’s `DIRECT` mode in headless mode for performance. Use `p.connect(p.GUI)` for visual debugging.

>[!WARNING] Headless Mode
> If `headless=True`, ensure no GUI dependencies are needed for visualization. Logging may be limited without `LoggingBox`.
