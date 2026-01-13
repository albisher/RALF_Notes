**Tags:** #aerial_logistics, #autonomous_drones, #cartridge_swap, #battery_management, #wind_safety, #path_planning, #ML_control, #research_project
**Created:** 2026-01-13
**Type:** code-notes

# hmrs_tanker_mule_drone

## Summary

```
Drone system for aerial logistics, specifically designed to autonomously perform cartridge resupply missions by monitoring fluid levels and docking for refueling.
```

## Details

> This module implements a **Tanker Mule Drone** within the HMRS (Hypothetical Multi-Role Systems) framework, focusing on aerial logistics for resupplying climber cartridges. The drone integrates multiple specialized components (e.g., docking systems, path planning, ML-based collision avoidance) to execute missions like monitoring fluid levels and docking autonomously. The system leverages PyBullet for physics simulation and customizable configurations for research-based or default settings.
> 
> The `HMRSTankerMuleDrone` class inherits from `BaseDrone` and initializes with configurable parameters such as drone ID, position, physics client, and optional weather/building systems. It loads a default configuration (`TankerMuleConfig`) if none is provided, and overrides fluid-level thresholds via `fluid_threshold`.

## Key Functions

### ``__init__``

Initializes the drone with physics, mapping, and mission-specific configurations.

### ``config``

Stores drone-specific settings (e.g., fluid thresholds, battery limits) from `TankerMuleConfig`.

### ``building_mapper``

Handles spatial/environmental data (e.g., docking stations, obstacles).

### ``fluid_threshold``

Dynamically adjusts docking criteria based on user input or config defaults.

## Usage

1. **Initialize**: Create an instance with required parameters (e.g., `drone_id`, `position`).
2. **Configure**: Override defaults via `config` or `fluid_threshold`.
3. **Execute Mission**: Call methods from submodules (e.g., `DockingSystemBox.dock()`) to trigger resupply operations.
   Example:
   ```python
   drone = HMRSTankerMuleDrone(drone_id=1, position=(0, 0, 10))
   drone.docking_system_box.dock()  # Swap cartridges autonomously
   ```

## Dependencies

> ``numpy``
> ``PyBullet``
> ``.base_drone``
> ``.building_mapper``
> ``.battery_model``
> ``.boxes/*``
> ``.config.tanker_mule_config``

## Related

- [[`base_drone]]
- [[`building_mapper]]
- [[`tanker_mule_config]]

>[!INFO] **Dynamic Thresholds**
> Fluid level thresholds can be overridden at runtime via `fluid_threshold`, allowing adaptive mission planning (e.g., for low-battery scenarios).

>[!WARNING] **Dependency Risk**
> If `AttentionCollisionAvoidanceBox` is unavailable (e.g., 2025 integration not yet implemented), the drone may lack advanced collision avoidance—test in simulated environments.
