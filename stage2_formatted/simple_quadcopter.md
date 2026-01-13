**Tags:** #pybullet, #quadcopter, #simulation, #robotics, #physics, #hmsr, #multi-robot
**Created:** 2026-01-13
**Type:** code-notes

# simple_quadcopter

## Summary

```
Simulates a quadcopter for verifying HMRS system requirements using PyBullet.
```

## Details

> This code implements a basic quadcopter simulator leveraging PyBullet, a physics engine. It supports multi-robot coordination, sensor simulation, real-time physics, and headless operation for performance. The simulator initializes a physics server, loads a ground plane, and allows creation of multiple quadcopters with configurable positions and orientations. Each quadcopter is modeled as a box with adjustable mass and inertia, though URDF-based models can be replaced later.

## Key Functions

### ``QuadcopterSimulator.__init__``

Initializes the physics server, configures gravity, time-step, and loads a ground plane. Supports headless or GUI modes.

### ``create_quadcopter``

Creates a quadcopter in the simulation using a simple box model, sets mass, and stores its ID, position, and orientation.

### ``get_quadcopter_state``

Retrieves the current state (position, orientation, velocity) of a specified quadcopter.

## Usage

1. Instantiate `QuadcopterSimulator` with desired settings (e.g., `headless=True` for performance).
2. Use `create_quadcopter` to spawn quadcopters at specified positions.
3. Query state with `get_quadcopter_state` to monitor their dynamics.

## Dependencies

> `pybullet`
> `pybullet_data`
> `numpy`
> `time`

## Related

- [[none]]

>[!INFO] Physics Server Connection
> The simulator connects to PyBullet in headless mode (`DIRECT`) for maximum performance, or GUI mode (`GUI`) for visualization. Always ensure PyBullet is installed and the URDF files (`plane.urdf`, `cube.urdf`) are accessible via `pybullet_data.getDataPath()`.

>[!WARNING] Mass and Inertia Approximation
> The quadcopter is modeled as a box with a fixed mass (1.5 kg). For realistic simulations, replace the box with a URDF model (e.g., a quadcopter-specific URDF) and adjust mass/inertia properties dynamically.
