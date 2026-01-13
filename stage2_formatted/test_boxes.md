**Tags:** #unit-test, #swarm-robotics, #ml-controller, #path-planning
**Created:** 2026-01-13
**Type:** code-notes

# test_boxes

## Summary

```
Unit tests for Box modules in a swarm robotics system, validating initialization, ML control, path planning, LiDAR, and camera processing.
```

## Details

> This file contains unit tests for `Boxes` components in a swarm robotics system, specifically `MLControllerBox`, `PathPlannerBox`, `LiDARProcessorBox`, and `CameraProcessorBox`. Tests verify initialization, neural network forward passes, control computations, weight updates, and file I/O for `MLControllerBox`. `PathPlannerBox` tests cover configuration and waypoint logic. The tests use NumPy for numerical validation and temporary files for serialization.

## Key Functions

### `MLControllerBox.test_initialization`

Validates constructor parameters (`input_size`, `hidden_size`, `output_size`).

### `MLControllerBox.test_forward_pass`

Ensures neural network outputs 4 normalized values (0–1) for a random input.

### `MLControllerBox.test_compute_control`

Checks control thrust computation (4 outputs) with simulated inputs (position, velocity, orientation, target, wind).

### `MLControllerBox.test_update_weights`

Confirms weight updates do not raise exceptions.

### `MLControllerBox.test_save_load`

Validates serialization/deserialization of weights via temporary file.

### `PathPlannerBox.test_initialization`

Confirms `max_waypoint_distance` and `obstacle_clearance` settings.

## Usage

Run via Python command: `python -m unittest test_boxes`. Tests are organized per box class, with `setUp` initializing fixtures.

## Dependencies

> `unittest`
> `numpy`
> `swarm.boxes (local module)`

## Related

- [[boxes]]
- [[box_tests]]

>[!INFO] Test File Scope
> Tests focus on isolated Box components; no external swarm dependencies are tested here.

>[!WARNING] Temp File Cleanup
> Manual cleanup of temporary files is handled in `test_save_load` via `finally` block.
