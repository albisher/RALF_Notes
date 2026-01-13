**Tags:** #matplotlib, #data-visualization, #log-analysis, #3d-coordinates, #waypoint-plotting
**Created:** 2026-01-13
**Type:** code-notes

# visualize_logs

## Summary

```
Visualizes LiDAR log data with drone waypoints and object positions using Matplotlib.
```

## Details

> This script loads predefined log data (object positions and labels) alongside a drone’s waypoint path, plotting them on a 2D coordinate plane. The `ground_truth` array contains objects (e.g., "Cube," "Sphere") with XY coordinates, while `waypoints` defines the drone’s trajectory. The visualization uses scatter plots for objects (distinguished by shape/marker) and a red dashed line for the path, with grid and legend for clarity.

## Key Functions

### ``plt.scatter()``

Renders object positions with custom markers (squares for "Cube," circles for "Sphere").

### ``zip(*waypoints)``

Extracts X/Y coordinates from `waypoints` for plotting the drone path.

### ``plt.plot()``

Draws the drone’s trajectory as a red dashed line with markers.

## Usage

1. Replace `ground_truth` and `waypoints` with actual log data.
2. Run the script to generate an interactive plot showing object locations and drone path.

## Dependencies

> `matplotlib`
> `numpy`
> `json`

## Related

- [[none]]

>[!INFO] Important Note
> The script assumes 2D coordinates; extend `ground_truth` with Z-values if 3D data is present.

>[!WARNING] Caution
> Hardcoded waypoints may not reflect real-world mission paths. Validate against actual sensor data.
