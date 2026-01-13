**Tags:** #docker, #containerization, #ml-ui, #simulation, #no-local-server
**Created:** 2026-01-13
**Type:** documentation

# README_DOCKER

## Summary

```
Documentation for Docker-based containerized setup for ML scenario UI and simulation services, emphasizing no local server dependencies.
```

## Details

> This `README_DOCKER` provides instructions for deploying a **Dockerized** ML scenario UI and simulation stack without running any local server. It outlines two deployment modes: a standalone ML UI and a full-stack simulator + ML UI setup. The documentation details container configurations, ports, networks, and troubleshooting steps for common issues like port conflicts or failed container starts. It also explains data persistence via Docker volumes and network isolation between services.

## Key Functions

### ``docker-run-ml-ui.sh``

Script to start the standalone ML UI container.

### ``docker-compose.ml-ui.yml``

Configuration file for the standalone ML UI container.

### ``docker-compose.yml``

Full-stack configuration for simulator + ML UI.

### ``ml-scenario-ui``

Container running the ML scenario UI (port `5006`).

### ``hmrs-simulator``

Container running the HMRS simulation environment.

### ``ml-scenario-data``

Docker volume storing scenario data (`/app/data/ml_scenarios.json`).

## Usage

1. **Standalone ML UI**:
   - Navigate to `simulation` directory and run:
     ```bash
     ./docker-run-ml-ui.sh
     ```
     or manually:
     ```bash
     docker-compose -f docker-compose.ml-ui.yml up -d
     ```
   - Access UI at `http://localhost:5006`.

2. **Full Stack**:
   - Run:
     ```bash
     cd simulation && docker-compose up -d
     ```
   - Services (`ml-scenario-ui`, `simulator`) are isolated on `simulation-network`.

## Dependencies

> `Docker Engine`
> `Docker Compose`
> `Python (for ML UI if not containerized separately).`

## Related

- [[DOCKERFILE]]
- [[docker-compose]]
- [[docker-compose.ml-ui]]
- [[DOCKER_ML_SCENARIO_UI]]

>[!INFO] Important Note
> All services run in Docker containers. Ensure Docker and Docker Compose are installed and running before deployment. Use `docker ps` to verify containers are active.


>[!WARNING] Caution
> If port `5006` is occupied by a local process, stop it first (`pkill -f "python.*ml_scenario_ui"`). Rebuild containers if errors persist (`docker-compose build --no-cache`).
