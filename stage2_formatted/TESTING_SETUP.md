**Tags:** #docker, #testing, #backend, #frontend, #database, #api, #devops, #postgresql, #redis, #flask, #vuejs, #unified-generator
**Created:** 2026-01-13
**Type:** documentation

# TESTING_SETUP

## Summary

```
Guide for setting up and testing a multi-service application with Docker, PostgreSQL, Redis, and a unified AI generator interface.
```

## Details

> This file outlines the setup process for a Dockerized application stack, including frontend (Vue.js), backend (Flask), database (PostgreSQL), cache (Redis), and a reverse proxy (Nginx). Users must configure environment variables, run migrations, and verify service status before accessing endpoints. The setup includes a unified generator UI for testing AI-generated content across multiple modules.

## Key Functions

### `docker-compose up -d`

Starts all containerized services in detached mode.

### `flask db upgrade`

Executes database migrations in the Flask backend.

### `docker-compose ps`

Lists running container services.

### `docker-compose logs -f`

Streams logs for debugging.

### `unified-generator UI`

Frontend endpoint for testing AI-generated content tabs (Characters, Locations, Items, etc.).

### `Backend API (ports 5000/8080)`

Exposes Flask-based endpoints for programmatic access.

### `Frontend (ports 5173/8080)`

Hosts Vue.js dev server and proxy routes.

## Usage

1. Clone the project and create a `.env` file with required credentials.
2. Run `docker-compose up -d` to start services.
3. Execute `docker-compose exec backend flask db upgrade` to apply migrations.
4. Access endpoints via `localhost:8080` (proxy) or direct ports (e.g., `localhost:5173`).
5. Test the unified generator at `localhost:8080/unified-generator`.

## Dependencies

> `PostgreSQL 16`
> `Redis 7`
> `Docker Compose`
> `Flask`
> `Nginx`
> `Vue.js/Vite`
> `Docker.`

## Related

- [[Docker Compose Configuration]]
- [[Backend API Documentation]]
- [[Frontend Vue]]

>[!WARNING] Database Reset
> **Warning**: Running `docker-compose down -v` deletes all data in PostgreSQL. Use only if testing a clean environment.

>[!INFO] Proxy vs Direct Access
> The proxy (Nginx) routes traffic to `localhost:8080`, while direct ports (e.g., `5000`) bypass it. Use `8080` for unified access.

>[!Caution] Port Conflicts
> If ports are occupied, modify `docker-compose.yml` or stop conflicting services (e.g., another app using `5173`).
