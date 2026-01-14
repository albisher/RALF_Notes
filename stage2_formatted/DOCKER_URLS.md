**Tags:** #docker, #web-development, #api, #frontend-backend, #logging, #debugging
**Created:** 2026-01-13
**Type:** documentation

# DOCKER_URLS

## Summary

```
Documentation for Docker container URLs, ports, and troubleshooting for a local development environment with UI, backend API, and proxy services.
```

## Details

> This document outlines the Docker container URLs, port mappings, and access points for a multi-service application stack. It includes URLs for the UI-Beta (production UI), frontend (Vue.js dev server), backend API, static files, and health checks. The setup uses Docker Compose to manage containers, with detailed instructions for starting services, accessing logs, and resolving common issues like UI or API failures.

## Key Functions

### `UI-Beta (Production UI)`

Main production UI with all features (Generate, Link, Card, Timeline, Story).

### `Frontend (Vue.js Dev Server)`

Development server with hot reload, accessible via `http://localhost:5173` or proxy.

### `Backend API`

REST API endpoints accessible via `http://localhost:5001/api` or proxy.

### `Nginx Proxy`

Handles HTTP/HTTPS routing between containers and host ports.

### `Logging System`

Debug-level request/response logging with console and file output.

### `Health Check`

Endpoint to verify service availability (`http://localhost:8888/health`).

## Usage

1. **Start Services**: Run `docker-compose up -d` to launch all containers.
2. **Access UI**: Open `http://localhost:8888/ui-beta/` in a browser.
3. **Debugging**:
   - View logs with `docker-compose logs -f <service>`.
   - Check container status with `docker-compose ps`.
   - Copy logs to host with `docker-compose cp <container>:<logfile> ./`.

## Dependencies

> `- Docker`
> `Docker Compose
- PostgreSQL (internal)
- Redis (internal)
- Nginx (proxy)
- Flask (backend)
- Vue.js (frontend)`

## Related

- [[Dockerfile_Configuration]]
- [[docker-compose]]
- [[Backend_API_Reference]]

>[!INFO] Important Note
> UI-Beta is the production UI and must be accessed via `http://localhost:8888/ui-beta/` or `https://localhost:8443/ui-beta/`. Direct frontend access (`http://localhost:5173`) is for development only.


>[!WARNING] Caution
> Ensure all containers are running (`docker-compose ps`) before accessing services. Misconfigured ports or missing dependencies (e.g., PostgreSQL/Redis) will cause API failures or UI errors. Check logs immediately if issues arise.
