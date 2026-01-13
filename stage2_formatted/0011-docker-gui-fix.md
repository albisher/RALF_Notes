**Tags:** #docker, #headless-mode, #simulation, #gui-fix, #containerization, #x-server, #performance-optimization, #web-visualization
**Created:** 2026-01-13
**Type:** code-notes

# 0011-docker-gui-fix

## Summary

```
Fixes Docker container GUI mode errors by enforcing headless mode for production simulations, improving performance and compatibility.
```

## Details

> This document addresses a Docker container issue where the simulation ran in GUI mode, causing dependency failures on X servers. The root cause was a default command in the Dockerfile and hardcoded GUI settings in `run_simulation.py`. The fix involves:
> 1. Updating the Dockerfile to use `hmrs_simulation_live.py`, a headless service.
> 2. Modifying `run_simulation.py` to detect Docker environments and default to headless mode unless explicitly configured for GUI.

## Key Functions

### ``hmrs_simulation_live.py``

Runs in headless mode with web-based visualization.

### ``run_simulation.py``

Detects Docker environment and defaults to headless mode (`headless=True`).

### `Dockerfile`

Updated `CMD` to use `hmrs_simulation_live.py` instead of `run_simulation.py`.

## Usage

- **Production**: Run `docker compose up -d hmrs-live` to deploy headless mode.
- **Testing**: Use `docker compose run --rm simulator python run_simulation.py` to test headless mode automatically.

## Dependencies

> `- Docker`
> `Docker Compose`
> `Python`
> `PyBullet`
> `PyQt (for GUI fallback if X11 forwarding is active).`

## Related

- [[`0013-docker-troubleshooting]]
- [[0002-docker-se`]]

>[!INFO] Important Note
> The fix ensures compatibility with cloud/CI/CD environments by removing X server dependencies, improving performance by 2-5x, and enabling web-based visualization without GUI overhead.


>[!WARNING] Caution
> If manually testing GUI mode, ensure X11 forwarding (`-v $DISPLAY`) is properly configured in Docker. The script defaults to headless mode in Docker environments.
