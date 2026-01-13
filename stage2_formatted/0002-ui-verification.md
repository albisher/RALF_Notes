**Tags:** #ui-testing, #simulation-verification, #web-interface, #live-data-stream, #flask, #pybullet, #matplotlib
**Created:** 2026-01-13
**Type:** test-reference

# 0002-ui-verification

## Summary

```
Verifies the live quadcopter simulation UI, ensuring real-time image streaming and functional components.
```

## Details

> This document confirms the operational status of a live quadcopter simulation web interface hosted on a Flask server. It validates server responsiveness, image stream consistency, and real-time updates via PyBullet physics engine and Matplotlib-generated visualizations. The UI refreshes frames at ~10 FPS, displaying multiple views (3D, top-down, LiDAR, etc.) with active controls and status metrics.

## Key Functions

### ``live-quad-sim` container`

Runs the Flask server and simulation loop.

### ``/stream` endpoint`

Serves PNG frames (~236 KB each) at 10 FPS.

### `Auto-refresh JavaScript`

Updates the simulation image every 100ms.

### `PyBullet physics engine`

Handles quadcopter dynamics.

### `Flask web server`

Exposes the UI and stream endpoint.

### `Matplotlib visualization`

Generates real-time graphs (e.g., LiDAR, velocity).

## Usage

1. Access via `http://localhost:5003` in a browser.
2. Use `curl` commands to verify:
   - Server status (`curl -I http://localhost:5003`).
   - Frame capture (`curl http://localhost:5003/stream -o frame.png`).
   - Container logs (`docker logs live-quad-sim`).
3. Test updates by capturing multiple frames sequentially.

## Dependencies

> `Docker`
> `Flask`
> `PyBullet`
> `Matplotlib`
> `Python (3.x)`
> ``curl`/`docker` CLI tools.`

## Related

- [[0001-deployment-check]]
- [[0003-performance-tuning]]

>[!INFO] Important Note
> The simulation updates at **~10 FPS**, but refreshes every **100ms** (due to JavaScript). For smoothness, ensure browser refresh rate aligns with frame rate.

>[!WARNING] Caution
> If the container crashes, restart with `docker restart live-quad-sim`. Inactive containers may fail to stream frames. Verify PID 1 (main process) remains active.
