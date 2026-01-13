**Tags:** #RTK, #GPS, #Drones, #Precision, #Positioning, #Numpy, #Real-Time, #Navigation
**Created:** 2026-01-13
**Type:** code-notes

# gps_tracker

## Summary

```
A centimeter-accurate RTK GPS tracker for drone navigation with relative/absolute position tracking.
```

## Details

> The `GPSTracker` class implements an RTK (Real-Time Kinematic) GPS system for drones, supporting centimeter-level precision (default: 0.01m). It tracks absolute and relative positions, velocity history, and status flags (e.g., `NO_FIX`, `RTK_FIX`). The system relies on a base station for relative positioning and simulates GPS noise to mimic accuracy constraints. Key features include HDOP monitoring and multi-satellite tracking, aligning with specifications for CUAV C-RTK or Here+ V2.

## Key Functions

### ``__init__(initial_position, base_position=None, accuracy=0.01)``

Initializes tracker with absolute/relative positions, accuracy threshold, and status flags.

### ``update_base_position(base_position)``

Updates the base station’s position, recalculating relative offsets.

### ``update_position(true_position, velocity)``

Simulates GPS updates with noise, storing absolute positions and velocities in history.

## Usage

```python
tracker = GPSTracker(initial_position=[0.0, 0.0, 0.0], base_position=[10.0, 10.0, 0.0])
tracker.update_position(np.array([1.0, 1.0, 0.0]), np.array([0.5, 0.5, 0.0]))
```

## Dependencies

> `numpy`
> `time`

## Related

- [[RTK_GPS_Specs]]
- [[Drone_Navigation_Architecture]]

>[!INFO] Missing Noise Function
> The `update_position` method references `no` (undefined variable) instead of `noise` (defined as `np.random.normal`).

>[!WARNING] Hardcoded Defaults
> Accuracy (1cm) and base position (0.0) are hardcoded; real-world use should pass dynamic values.
