**Tags:** #visualization, #simulation, #quadcopters, #matplotlib, #LiDAR, #Docker, #3D_visualization, #flight_simulation, #top-down_view, #altitude_graph
**Created:** 2026-01-13
**Type:** tutorial

# VISUAL_SIMULATION

## Summary

```
Guide for running and interpreting a quadcopter flight simulation with interactive 3D/2D views, LiDAR scans, and height tracking.
```

## Details

> This guide provides instructions for executing a visual simulation of quadcopters, featuring interactive GUI modes (3D/2D views) and frame-saving capabilities. The simulation includes real-time position updates, trajectory visualization, and LiDAR obstacle detection. The workflow involves running Python scripts in either local or Docker environments, with fallback options for GUI failures.

## Key Functions

### ``run_visual_demo.py``

Opens an interactive matplotlib GUI with 3D/2D views, height graph, and LiDAR scans.

### ``run_visual_save.py``

Saves simulation frames to `simulation_output/` for offline viewing.

### ``run_visual.sh``

Convenience script that auto-selects GUI or save mode.

### ``simulation_output/``

Directory storing saved frames (PNGs) for visualization.

## Usage

1. **Local GUI**: Run `python run_visual_demo.py` after activating a virtual environment.
2. **Save Frames**: Use `python run_visual_save.py` (works locally or in Docker).
3. **Convenience Script**: Execute `./run_visual.sh` for automated execution.

## Dependencies

> `matplotlib`
> `Docker (optional)`
> `Python 3.x`

## Related

- [[Visual_Simulation_Setup]]
- [[Quadcopter_Sensor_Simulation]]

>[!INFO] **GUI Requirements**
> Ensure matplotlib is installed (`pip install matplotlib`) and run locally (not Docker) for GUI to work on macOS.

>[!WARNING] **Docker Permissions**
> If frames fail to save in Docker, check directory permissions (`mkdir -p simulation_output`) and ensure `simulation_output/` exists.
