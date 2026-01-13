**Tags:** #docker, #microservices, #ml-ui, #containerization, #flask, #persistent-storage
**Created:** 2026-01-13
**Type:** code-notes

# 0007-docker-ml-scenario-ui

## Summary

```
Docker setup for ML scenario UI with containerized deployment and data persistence.
```

## Details

> This document outlines the Docker container configuration for an ML Scenario UI application, ensuring it runs entirely within containers without a local server. The setup includes two deployment options: a standalone ML UI container and a full-stack solution combining the UI with a simulation service. The ML UI container uses a custom Docker image (`ml-scenario-ui:latest`), exposes port `5006`, and manages data persistence via named volumes (`ml-scenario-data`). Environment variables control logging, Flask app execution, and host binding. Data (scenarios and outputs) is stored in both container volumes and host directories, ensuring persistence across container restarts.

## Key Functions

### ``docker-compose -f docker-compose.ml-ui.yml up -d``

Starts the standalone ML UI container.

### ``docker-compose up -d``

Launches both `ml-scenario-ui` and `hmrs-simulator` containers.

### ``docker logs -f ml-scenario-ui``

Monitors real-time logs for the ML UI container.

### ``docker inspect ml-scenario-ui | grep Health``

Checks container health via the `/api/scenarios` endpoint.

### ``docker-compose logs -f``

Aggregates logs from all services in the full-stack setup.

## Usage

1. Navigate to the `simulation` directory and run:
   - **Standalone**: `docker-compose -f docker-compose.ml-ui.yml up -d` → Access UI at `http://localhost:5006`.
   - **Full Stack**: `docker-compose up -d` → UI runs on `http://localhost:5006` with simulator integration.
2. Use `docker-compose logs -f` to debug issues, and `docker-compose down` to stop containers.

## Dependencies

> ``docker``
> ``docker-compose``
> ``flask` (for the ML UI application)`
> ``ml-scenario-ui` Docker image.`

## Related

- [[0007-docker-ml-scenario-ui]]
- [[simulation-network-config]]
- [[ml-scenario-ui]]

>[!INFO] **Data Persistence**
> Scenario data (`ml_scenarios.json`) is stored in a named volume (`ml-scenario-data`), ensuring it persists across container restarts. Output files (e.g., screenshots) are synced to the host directory (`./simulation_output/`).


>[!WARNING] **Network Isolation**
> In standalone mode, the `ml-ui-network` bridge isolates the container from other services. Ensure no conflicting ports (e.g., `5006`) are used on the host machine to avoid conflicts.
