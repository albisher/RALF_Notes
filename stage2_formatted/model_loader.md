**Tags:** #3D-modeling, #pybullet, #simulation, #robotics, #visualization
**Created:** 2026-01-13
**Type:** code-notes

# model_loader

## Summary

```
Loads and creates detailed 3D models for drones, vehicles, and structures in a physics simulation environment.
```

## Details

> This module (`model_loader`) initializes a class (`ModelLoader`) to create visually enhanced 3D representations of drones, vehicles, and buildings using PyBullet. It provides composite shapes (e.g., quadcopters with propellers) instead of basic cubes, improving realism. The class handles initialization, model creation, and configuration for simulation elements like drones, trucks, and buildings.
> 
> The implementation uses PyBullet’s `createMultiBody` to assemble complex shapes, with collision and visual components defined separately. Propellers, for example, are added as semi-transparent visual shapes positioned relative to the drone’s body.

## Key Functions

### `create_quadcopter_drone`

Creates a quadcopter drone with a body and four propellers, configurable via position, orientation, color, and scale.

### `ModelLoader.__init__`

Initializes the loader with a PyBullet physics client ID and sets up a directory for model storage.

## Usage

```python
# Initialize the loader
loader = ModelLoader(physics_client_id)

# Create a drone at (0, 0, 0) with default orientation and color
drone_id = loader.create_quadcopter_drone((0, 0, 0))
```

## Dependencies

> `pybullet`
> `numpy`
> `os`

## Related

- [[None]]

>[!INFO] Important Note
> The `propeller_o` variable in the snippet appears to be a typo (likely meant `propeller_offsets`). Ensure correct variable names are used to avoid runtime errors.


>[!WARNING] Caution
> Avoid scaling values too large/small, as extreme values may cause numerical instability or collision issues in PyBullet. Default scale (1.0) is recommended for testing.
