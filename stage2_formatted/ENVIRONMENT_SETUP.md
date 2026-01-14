**Tags:** #environment-configuration, #docker-setup, #api-integration, #security-best-practices, #database-management
**Created:** 2026-01-13
**Type:** documentation

# ENVIRONMENT_SETUP

## Summary

```
Guides setup of environment variables for a multi-service project integrating OpenProject and Continue AI using Docker and API keys.
```

## Details

> This guide outlines the process of configuring environment variables for the **Space Pearl** project, which includes OpenProject (a project management tool) and **Continue AI** (an AI service). Users must copy a template, customize `.env` with API keys and credentials, and deploy services via Docker Compose. The setup involves required API keys (Perplexity/OpenAI), security secrets (JWT/OpenProject), database configurations (PostgreSQL), and service ports. Security best practices emphasize avoiding default credentials, using Docker secrets, and isolating environments.

## Key Functions

### ``env.template``

Predefined `.env` file template for copying.

### ``docker-compose up -d``

Deploys all services in detached mode.

### ``JWT_SECRET_KEY``

Generates JWT tokens for authentication.

### ``POSTGRES_DB`/`OPENPROJECT_DB``

Configures database names/users/passwords.

### ``CONTINUE_PORT``

Binds Continue AI service to a specified port.

### ``docker-compose logs``

Retrieves service logs for debugging.

## Usage

1. Copy `env.template` to `.env` and edit values.
2. Run `docker-compose up -d` to start services.
3. Access services via provided URLs (frontend, OpenProject, Continue AI).
4. For production, enforce HTTPS, use Docker secrets, and monitor logs.

## Dependencies

> `Docker`
> `Docker Compose`
> `PostgreSQL`
> `OpenProject`
> `Continue AI (Node.js-based)`
> `and external APIs (Perplexity/OpenAI).`

## Related

- [[Space Pearl Project Architecture]]
- [[Continue AI API Documentation]]
- [[OpenProject Deployment Guide]]

>[!INFO] Important Note
> **Never commit `.env` to version control**—it contains sensitive keys. Use `.gitignore` or Docker secrets instead.

>[!WARNING] Caution
> **Default passwords (`spacepearl123`, `openproject123`) are insecure**. Replace them immediately in production.
