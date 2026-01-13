**Tags:** #drone-swarm, #physics-simulation, #pybullet, #swarm-control, #base-class
**Created:** 2026-01-13
**Type:** code-notes

# base_drone

## Summary

```
Core drone class for swarm physics and state management in PyBullet.
```

## Details

> This `BaseDrone` class encapsulates common functionality for all drone types within a swarm, including physics integration via PyBullet, spatial state tracking, and optional motion patterns. It handles initialization with configurable parameters like drone ID, position, and base reference point while supporting weather effects and ROS 2 interfacing. The class abstracts core behaviors like position updates and return-to-base operations, enabling modular extension for specialized drone behaviors.

## Key Functions

### ``__init__``

Initializes drone physics, state, and optional components (motion patterns, ROS 2, weather systems).

### ``self.position``

Tracks current (x,y,z) coordinates as a NumPy array.

### ``self.base_position``

Stores home/return position with optional timestamping (default: [0,0,0]).

### ``self.motion_pattern``

Optional subclassed pattern for flight dynamics (e.g., circular, linear).

### ``self.weather_system``

Handles wind/atmospheric effects (if provided).

## Usage

1. Subclass `BaseDrone` to define drone-specific behaviors.
2. Pass required args: `drone_id`, `position`, `physics_client`.
3. Optionally configure `motion_pattern`, `base_position`, or `enable_ros2`.
4. Extend methods like `update_position()` or `execute_motion()` in derived classes.

## Dependencies

> `pybullet`
> `numpy`
> `logging`
> `datetime`
> ``from .boxes.logging_box``
> ``from .motion_patterns.base_motion_pattern``
> ``from .boxes.ros2_interface_box` (if enabled).`

## Related

- [[swarm_controller]]
- [[drone_motion_patterns]]
- [[logging_system]]

>[!INFO] Logging Box
> If `.boxes.logging_box` fails to import, `LOGGING_BOX_AVAILABLE` defaults to `False`, and `LoggingBox` becomes `None`. This gracefully skips logging features.

>[!WARNING] ROS 2 Dependency
> ROS 2 interface (`ROS2InterfaceBox`) requires `rclpy`; missing it triggers a warning but does not crash the drone. Always check `self.ros2_box` for availability.
