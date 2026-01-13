**Tags:** #Docker, #MachineLearning, #Containerization, #Flask, #MLUI, #Simulation, #DevOps
**Created:** 2026-01-13
**Type:** code-notes

# DOCKER_ML_SCENARIO_UI

## Summary

```
Docker-based ML scenario UI setup with containerized execution for simulation workflows.
```

## Details

> This document describes a Docker containerized setup for an ML Scenario UI, eliminating the need for a local Python server. The UI runs in a containerized environment (`ml-scenario-ui`) with persistent data storage via Docker volumes. It supports two deployment modes: standalone (isolated) or full-stack (integrated with a simulation service). The UI exposes a Flask application on port `5006` and includes health checks for monitoring.

## Key Functions

### ``ml-scenario-ui``

Hosts the ML UI application via Flask, serving scenario data and outputs.

### ``docker-compose.ml-ui.yml``

Defines the standalone container configuration for the ML UI.

### ``docker-compose``

Orchestrates container lifecycle (start, stop, logs, rebuild) for both standalone and full-stack deployments.

### ``ml-scenario-data` volume`

Persists scenario configurations across container restarts.

### ``simulation_output` volume`

Stores screenshots and verification artifacts.

## Usage

1. **Standalone Deployment**:
   - Navigate to `simulation` directory and run:
     ```bash
     docker-compose -f docker-compose.ml-ui.yml up -d
     ```
   - Access UI at `http://localhost:5006`.

2. **Full-Stack Deployment**:
   - Run:
     ```bash
     docker-compose up -d
     ```
   - UI runs on `ml-scenario-ui` (port `5006`), simulator on `simulator` (default port `5000`).

## Dependencies

> `Docker Engine`
> `Docker Compose`
> `Python 3.x (for Flask)`
> `ML-related libraries (e.g.`
> `TensorFlow/PyTorch if applicable).`

## Related

- [[Dockerfile_ML_SCENARIO_UI]]
- [[simulation-network-config]]
- [[flask-ml-ui-api-reference]]

>[!INFO] **Data Persistence**
> Scenario data (`ml_scenarios.json`) is stored in a Docker volume (`ml-scenario-data`), ensuring persistence across container restarts. Output files (e.g., screenshots) are synced to the host via `./simulation_output/`.


>[!WARNING] **Network Isolation**
> In standalone mode, the `ml-ui-network` bridge isolates the container from other services. Ensure no conflicting ports (e.g., `5006`) are used on the host. For full-stack mode, containers share the `simulation-network`, enabling inter-container communication.
