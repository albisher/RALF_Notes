**Tags:** #docker, #server-management, #restart-procedure, #api-endpoints, #simulation
**Created:** 2026-01-13
**Type:** documentation

# 0017-server-restart-instructions

## Summary

```
Instructions for restarting a Dockerized server simulation, including Docker Compose, manual scripts, and verification steps.
```

## Details

> This document provides detailed restart procedures for a server running on port 5007, which is currently down. It outlines three methods: **Docker Compose** (recommended), a **start script**, and **manual execution** via Python. After restarting, users must verify API endpoints via route checks or Python tests. Expected console output confirms successful initialization and registered routes. Quick test commands demonstrate interaction with key endpoints (session selection, replay, and health checks).

## Key Functions

### ``docker compose up -d hmrs-live``

Starts the server using Docker Compose.

### ``docker compose restart hmrs-live``

Restarts the containerized server.

### ``docker compose logs -f hmrs-live``

Displays real-time logs of the container.

### ``./start_server.sh``

Executes a preconfigured script to start the server manually.

### ``python hmrs_simulation_live.py``

Runs the server directly from the command line.

### ``./verify_routes_after_restart.sh``

Validates API endpoints post-restart.

### ``python3 test_session_endpoints.py``

Automated Python test for session routes.

### ``curl` commands`

Test endpoints interactively (e.g., session selection/replay).

## Usage

1. Navigate to the `simulation` directory.
2. Choose a method (Docker Compose, script, or manual Python).
3. Restart the server and verify endpoints using provided commands.
4. Troubleshoot conflicts (e.g., port 5007) or missing dependencies.

## Dependencies

> `Docker`
> `Docker Compose`
> `Python 3`
> ``curl``
> `virtual environment (if manual start is used).`

## Related

- [[Dockerfile for `hmrs-live`]]
- [[`simulation` directory structure]]
- [[`hmrs_simulation_live]]

>[!INFO] Expected Output Confirmation
> Verify the console output matches:
> ```
> ✅ HMRS Live Simulation initialized (port: 5007)
> ✅ Session select route registered
> ✅ Session replay route registered
> ```
> If missing, check route registration or container logs.


>[!WARNING] Port Conflict Risk
> If port 5007 is already in use, **stop conflicting processes** (e.g., `lsof -i :5007`) or modify the server’s port binding in `docker-compose.yml`.
