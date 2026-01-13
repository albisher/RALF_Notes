**Tags:** #docker, #ml-ui, #containerization, #scripting, #orchestration, #ml-scenario
**Created:** 2026-01-13
**Type:** code-notes

# docker-run-ml-ui

## Summary

```
Script automates Docker container startup for ML UI application, ensuring containerized execution without local server dependencies.
```

## Details

> This Bash script orchestrates the lifecycle of a Docker container for an ML Scenario UI application. It checks for an existing container, stops it if present, then starts a new containerized instance using `docker compose`. The script includes readiness checks, logs, and user instructions for accessing the UI and managing the container.

## Key Functions

### `Container lifecycle management`

Starts/stopps `ml-scenario-ui` container using `docker compose`.

### `Readiness validation`

Checks container status via `docker ps` and logs.

### `User feedback`

Provides clear instructions for accessing the UI (`localhost:5006`) and container management.

## Usage

1. Run the script from the project root:
   ```bash
   ./docker-run-ml-ui
   ```
2. Access the UI at `http://localhost:5006` after container startup.
3. Stop the container with:
   ```bash
   docker compose -f docker/docker-compose.ml-ui.yml down
   ```

## Dependencies

> ``docker``
> ``docker-compose` (installed via Docker Engine)`

## Related

- [[docker-compose.ml-ui]]
- [[docker-compose]]

>[!INFO] Container Check
> The script checks for the `ml-scenario-ui` container using `docker ps` before proceeding. If the container exists, it stops it first to avoid conflicts.

>[!WARNING] Exit on Failure
> If the container fails to start, the script exits with status `1` and suggests checking logs via `docker logs ml-scenario-ui`.
