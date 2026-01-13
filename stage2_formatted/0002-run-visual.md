**Tags:** #docker, #simulation, #quadcopter, #pybullet, #visualization, #physics, #data-visualization, #multirotor, #aerial-robotics, #obstacle-avoidance
**Created:** 2026-01-13
**Type:** code-notes

# 0002-run-visual

## Summary

```
Runs a PyBullet physics simulation with quadcopters in Docker, generating visual frames and metrics for analysis.
```

## Details

> This script orchestrates a Docker-based simulation of quadcopters using PyBullet, producing a 6-panel visualization (3D view, top view, height/velocity plots, LiDAR scan) and saving frames at 0.1-second intervals. The simulation logs quadcopter positions, LiDAR data, and metrics, with results stored in a `simulation_output/` directory. The workflow includes running the simulation via `docker compose` and viewing saved frames (e.g., `frame_0000.png` to `frame_0050.png`).

## Key Functions

### ``docker compose run --rm simulator python simple_quadcopter_visual.py``

Executes the simulation container, triggering PyBullet physics and visual rendering.

### ``simple_quadcopter_visual.py``

Core script defining quadcopter behavior, simulation logic, and visualization parameters (e.g., frame save interval, LiDAR channels).

### ``PyBullet``

Physics engine handling quadcopter dynamics and collision detection.

### ``simulation_output/``

Directory storing generated PNG frames and metadata logs.

## Usage

1. Ensure Docker and Docker Compose are installed.
2. Run the command:
   ```bash
   docker compose run --rm simulator python simple_quadcopter_visual.py
   ```
3. View results in `simulation_output/` (e.g., `open simulation_output/frame_0050.png`).

## Dependencies

> `PyBullet`
> `Docker Compose`
> `Python 3.x (with PyBullet and OpenGL libraries).`

## Related

- [[0001-run-physics]]
- [[0003-post-process-data]]

>[!INFO] Important Note
> The simulation duration defaults to 5 seconds (50 frames at 0.1s intervals). Adjust `simple_quadcopter_visual.py` to extend/delay the run or modify frame intervals (e.g., `frame_interval=0.2`).

>[!WARNING] Caution
> LiDAR range in the example is hardcoded to 100m. For real-world use, dynamically update this value or implement adaptive scanning logic to avoid false positives in obstacle detection.
