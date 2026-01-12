**Tags:** #live-testing, #docker, #system-validation, #backend-api, #simulation, #drone-spawning
**Created:** 2026-01-12
**Type:** test-reference

# system-validation-results

## Summary

```
Validates system operational status post-Docker startup, including container health, backend API, simulation state, and drone functionality.
```

## Details

> This document records live system validation results after Docker containers were started, confirming core functionality. Tests verify container startup, health checks, backend API responsiveness, simulation state persistence, and drone spawning. Minor issues (e.g., command logging bug) are noted but deemed non-critical.

## Key Functions

### `Docker Compose Startup`

Launches all required containers (`hmrs-session-db`, `hmrs-backend`, `hmrs-frontend`, `hmrs-simulator`).

### `Health Check API`

Validates backend API status via `/api/health` endpoint.

### `Simulation State API`

Retrieves loaded buildings and base position via `/api/state`.

### `Drone Spawning API`

Spawns drones (e.g., scout) with customizable positions via POST `/api/spawn`.

## Usage

1. Run `docker compose up -d` to start containers.
2. Execute health checks via `curl` to verify system state.
3. Use `/api/state` to inspect simulation data (e.g., buildings).
4. Spawn drones via `/api/spawn` with JSON payloads.

## Dependencies

> `Docker`
> ``docker-compose``
> ``curl``
> `HTTP client libraries (for API calls).`

## Related

- [[Docker Compose Configuration]]
- [[Backend API Documentation]]
- [[Simulation State Schema]]

>[!INFO] Important Note
> Minor command logging bug exists but does not impact core functionality. System remains operational with no critical failures.

>[!WARNING] Caution
> Ensure `localhost:5007` is accessible; port conflicts may arise if other services use the same port.
