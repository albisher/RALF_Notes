**Tags:** #docker, #openproject, #postgresql, #containerization, #database-configuration, #environment-variables, #devops
**Created:** 2026-01-13
**Type:** documentation

# 2025-08-17_openproject-docker-container-setup-requirements-po

## Summary

```
Provides detailed setup requirements for OpenProject using Docker containers, including ports, environment variables, PostgreSQL configuration, and persistent storage.
```

## Details

> This document outlines the essential steps and configurations needed to deploy OpenProject in Docker containers, emphasizing secure database integration (PostgreSQL), proper port mapping, and environment variable management. It includes hardware recommendations, persistent storage paths, and best practices for Docker Compose orchestration, ensuring scalability and data integrity for medium-sized projects.

## Key Functions

### `Docker Compose Setup`

Orchestrates OpenProject and PostgreSQL containers with persistent volumes for data retention.

### `Port Mapping`

Exposes OpenProject on a host port (e.g., `8080:80`) for external access.

### `Environment Variables`

Configures security (e.g., `OPENPROJECT_SECRET_KEY_BASE`) and database connections (e.g., `DATABASE_URL`).

### `PostgreSQL Configuration`

Manages dedicated database users, credentials, and volume mounts for PostgreSQL data persistence.

### `Secret Management`

Handles sensitive data securely via `.env` files or Docker secrets.

## Usage

1. Install Docker and Docker Compose on the host machine.
2. Create a `.env` file with required secrets (e.g., `OPENPROJECT_SECRET_KEY_BASE`).
3. Define a `docker-compose.yml` with OpenProject and PostgreSQL services, including volumes for persistent storage.
4. Run `docker-compose up -d` to deploy the containers.
5. Access OpenProject via the mapped port (e.g., `http://localhost:8080`).

## Dependencies

> `Docker Engine`
> `Docker Compose`
> `PostgreSQL client libraries (e.g.`
> ``psql`)`
> `and a host system with sufficient CPU/RAM for containerized workloads.`

## Related

- [[OpenProject Docker Official Documentation]]
- [[PostgreSQL Docker Quick Start]]
- [[Docker Compose Best Practices]]

>[!INFO] **Persistent Storage Critical**
> Ensure volumes (`/var/lib/openproject/pgdata` and `/var/lib/openproject/assets`) are mounted to host directories to avoid data loss during container restarts. Use absolute paths for reliability.


>[!WARNING] **HTTPS Mandatory in Production**
> Disable HTTPS (`OPENPROJECT_HTTPS=false`) only for development. Enforce HTTPS in production to secure communications and comply with web standards. Use a reverse proxy (e.g., Nginx) for TLS termination if needed.
