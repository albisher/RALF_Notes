**Tags:** #documentation, #visualization, #simulation, #docker, #tutorial
**Created:** 2026-01-13
**Type:** tutorial

# HOW_TO_RUN

## Summary

```
Guide for running and visualizing a drone exploration simulation with LiDAR data.
```

## Details

> This document provides instructions for executing a drone exploration simulation in Docker and generating a 3D visualization of detected objects, paths, and LiDAR data. It covers three main workflows: running everything in one command, running simulation and visualization separately, or visualizing pre-existing logs. The visualization includes a 3D LiDAR point cloud, drone path, detected objects, and ground truth objects.

## Key Functions

### ``./scenarios/exploration/run_and_visualize.sh``

Orchestrates Docker simulation, log copying, and visualization generation.

### ``scenarios/exploration/simple-exploration/simple_exploration_test.py``

Core simulation script executed via Docker.

### ``scenarios/exploration/visualize_exploration.py``

Generates visualization from log files.

## Usage

1. **Quick Start**: Execute the script from the project root.
2. **Simulation Only**: Run the Dockerized simulation script, then execute visualization separately.
3. **Visualization Only**: Use existing log files to generate visualizations.

## Dependencies

> `- Docker`
> ``docker compose``
> `Python (for visualization scripts).`

## Related

- [[docker-compose]]
- [[visualize_exploration]]

>[!INFO] Important Note
> Ensure the simulation completes successfully before running visualization. Check log files in `scenarios/exploration/visualization/` for errors.

>[!WARNING] Caution
> If logs are missing, verify the simulation ran and check file paths. Empty visualizations may indicate missing LiDAR data or incomplete drone waypoints.
