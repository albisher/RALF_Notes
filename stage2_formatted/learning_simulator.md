**Tags:** #simulation, #machine-learning, #pybullet, #drone, #physics-engine, #scenario-management
**Created:** 2026-01-13
**Type:** code-notes

# learning_simulator

## Summary

```
Manages drone-based ML learning scenarios with physics simulation, weather effects, and screenshot capture.
```

## Details

> The `LearningSimulator` class initializes a physics-based simulation environment using PyBullet for drone operations. It sets up a base and building structure, configures a shared ML controller for collaborative learning, and manages scenario generation, weather conditions, and drone operations. The simulator supports up to three concurrent learning drones while tracking their progress through predefined tasks. It integrates vision capabilities for mission observation and captures visual data for ML training.

## Key Functions

### ``__init__``

Initializes the simulation environment with physics setup, building, base, and drone configurations.

### ``model_loader.create_building``

Creates a multi-story building using URDF models.

### ``model_loader.create_base_truck``

Spawns a base vehicle at the simulation origin.

### ``scenario_generator``

Generates dynamic learning scenarios with weather conditions.

### ``shared_ml_controller``

Manages centralized ML policy updates for all drones.

### ``LearningDrone``

Individual drone instances (inferred from imported module) handle autonomous task execution.

### ``VisionDrone``

Dedicated drone for observing mission tasks (inferred from imported module).

## Usage

1. Initialize with base/building positions.
2. Spawn up to 3 `LearningDrone` instances via `self.learning_drones`.
3. Run scenarios via `scenario_generator.generate()`.
4. Capture screenshots or collect vision data for ML training.
5. Use `shared_ml_controller` to update policies across drones.

## Dependencies

> `pybullet`
> `pybullet_data`
> `numpy`
> `matplotlib`
> `scipy`
> `datetime`
> `typing`
> `collections`
> `mpl_toolkits`

## Related

- [[learning_drone]]
- [[ml_controller]]
- [[scenario_generator]]
- [[weather_system]]

>[!INFO] Physics Client Mode
> The simulator uses `p.DIRECT` mode for deterministic physics, which may impact real-time responsiveness. Consider switching to `p.GUI` for visualization debugging.


>[!WARNING] Concurrent Drones
> Exceeding `max_concurrent_drones=3` will crash the simulation due to PyBullet’s thread safety limits. Monitor drone spawn limits carefully.
