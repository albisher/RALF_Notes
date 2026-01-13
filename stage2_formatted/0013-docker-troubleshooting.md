**Tags:** #docker, #compose, #troubleshooting, #troubleshooting-guide, #docker-desktop, #linux, #macos
**Created:** 2026-01-13
**Type:** code-notes

# 0013-docker-troubleshooting

## Summary

```
Guide for resolving Docker and Docker Compose connection and operational issues.
```

## Details

> This document provides troubleshooting steps for Docker and Docker Compose errors, particularly focusing on the "Cannot connect to the Docker daemon" issue. It includes solutions for starting Docker Desktop, running a custom check-and-start script, verifying Docker status, and manually managing services. The guide also addresses common issues like incorrect command syntax, port conflicts, permission errors, and database connection problems. It offers alternatives for running applications without Docker, noting limitations on database features.

## Key Functions

### ``docker info``

Verifies Docker daemon status and system information.

### ``docker compose up -d``

Starts all services in detached mode.

### ``docker compose down``

Stops and removes containers.

### ``docker compose ps``

Lists running containers.

### ``docker compose logs -f hmrs-live``

Follows logs for a specific service.

### ``docker compose up -d --build``

Rebuilds and starts services.

### ``docker compose restart hmrs-live``

Restarts a specific service.

### ``docker compose down -v``

Removes containers and volumes.

### ``lsof -i`

5007`**: Identifies processes using a specific port.

### ``sudo usermod -aG docker $USER``

Adds user to Docker group (Linux).

### ``./check_and_start_docker.sh``

Script to check and start Docker services.

### ``docker compose up -d session-db``

Starts a database container first.

### ``docker compose up -d hmrs-live``

Starts the main service after database.

## Usage

1. **Check Docker Status**: Run `docker info` to verify Docker is running.
2. **Start Docker Services**: Use `docker compose up -d` or `docker compose up -d --build` to start services.
3. **Resolve Port Conflicts**: Use `lsof -i :5007` to find and resolve port conflicts.
4. **Fix Permissions**: Add your user to the Docker group on Linux (`sudo usermod -aG docker $USER`).
5. **Database Dependency**: Start database containers first (`docker compose up -d session-db`).
6. **Run Without Docker**: Use `pip install -r requirements.txt` and `python hmrs_simulation_live.py` if Docker is unavailable.

## Dependencies

> `- Docker Desktop (macOS)
- Docker Engine (Linux)
- Docker Compose (v1 or v2)
- `lsof` (Linux command for port analysis)
- Python (for running `hmrs_simulation_live.py`)
- `pip` (Python package manager)
- `requirements.txt` (Python dependencies)`

## Related

- [[Docker Official Documentation]]
- [[Docker Compose Guide]]
- [[Linux User Permissions Guide]]

>[!INFO] Important Note
> Ensure Docker Desktop is running on macOS before executing Docker commands. The `open -a Docker` command launches Docker Desktop automatically.


>[!WARNING] Caution
> Running `docker compose down -v` permanently deletes all containers and volumes. Use with caution to avoid data loss.
