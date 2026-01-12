**Tags:** #refactoring, #autonomous_exploration, #code_reorganization, #reusable_components, #lidar_simulation, #visualization, #data_logging, #path_planning
**Created:** 2026-01-12
**Type:** code-notes

# simulation_swarm_boxes

## Summary

```
Centralized refactored autonomous exploration simulation components with reusable boxes for sensor data, visualization, and path planning.
```

## Details

> This refactoring consolidates critical autonomous exploration modules into modular "Boxes" across the simulation swarm system. The codebase was restructured to eliminate redundant logic, improve maintainability, and enable global reuse of core functionalities like LiDAR scanning, path planning, and visualization. Each box encapsulates specific responsibilities (e.g., sensor data processing, state management) while supporting configurable presets and batch operations for performance optimization.
> 
> The refactored system organizes components into a unified architecture where previously scattered logic (e.g., in `scenarios/exploration/simple-exploration/`) is now centralized in `simulation/swarm/boxes/`. This reduces duplication by ~850 lines of code and enables modular testing and integration.

## Key Functions

### `LiDARScannerBox`

Handles real-world sensor simulations (VLP-16/VLP-32/HDL-64) with configurable FOV, noise, and ray casting.

### `VisualizationBox`

Provides dual backend support (Plotly/Matplotlib) for 2D/3D visualization with configurable styles and quad views.

### `GroundTruthLoggerBox`

Logs object states (hidden from C&C) in JSON format for statistical analysis.

### `BaseStationBox`

Manages telemetry, point cloud accumulation, and export of simulation statistics.

### `ScenarioUtilsBox`

Generates random objects, PyBullet spawn configurations, and building presets.

### `ExplorationEnhancementBox`

Implements frontier-based waypoint generation for autonomous exploration.

### `PathPlannerBox`

Safely plans paths with obstacle avoidance, now reusable globally.

### `LearningSystemBox`

Accumulates knowledge from simulations for future decision-making.

### `ExplorationManagerBox`

Consolidated state handlers (`_handle_idle_state`, `_handle_scanning_state`, `_handle_moving_state`) into modular methods for cleaner `update()` logic.

## Usage

To use these refactored boxes:
1. Import the box (e.g., `from simulation.swarm.boxes import LiDARScannerBox`).
2. Configure sensor/visualization parameters via box-specific attributes.
3. Integrate into the simulation loop by calling box methods (e.g., `box.update()`).
4. For global reuse, replace legacy components with these modular boxes (e.g., `ExplorationManagerBox` or `PathPlannerBox`).

## Dependencies

> `Plotly`
> `Matplotlib`
> `PyBullet`
> `JSON libraries (standard Python libraries)`
> `custom simulation utilities.`

## Related

- [[simulation_swarm_architecture]]
- [[exploration_scenario_guide]]

>[!INFO] Key Benefit
> The modular design allows independent testing of each box (e.g., LiDARScannerBox can be validated without the full simulation swarm).

>[!WARNING] Dependency Risk
> Ensure Plotly/Matplotlib are installed for visualization backends. If using custom PyBullet versions, verify compatibility with the refactored `ScenarioUtilsBox`.
