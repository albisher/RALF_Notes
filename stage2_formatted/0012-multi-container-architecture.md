**Tags:** #docker, #microservices, #backend, #frontend, #database, #containerization, #nginx, #flask, #postgresql, #real-time, #scaling, #separation-of-concerns
**Created:** 2026-01-13
**Type:** architecture

# 0012-multi-container-architecture

## Summary

```
Implements a multi-container microservices architecture for a web application using Docker, separating frontend, backend, and database into distinct containers.
```

## Details

> This architecture divides the application into three primary containers: a **frontend** (serving static files via Nginx), a **backend** (hosting Flask + Socket.IO), and a **database** (PostgreSQL). The **simulator** container reuses the backend image for standalone simulation runs. Communication flows include HTTP API requests, Socket.IO real-time connections, and static file serving. Nginx acts as a lightweight proxy for routing `/api/` and `/socket.io/` requests to the backend, while the frontend container exposes port 5007 externally for static assets. PostgreSQL stores session data, building records, and ML training data. The design emphasizes modularity, scalability, and independent updates for each component.

## Key Functions

### `Backend Container (`backend`)`

Manages Flask API endpoints, Socket.IO real-time communication, simulation logic, and database connections.

### `Frontend Container (`frontend`)`

Serves Vue.js static files via Nginx, proxies API/Socket.IO requests, and caches assets.

### `Database Container (`session-db`)`

Hosts PostgreSQL for session data, building records, and ML learning data.

### `Simulator Container (`simulator`)`

Runs standalone simulations using the backend image, generating training data without a web interface.

### `Nginx Proxy`

Routes `/api/` and `/socket.io/` requests from the frontend to the backend, handling static file requests directly.

## Usage

1. Deploy containers using Docker Compose with the provided `docker-compose.yml` (not shown here).
2. Mount frontend and backend volumes for hot-reloading during development.
3. Expose the frontend container’s port 5007 externally for static file serving.
4. Configure Nginx to proxy `/api/` and `/socket.io/` requests to the backend container.
5. Ensure PostgreSQL is accessible internally (port 5432) for database connections.
6. Run simulations manually via the `simulator` container when needed.

## Dependencies

> `- Docker`
> `Docker Compose
- Nginx
- Flask (Python)
- Socket.IO (Python)
- PostgreSQL
- Vue.js (frontend static files)`

## Related

- [[Dockerfile]]
- [[Dockerfile]]
- [[docker-compose]]
- [[PostgreSQL Configuration]]

>[!INFO] Important Note
> The **frontend container** must expose port 5007 externally to serve static files and proxy API/Socket.IO requests. This is critical for client access to the application.
>

>[!WARNING] Caution
> Ensure **network isolation** between containers is correctly configured to avoid security risks (e.g., exposing backend ports externally). Use Docker’s internal networking or a reverse proxy like Nginx for secure routing.
