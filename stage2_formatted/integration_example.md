**Tags:** #integration, #pybullet, #box_modules, #drone_control, #simulation
**Created:** 2026-01-13
**Type:** code-notes

# integration_example

## Summary

```
Demonstrates integrating drone control and path planning modules into existing PyBullet-based simulations.
```

## Details

> This file provides integration examples for drone control components (`MLControllerBox`, `PathPlannerBox`, etc.) within a PyBullet simulation environment. It shows how to replace legacy controllers with modular "box" implementations while maintaining backward compatibility. The examples cover basic control, path planning, and obstacle avoidance using the same interfaces as original code.

## Key Functions

### ``example_integration_learning_simulator()``

Demonstrates replacing an old ML controller with `MLControllerBox` in a learning simulator, ensuring minimal code changes.

### ``example_integration_worker_drone()``

Illustrates integrating `PathPlannerBox` for path generation in a worker drone, including waypoint navigation.

### ``example_integration_complex_behavior()``

Combines multiple boxes (ML controller, path planner, LiDAR) in a PyBullet simulation to enable obstacle-aware navigation.

## Usage

1. Import the example functions in a script.
2. Call `example_integration_learning_simulator()` for control integration.
3. Call `example_integration_worker_drone()` for path planning.
4. Call `example_integration_complex_behavior()` for full system integration with PyBullet.

## Dependencies

> `numpy`
> `pybullet`
> `pybullet_data`
> ``.boxes` module (local imports)`

## Related

- [[simulation_setup]]
- [[drone_control_architecture]]

>[!INFO] Interface Compatibility
> The box modules (`MLControllerBox`, `PathPlannerBox`) expose identical signatures to legacy code, ensuring seamless integration without API changes.

>[!WARNING] PyBullet Setup
> Ensure `pybullet_data` is properly configured with URDF paths (e.g., `plane.urdf`) to avoid simulation errors. The example uses `DIRECT` mode for simplicity.
