**Tags:** #simulation, #docker, #robotics, #ml-training, #development, #testing, #visualization, #containerization, #pybullet
**Created:** 2026-01-13
**Type:** code-notes

# 0013-hmrs-simulator-tasks

## Summary

```
A standalone HMRS simulation container for running multi-robot system simulations, ML data generation, and testing without web dependencies.
```

## Details

> The `hmrs-simulator` container is a standalone simulation environment for HMRS (Heterogeneous Multi-Robot System) that supports PyBullet physics simulations, ML training data generation, and custom script execution. It operates independently of the web interface and reuses the same backend image for consistency. The container is configured for manual execution, allowing users to run simulations in headless or GUI modes, generate training datasets, debug logic, and verify system requirements. Key features include full volume access for development, X11 support for GUI applications, and no auto-restart policy.

## Key Functions

### ``run_simulation.py``

Executes standalone PyBullet physics simulations.

### ``run_ml_sessions.py``

Generates ML training data from simulations.

### ``verify_requirements.py``

Checks system and PyBullet installation compatibility.

### ``simple_quadcopter_visual.py``

Runs visual demos with matplotlib.

### `Custom scripts`

Allows execution of user-defined simulation tasks.

## Usage

Run via Docker Compose with:
```bash
docker compose run --rm simulator <script_name.py>
```
Example commands:
- `python run_simulation.py` (standalone execution)
- `python run_ml_sessions.py` (training data generation)
- `bash` (interactive shell for debugging).

## Dependencies

> ``hmrs-backend:latest` (shared image for consistent dependencies)`
> `Docker Compose`
> `PyBullet`
> `Python libraries (e.g.`
> ``matplotlib``
> ``numpy`).`

## Related

- [[hmrs-backend-config]]
- [[pybullet-simulation-guides]]
- [[docker-compose-usage]]

>[!INFO] Manual Execution Required
> The container has no default command; it must be explicitly started using Docker Compose. Always use `--rm` to clean up containers after execution.

>[!WARNING] GUI Mode Dependency
> If running GUI applications (e.g., visualizations), ensure X11 forwarding is enabled in the host environment. The container uses `restart: no` to avoid unintended auto-restarts.
