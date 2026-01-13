**Tags:** #simulation, #robotics, #drone, #oop, #ml, #building_mapping, #box_architecture, #autonomous, #drone_automation, #drone_systems
**Created:** 2026-01-13
**Type:** documentation

# HMRS_README

## Summary

```
Documentation for the HMRS (Heterogeneous Multi-Robot System) simulation framework, detailing its complete implementation with drone types, OOP design, and ML capabilities.
```

## Details

> The `HMRS_README` provides a comprehensive overview of the HMRS simulation system, emphasizing its modular, reusable architecture based on the **Box Architecture** principle. It outlines four specialized drone types (Scout, Tanker-Mule, Tanker-Lifeline, Overseer) and highlights key components like real-time LiDAR mapping, ML training, and autonomous docking. The system avoids CAD models by generating building maps dynamically from LiDAR data, storing them persistently for reuse. The documentation includes usage examples for spawning drones and initiating mapping missions.

## Key Functions

### `Box Architecture`

Modular design ensuring single responsibility and reusability.

### `AdvancedLiDARBox`

Real-time 3D mapping and obstacle classification.

### `MLControllerBox`

Trainable neural network for drone control.

### `Building Mapping`

LiDAR-based autonomous building generation.

### `HMRSScoutDrone`

Dynamic mapping and pre-computation for Scout drones.

### `HMRSSimulation`

Core simulation engine for drone management and spawning.

## Usage

1. **Initialize Simulation**: Create an instance of `HMRSSimulation` with optional headless mode.
2. **List Drones**: Retrieve available drone types via `list_available_drones()`.
3. **Spawn Drones**: Instantiate drones using predefined types (e.g., `scout`, `tanker_lifeline`) with custom positions and names.
4. **Trigger Mapping**: Use Scout drones to generate building maps from LiDAR data without CAD input.

## Dependencies

> `- Python libraries (likely including `numpy``
> ``pandas``
> `custom drone simulation frameworks).
- Real-time sensor data processing libraries (e.g.`
> ``OpenCV``
> ``PyTorch` for ML).
- LiDAR and camera hardware interfaces (if hardware-based).`

## Related

- [[HMRS_Simulation_Engine]]
- [[HMRS_Drone_Classes]]
- [[Building_Mapping_Algorithm]]

>[!INFO] Key Feature
> The system’s **Box Architecture** ensures modularity, allowing easy integration of new components (e.g., additional LiDAR processors) without redesigning the core simulation.


>[!WARNING] Dependency Note
> Ensure LiDAR/camera hardware is compatible with the simulation’s real-time processing requirements. Headless mode may not support hardware sensors.
