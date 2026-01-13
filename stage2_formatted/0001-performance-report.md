**Tags:** #performance, #simulation, #api, #docker, #benchmark, #real-time
**Created:** 2026-01-13
**Type:** documentation

# 0001-performance-report

## Summary

```
Documentation of HMRS simulation system performance metrics, including API response times, simulation configuration, and system architecture.
```

## Details

> This report evaluates the performance of the HMRS simulation system, focusing on API response times, simulation timesteps, and real-time visualization. It highlights that API endpoints are highly responsive (average < 10ms), while simulation performance depends on Docker for accurate testing. Key metrics include a 240 Hz physics timestep, frame caching, and background thread management for smooth operation.

## Key Functions

### ``hmrs_simulation_live.py``

Main simulation controller with Flask web server and real-time physics at 240 Hz.

### ``simulation/test_performance.py``

Benchmarking script for initialization speed, step performance, and API response times.

### `Docker container (`hmrs-live-simulation`)`

Isolated environment with PyBullet, NumPy, and Matplotlib for simulation dependencies.

## Usage

To test performance:
1. Run the simulation in a Docker container.
2. Execute `simulation/test_performance.py` for benchmarking.
3. Monitor API endpoints (`/api/state`, `/api/data`) for real-time responsiveness.

## Dependencies

> `PyBullet`
> `NumPy`
> `Matplotlib`
> `Flask`
> `Docker (for full testing environment).`

## Related

- [[None]]

>[!INFO] Important Note
>API response times are measured in a non-Docker environment and may vary in production due to system overhead. Docker ensures consistent testing.

>[!WARNING] Caution
>Simulation performance degrades if the Docker container lacks sufficient CPU/RAM. Ensure resources meet 240 Hz requirements (e.g., 4+ cores, 8GB+ RAM).
