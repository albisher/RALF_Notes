**Tags:** #drone, #simulation, #physics, #ai, #multi_rotor, #gaming, #simulation_engine
**Created:** 2026-01-13
**Type:** code-notes

# hmrs_drone_spawner

## Summary

```
Manages drone spawning and configuration for HMRS (High-Mobility Multi-Role System) drones with configurable types and parameters.
```

## Details

> This module implements a spawner class (`HMRSDroneSpawner`) for initializing and managing HMRS drones. It supports a variety of drone types (e.g., scout, tanker, quadcopter) and allows dynamic spawning based on user input. The spawner integrates with a physics client (PyBullet), building mapper, and optional weather systems. It provides metadata for each drone type, including battery life, payload capacity, and sensor capabilities.
> 
> The `HMRSDroneType` enum categorizes drone types into original HMRS models, multi-rotor, fixed-wing, helicopter, tiltrotor, and bio-inspired designs. The spawner initializes with configurable parameters like base position and weather effects, loading drone models via `ModelLoader`.

## Key Functions

### ``HMRSDroneType``

Enum defining all supported drone types with descriptive names.

### ``HMRSDroneSpawner.__init__()``

Initializes spawner with physics client, building mapper, and optional weather system.

### ``model_loader``

Instance of `ModelLoader` for loading drone physics models (instantiated in `__init__`).

## Usage

1. Instantiate `HMRSDroneSpawner` with required physics client and building mapper.
2. Use `available_drones` dictionary to select drone types (e.g., `HMRSDroneType.SCOUT`).
3. Spawn drones dynamically by leveraging the spawner’s integration with physics/weather systems.

## Dependencies

> ``.base_drone``
> ``.building_mapper``
> ``.model_loader``
> ``.boxes.drone_name_formatter_box``
> `PyBullet (via `physics_client`)`
> `NumPy.`

## Related

- [[none]]

>[!INFO] Important Note
> The `ModelLoader` class is responsible for loading drone physics models into the physics client, ensuring compatibility with PyBullet. This is a critical dependency for drone simulation.

>[!WARNING] Caution
> Hardcoded default values (e.g., `base_position = (0.0, 0.0, 0.0)`) may need adjustment for complex simulations. Ensure `physics_client` and `building_mapper` are properly initialized before instantiation.
