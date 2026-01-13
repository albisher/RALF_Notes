**Tags:** #visualization, #simulation, #quadcopter, #animation, #saving, #matplotlib, #3d, #data-science
**Created:** 2026-01-13
**Type:** code-notes

# run_visual_save

## Summary

```
Generates and saves 3D quadcopter simulation frames for offline viewing when GUI is unavailable.
```

## Details

> This script creates a non-interactive Matplotlib-based visualization of multiple quadcopters in a 3D environment, updating their positions and heights over time. It records frames to a specified directory for playback, including top-down views, height trajectories, and LiDAR scans. Physics-based thrust calculations adjust each copter’s vertical velocity toward its target height. The demo uses `Agg` backend to render static frames instead of interactive plots.

## Key Functions

### `update_physics(self, dt)`

Computes thrust forces and updates quadcopter positions/velocities based on height error.

### `VisualQuadcopterDemoSave.__init__(self, num_quadcopters, save_dir)`

Initializes quadcopters with predefined positions, sets up Matplotlib subplots, and creates a directory for saved frames.

### ``self.ax_3d`, `self.ax_top`, `self.ax_height`, `self.ax_lidar``

Matplotlib axes for 3D view, top-down projection, height-time plot, and polar LiDAR scan, respectively.

## Usage

1. Instantiate the class: `demo = VisualQuadcopterDemoSave(num_quadcopters=3, save_dir="output")`.
2. Call `update_physics()` in a loop with a time step (e.g., `dt=0.01`) to simulate physics.
3. Frames are saved as PNGs in `save_dir/` (e.g., `output/frame_0001.png`).

## Dependencies

> `numpy`
> `matplotlib`
> `matplotlib.animation`
> `mpl_toolkits.mplot3d`
> `time`
> `os`

## Related

- [[None]]

>[!INFO] Important Note
> The script uses `matplotlib.use('Agg')` to disable interactivity, ensuring frames are saved statically. Adjust `dt` in `update_physics()` for smoother/faster simulations.


>[!WARNING] Caution
> LiDAR plots (`ax_lidar`) are simplified polar plots; actual LiDAR data would require custom plotting logic. Ensure `save_dir` exists or the script will create it.
