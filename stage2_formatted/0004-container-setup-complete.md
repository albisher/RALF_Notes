**Tags:** #docker, #containerization, #ml-scenario-ui, #deployment, #docker-compose, #flask, #python, #microservices
**Created:** 2026-01-13
**Type:** documentation

# 0004-container-setup-complete

## Summary

```
Documentation for containerizing ML scenario UI services using Docker, ensuring no local server dependencies.
```

## Details

> This file documents the completion of containerizing all services, replacing local Python/Flask servers with Docker containers. Key changes include:
> - Configuring `docker-compose.ml-ui.yml` for an isolated ML UI container with health checks and persistent volumes.
> - Updating `docker-compose.yml` to integrate the ML UI service into the existing `simulation-network`.
> - Modifying the `Dockerfile` to include health checks and production-ready configurations.
> - Updating `ml_scenario_ui.py` to dynamically read environment variables for port/host instead of hardcoding local references.
> 
> The setup includes a startup script (`docker-run-ml-ui.sh`) and detailed documentation for deployment, access, and troubleshooting.

## Key Functions

### ``docker-compose.ml-ui.yml``

Defines a standalone ML UI container with isolated networking and persistent volumes.

### ``ml_scenario_ui.py``

Containerized Flask application reading environment variables for port/host and logging.

### ``docker-run-ml-ui.sh``

Bash script to start the ML UI container using either the script or `docker-compose`.

### ``docker-compose.yml``

Main compose file integrating the ML UI service into the existing network.

## Usage

1. Navigate to the `simulation` directory.
2. Run either:
   - `./docker-run-ml-ui.sh` (preferred script method),
   - or `docker-compose -f docker-compose.ml-ui.yml up -d` (direct compose command).
3. Access the UI at `http://localhost:5006`.
4. Use `docker logs -f ml-scenario-ui` to view logs and `docker-compose down` to stop the container.

## Dependencies

> `Docker`
> `Docker Compose`
> `Python (for Flask)`
> ``curl` (for health checks and testing).`

## Related

- [[0007-docker-ml-scenario-ui]]
- [[0001-docker-readme]]
- [[0004-container-setup-complete]]
- [[0001-docker-readme]]

>[!INFO] Important Note
> **No Local Server**: The application runs entirely within Docker containers, eliminating the need for a local Python/Flask instance. Environment variables (`FLASK_PORT`, `FLASK_HOST`) dynamically configure the containerized Flask app.


>[!WARNING] Caution
> **Port Conflicts**: Ensure port `5006` is free before running the container. Use `lsof -i :5006` to check for conflicts and `pkill` to terminate conflicting processes if necessary.
