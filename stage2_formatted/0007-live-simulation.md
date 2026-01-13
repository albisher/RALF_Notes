**Tags:** #real-time, #web-interface, #simulation, #docker, #pybullet, #quadcopter, #flask, #live-updates
**Created:** 2026-01-13
**Type:** code-notes

# 0007-live-simulation

## Summary

```
A Docker-based live simulation system for real-time quadcopter visualization using PyBullet physics and a Flask web server.
```

## Details

> This system runs a PyBullet physics engine in a Docker container to simulate quadcopters, then streams the simulation frames via a Flask web server accessible through a browser. The web interface provides a 6-panel dashboard (3D view, top view, height graph, LiDAR scan, velocity graph, and info panel) for live monitoring of the simulation. The simulation updates at approximately 10 frames per second, with the browser refreshing the display every 100ms to maintain real-time visualization.

## Key Functions

### ``docker compose run --rm -p 5000`

5000 simulator python simple_quadcopter_live.py`**: Starts the simulation container with Flask running on port 5000.

### ``simple_quadcopter_live.py``

Main script containing PyBullet simulation logic and Flask web server setup to stream frames.

### `Flask web server`

Handles rendering and streaming live frames to the browser.

### `PyBullet physics engine`

Runs in a background thread to generate simulation frames (~10 FPS).

## Usage

1. Run the command in the terminal to start the simulation container.
2. Open a browser and navigate to `http://localhost:5000`.
3. Monitor the live quadcopter simulation dashboard.

## Dependencies

> `Docker`
> `PyBullet`
> `Flask`
> `Docker Compose.`

## Related

- [[PyBullet Documentation]]
- [[Flask Web Framework Guide]]
- [[Docker Compose Guide]]

>[!INFO] Important Note
> Ensure Docker is running before executing the command. If Docker is not running, the simulation will fail to start.

>[!WARNING] Caution
> If port 5000 is already in use, change the host port (e.g., `-p 5001:5000`) to avoid conflicts. Access the simulation at the new port (e.g., `http://localhost:5001`).
