**Tags:** #docker, #n8n, #postgresql, #docker-compose, #containerization, #database-configuration, #environment-variables, #security, #workflow-automation
**Created:** 2026-01-13
**Type:** documentation

# 2025-08-17_n8n-docker-container-setup-requirements-ports-envi

## Summary

```
Explains Docker container setup for **n8n**, including port mappings, environment variables, PostgreSQL database integration, and security best practices.
```

## Details

> This document outlines the requirements for deploying **n8n** in a Docker container, emphasizing PostgreSQL database configuration, port exposure, persistent data storage via volumes, and secure environment variable management. It provides a structured approach to integrating n8n with existing Docker Compose infrastructure while addressing performance, security, and networking considerations.

## Key Functions

### `Docker Image (`n8nio/n8n`

latest`)** – Hosts the n8n workflow automation engine.

### `Port Mapping (`5678`

5678`)** – Exposes the n8n web UI for remote access.

### `Persistent Volume (`./n8n_data`

/home/node/.n8n`)** – Ensures workflow data persists across container restarts.

## Usage

1. Define a `docker-compose.yml` with `n8n` and `postgres` services, mapping ports, volumes, and environment variables.
2. Ensure PostgreSQL is pre-configured with a dedicated database (`n8n_db`) and user (`n8n_user`).
3. Access n8n via `http://<host>:5678` after starting the container.
4. Secure credentials using Docker secrets or environment files.

## Dependencies

> ``n8nio/n8n``
> `PostgreSQL (`postgres:13`)`
> `Docker Compose`
> `Docker CLI.`

## Related

- [[Docker Compose Reference]]
- [[PostgreSQL Docker Setup Guide]]
- [[n8n Official Documentation]]

>[!INFO] **Database Isolation**
> Use a dedicated PostgreSQL user (`n8n_user`) and database (`n8n_db`) to prevent conflicts with other services.
>

>[!WARNING] **Resource Limits**
> Allocate at least **2GB RAM** and **2 CPU cores** to avoid performance degradation during workflow execution.
