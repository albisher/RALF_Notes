**Tags:** #Docker, #Multi-stage-builds, #Vue3, #Vite, #Flask, #Python3.12, #PostgreSQL16, #Redis, #Nginx, #Containerization
**Created:** 2026-01-13
**Type:** architecture

# 2025-07-30_docker-setup-for-vue-3-frontend-with-vite-flask-ba

## Summary

```
Optimized Docker setup for a Vue 3 frontend (Vite) and Flask backend (Python 3.12) with PostgreSQL 16, Redis, and Nginx reverse proxy, emphasizing production efficiency via multi-stage builds and Docker Compose orchestration.
```

## Details

> The setup leverages **multi-stage Docker builds** to minimize frontend (Vue 3/Vite) and backend (Flask/Python 3.12) image sizes while ensuring production-ready performance. The `docker-compose.yml` configures a cohesive environment with PostgreSQL 16 for persistence, Redis for caching, and Nginx as a reverse proxy to route traffic between services. Key optimizations include:
> - **Frontend**: Static assets served via Nginx in a lightweight Alpine-based image.
> - **Backend**: Gunicorn deployment with slim Python 3.12 image and dependency isolation.
> - **Database/Redis**: Official images with persistent volumes for data integrity.
> - **Networking**: A custom bridge network enables seamless inter-service communication.

## Key Functions

### ``frontend/Dockerfile``

Builds Vue 3 app with Vite and serves static files via Nginx in a multi-stage build.

### ``backend/Dockerfile``

Installs Flask dependencies, runs Gunicorn, and optimizes for production with slim Python 3.12.

### ``docker-compose.yml``

Orchestrates all services (frontend, backend, DB, Redis, Nginx) with dependency resolution and networking.

### ``proxy/nginx.conf``

Configures Nginx to route `/api/` to Flask and serve Vue static files via reverse proxy.

## Usage

1. **Build**: Run `docker-compose build` to generate optimized images.
2. **Run**: Execute `docker-compose up --build` to start all containers.
3. **Access**:
   - Frontend: `http://localhost` (Nginx proxy)
   - API: `http://localhost/api/` (Flask backend)
   - Internal services: Resolve via `frontend`, `backend`, `db`, `cache` in the network.

## Dependencies

> `- Node.js (for Vue 3/Vite frontend build)
- Python 3.12 (for Flask backend)
- PostgreSQL 16 (official image)
- Redis 7 (official Alpine image)
- Nginx (official Alpine image)`

## Related

- [[Docker Best Practices for Production]]
- [[Optimizing Multi-Container Docker Setups]]

>[!INFO] Multi-Stage Builds
> Multi-stage builds reduce image size by discarding build-time dependencies (e.g., Node.js in frontend, unnecessary Python packages in backend), improving security and download speed.

>[!WARNING] Environment Variables
> Avoid hardcoding secrets (e.g., `POSTGRES_PASSWORD`). Use Docker secrets or `.env` files for production-sensitive configurations.

>[!INFO] Nginx Proxy Configuration
> Ensure `try_files` in `nginx.conf` matches Vue router hash-based routing (e.g., `/index.html` for SPA fallback).

>[!WARNING] PostgreSQL Persistence
> The `postgres_data` volume ensures data survives container restarts but requires manual cleanup for container removal (`docker-compose rm -v`).
