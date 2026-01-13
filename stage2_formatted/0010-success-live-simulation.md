**Tags:** #verification, #live-simulation, #flask, #pybullet, #docker, #real-time, #visualization
**Created:** 2026-01-13
**Type:** documentation

# 0010-success-live-simulation

## Summary

```
Confirms successful live simulation setup with real-time visualization and Dockerized Flask server.
```

## Details

> This document confirms a working live simulation environment using a Flask web server running in Docker, integrated with a PyBullet physics engine. The system streams live simulation frames (~10 FPS) via HTTP to a browser, which auto-refreshes every 100ms to display real-time updates across six visualization panels (3D, top view, height/velocity data, LiDAR, etc.). The setup includes containerized execution, port mapping, and dynamic sensor/physics data rendering.

## Key Functions

### `Flask web server`

Hosts live simulation frames via Docker container (`live-quad-sim`).

### `PyBullet physics engine`

Runs in a background thread to generate simulation frames.

### `HTTP streaming`

Serves PNG images (~1573x990px) at 10 FPS via port 5003 (host:container 5001).

### `Auto-refresh browser`

Updates visualization panels every 100ms for real-time feedback.

## Usage

1. Access `http://localhost:5003` in a browser.
2. Monitor live quadcopter movement and sensor data across six panels.
3. Use for HMRS development by integrating real-time metrics into applications.

## Dependencies

> `Flask`
> `PyBullet`
> `Docker`
> `HTTP server (for streaming)`
> `browser (for visualization).`

## Related

- [[Live Simulation Codebase]]
- [[Flask Docker Setup Guide]]
- [[PyBullet Physics Engine Docs]]

>[!INFO] Important Note
> **Container Port Mapping**: Ensure port 5003 on host matches container port 5001 (e.g., `docker run -p 5003:5001`).
>

>[!WARNING] Caution
> **FPS Dependency**: Frame rate (~10 FPS) may vary; test under load conditions to avoid latency issues.
