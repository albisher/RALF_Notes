**Tags:** #docker, #simulation, #drone, #devops, #quickstart, #backend, #frontend, #postgres, #healthcheck
**Created:** 2026-01-12
**Type:** tutorial

# get-simulation-running-now

## Summary

```
Quick guide to launch a drone simulation using Docker Compose in under 5 minutes.
```

## Details

> This guide provides two paths to start the HMRS window cleaning drone simulation: a fast restart (2 minutes) or a clean build (5 minutes). It leverages Docker Compose to manage backend, frontend, and database containers. The simulation runs on `localhost:5007`, requiring Docker and Docker Compose to be installed. Users can verify the service via container health checks, API endpoints, and the web interface.

## Key Functions

### ``docker compose up -d``

Starts all containers in detached mode.

### ``docker compose down``

Stops and removes containers.

### ``docker compose down -v``

Stops, removes containers, and cleans volumes.

### ``docker compose build``

Rebuilds Docker images from the `docker-compose.yml` file.

### ``docker compose ps``

Lists running containers and their statuses.

### ``curl http`

//localhost:5007/api/health`**: Checks backend health via API.

### ``docker compose logs -f``

Follows logs for startup progress.

## Usage

1. Navigate to the simulation directory (`/Users/amac/Documents/code/WindowCleanner/simulation`).
2. Choose a path (fast restart or clean start) and execute commands.
3. Verify the simulation via container status, API health, or web interface.
4. Launch a drone via the web interface at `http://localhost:5007`.

## Dependencies

> `Docker`
> `Docker Compose`
> `Docker images (`hmrs-backend``
> ``hmrs-frontend``
> ``postgres:15-alpine`).`

## Related

- [[Docker Quickstart Guide]]
- [[HMRS Project Structure]]
- [[WindowCleanner API Documentation]]

>[!INFO] Important Note
> Ensure Docker and Docker Compose are installed with versions **24.x.x or higher**. Running outdated versions may cause compatibility issues with the `docker-compose.yml` file.


>[!WARNING] Caution
> If the backend fails to start, check logs with `docker compose logs -f` and ensure the `hmrs-backend` container logs contain messages like `Backend initialization complete`. A missing volume or misconfigured image may prevent the database from initializing.
