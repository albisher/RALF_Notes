**Tags:** #docker, #bash-script, #containerization, #devops, #service-deployment
**Created:** 2026-01-13
**Type:** code-notes

# check_and_start_docker

## Summary

```
Script checks Docker/Docker Compose status and starts services if available.
```

## Details

> This Bash script verifies Docker and Docker Compose availability, provides installation instructions if missing, and starts a Docker Compose service (`docker-compose.yml`) in a parent directory. It logs service status and waits briefly before displaying logs.

## Key Functions

### ``command -v docker``

Checks if Docker CLI is installed.

### ``docker info``

Validates Docker daemon is running.

### ``docker compose version``

Detects Docker Compose availability.

### ``docker compose up -d --build``

Starts services in detached mode with rebuild.

### ``docker compose ps``

Lists running services post-startup.

## Usage

1. Run script in directory containing `docker-compose.yml`.
2. Script navigates to parent directory (`../..`) for service startup.
3. Outputs service status and logs after startup.

## Dependencies

> `docker`
> `docker-compose (or `docker compose` CLI)`

## Related

- [[docker-compose]]
- [[Docker Desktop Installation Guide]]

>[!INFO] Important Note
> The script assumes `docker-compose.yml` exists in a `docker/` subdirectory relative to the script. Adjust paths if needed.

>[!WARNING] Caution
> If Docker fails to start, manually launch Docker Desktop before retrying. The script exits on critical errors.
