**Tags:** #healthcheck, #docker, #containerization, #nginx, #alpine, #wget, #unhealthy, #docker-compose
**Created:** 2026-01-12
**Type:** code-notes

# docker-compose.yml

## Summary

```
Fixes Docker Compose frontend healthcheck failure due to missing `wget` in Alpine-based image.
```

## Details

> The issue occurred because the `nginx:alpine` image lacks the `wget` package, causing healthchecks to fail when attempting to verify the container’s readiness. The fix involved installing `wget` in the `Dockerfile.frontend` and adjusting the healthcheck configuration in `docker-compose.yml` to include a `start_period` delay, allowing the Nginx service to initialize before the health check runs. This ensures the container is marked as healthy once Nginx is operational.

## Key Functions

### ``wget` installation`

Installed via `apk add --no-cache wget` in the `Dockerfile.frontend` to enable healthcheck commands.

### ``healthcheck` configuration`

Modified to include `start_period: 5s` in `docker-compose.yml` to delay verification until Nginx is ready.

### ``test`

["CMD", "wget", "--quiet", "--tries=1", "--spider", "http://localhost/"]`**: The healthcheck command that now works due to `wget` availability.

## Usage

1. Apply the changes to `Dockerfile.frontend` and `docker-compose.yml`.
2. Rebuild and redeploy the frontend container:
   ```bash
   docker compose build frontend
   docker compose up -d frontend
   ```
3. Verify health status:
   ```bash
   docker compose ps
   ```
   (Should show `healthy` instead of `unhealthy`.)

## Dependencies

> ``nginx:alpine``
> ``apk` (Alpine Linux package manager)`
> ``docker-compose``

## Related

- [[DOCKER_INTEGRITY_ISSUE]]
- [[MULTI_CONTAINER_ARCHITECTURE]]
- [[LAST_WORK_SUMMARY]]

>[!INFO] Important Note
> The fix ensures proper container monitoring without disrupting functionality. The `start_period` allows time for Nginx to start before health checks begin.

>[!WARNING] Caution
> Ensure `wget` is only installed if explicitly needed for health checks. Overhead may apply if unused.
