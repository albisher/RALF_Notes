**Tags:** #3d-visualization, #camera-controls, #zoom-management, #numerical-algorithms
**Created:** 2026-01-13
**Type:** code-notes

# zoom_box

## Summary

```
Manages zoom operations for 3D camera state adjustments with bounds and speed controls.
```

## Details

> The `ZoomBox` class implements a single-responsibility zoom system for 3D visualization. It calculates zoom levels from camera coordinates (eye, center, up vectors) and applies directional zoom adjustments while enforcing minimum/maximum zoom limits. The core logic computes zoom ratios by comparing distances between camera positions and a fixed reference point (`baseEye`), then adjusts the camera’s `eye` coordinates proportionally based on `zoom_direction` (in/out).

## Key Functions

### ``__init__(min_zoom, max_zoom, zoom_speed)``

Initializes zoom bounds and increment speed.

### ``calculate_zoom_from_camera(camera_state)``

Derives zoom level from camera state coordinates, returning a ratio (1.0 = default, >1.0 = zoomed in).

### ``apply_zoom(camera_state, zoom_direction, zoom_to_point)``

Adjusts camera state by scaling distances toward/from a target point (if provided) or default center, respecting bounds.

## Usage

1. Instantiate `ZoomBox` with desired bounds and speed.
2. Call `calculate_zoom_from_camera()` to compute current zoom level.
3. Use `apply_zoom()` to update camera state with `zoom_direction` (e.g., `"in"` or `"out"`).

## Dependencies

> `numpy`
> `typing`

## Related

- [[None]]

>[!INFO] Distance Handling
> Avoids division-by-zero by clamping `current_distance` to `2.6` if zero (arbitrary fallback).

>[!WARNING] Input Validation
> Returns `1.0` for invalid camera_state (e.g., missing keys) to prevent crashes.
