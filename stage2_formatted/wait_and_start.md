**Tags:** #Bash, #Docker, #Containerization, #Automation, #ServiceStartup
**Created:** 2026-01-13
**Type:** code-notes

# wait_and_start

## Summary

```
Script to wait for Docker to initialize, stop existing containers, and start Docker Compose services with health checks.
```

## Details

> This script automates the process of waiting for Docker to be ready, stopping any existing containers, and launching Docker Compose services. It includes a timeout mechanism for Docker initialization and checks if a health endpoint is responsive after service startup. The script uses relative paths to locate directories and performs cleanup before deployment.

## Key Functions

### `Docker readiness check`

Polls `docker info` until Docker is operational or a timeout occurs.

### `Container cleanup`

Stops and removes existing containers defined in `docker/docker-compose.yml`.

### `Service startup`

Runs `docker compose` with background mode (`-d`) and rebuilds images if specified (`--build`).

### `Health check`

Verifies if a health endpoint (`http://localhost:5007/api/health`) is accessible after initialization.

### `Logging and status`

Displays service status and provides useful commands for further debugging.

## Usage

1. Save the script as `wait_and_start`.
2. Run it in the directory where it is located (or modify paths to `SCRIPT_DIR` and `SIMULATION_DIR`).
3. The script will:
   - Wait for Docker to start (max 60 seconds).
   - Stop and remove existing containers.
   - Start new services with `docker-compose`.
   - Check if a health endpoint is responsive.
   - Provide useful commands for managing services.

## Dependencies

> `Docker CLI`
> ``curl``
> `Bash shell.`

## Related

- [[none]]

>[!INFO] Important Note
> Ensure Docker Desktop is running before executing this script. If Docker fails to start within 60 seconds, manually start Docker Desktop and retry.


>[!WARNING] Caution
> If the health endpoint (`/api/health`) is not immediately available, check logs with `docker compose logs -f backend` for startup errors. Avoid interrupting the script mid-execution.
