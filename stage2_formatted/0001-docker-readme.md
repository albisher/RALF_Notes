**Tags:** #docker, #containerization, #ml-ui, #simulation, #no-local-server, #docker-compose, #heterogeneous-robot-systems
**Created:** 2026-01-13
**Type:** documentation

# 0001-docker-readme

## Summary

```
Documentation for Docker containerized setup for ML scenario UI and simulation services, emphasizing no local server dependency.
```

## Details

> This README outlines how to deploy a Docker-based system for ML scenario UI and simulation services without running any local servers. It provides instructions for both standalone ML UI and full-stack (simulator + ML UI) deployments using Docker Compose. The setup ensures all components run in isolated containers, with defined ports, networks, and data persistence volumes.

## Key Functions

### ``docker-run-ml-ui.sh``

Script to start the standalone ML scenario UI container.

### ``docker-compose.ml-ui.yml``

Configuration file for the standalone ML UI container.

### ``docker-compose.yml``

Configuration file for the full-stack (simulator + ML UI) setup.

### ``ml-scenario-ui``

Container for the ML scenario selection and tracking UI.

### ``hmrs-simulator``

Container for the HMRS (Heterogeneous Multi-Robot System) simulation environment.

### ``ml-scenario-data``

Docker volume storing scenario data in `/app/data/ml_scenarios.json`.

## Usage

1. **Standalone ML UI**:
   - Navigate to the `simulation` directory and run `./docker-run-ml-ui.sh` or `docker-compose -f docker-compose.ml-ui.yml up -d`.
   - Access the UI at `http://localhost:5006`.

2. **Full Stack**:
   - Navigate to the `simulation` directory and run `docker-compose up -d`.
   - Services (`ml-scenario-ui` and `hmrs-simulator`) will start on their respective networks.

## Dependencies

> `Docker`
> `Docker Compose`
> `Python (for ML UI if running locally during troubleshooting).`

## Related

- [[0007-docker-ml-scenario-ui]]
- [[none]]

>[!INFO] Important Note
> All services are containerized, so ensure Docker and Docker Compose are installed and running on your system. Avoid running local Python/Flask servers to prevent conflicts with containerized ports.


>[!WARNING] Caution
> If port 5006 is already in use, stop any local Python processes (e.g., `pkill -f "python.*ml_scenario_ui"`) before starting the container. Rebuilding the container with `--no-cache` can resolve build errors.
