**Tags:** #environment-variables, #secrets-management, #database-configuration, #microservices, #api-integration, #security, #docker-containers, #openproject, #n8n, #flask, #redis, #postgresql, #ai-services
**Created:** 2026-01-13
**Type:** documentation

# environment-variables-definition

## Summary

```
Defines environment variables and secrets for the Space Pearl project’s tool stack, including databases, applications, and external services.
```

## Details

> This document outlines all required environment variables and secrets for the Space Pearl project’s microservices architecture, covering databases (PostgreSQL, Redis), applications (OpenProject, n8n, Flask, Continue AI), and external integrations (AI APIs, GitHub, email). It distinguishes between non-sensitive configurations (e.g., database names, hostnames) and sensitive data (e.g., passwords, API keys) marked with `<SECRET>`. The setup includes container networking, service URLs, and debugging configurations for development and deployment.

## Key Functions

### `POSTGRES_DB`

Sets the main PostgreSQL database name for the Space Pearl project.

### `OPENPROJECT_DB_USER`

Configures the OpenProject database user credentials.

### `JWT_SECRET_KEY`

Defines the secret key for JWT token signing in application security.

### `REDIS_HOST`

Specifies the Redis cache host for distributed session management.

### `PERPLEXITY_API_KEY`

Stores the API key for integrating Perplexity AI services.

### `DOCKER_NETWORK`

Defines the Docker network for inter-container communication.

### `DEBUG`

Enables or disables debug mode for development environments.

## Usage

1. Replace `<SECRET>` placeholders with actual sensitive values (e.g., passwords, API keys).
2. Configure containerized services (e.g., PostgreSQL, Redis) with these variables in `.env` files or Docker Compose.
3. Apply secrets securely (e.g., via Docker secrets, Kubernetes secrets, or environment variable managers like AWS Secrets Manager).
4. Use the defined service URLs (`FRONTEND_URL`, `BACKEND_URL`, etc.) for local development and deployment.

## Dependencies

> `PostgreSQL`
> `Redis`
> `OpenProject`
> `n8n`
> `Flask`
> `Continue AI`
> `Docker`
> `external AI services (Perplexity`
> `OpenAI`
> `Anthropic)`
> `SMTP services (if enabled).`

## Related

- [[Space Pearl Project Dockerfile]]
- [[OpenProject Deployment Guide]]
- [[n8n Configuration Guide]]
- [[AI Service Integration Docs]]

>[!INFO] Important Note
> Secrets marked with `<SECRET>` must be stored securely outside the codebase (e.g., in a secrets manager or encrypted `.env` files). Never commit these to version control.

>[!WARNING] Caution
> Avoid hardcoding sensitive data in environment variables. Use dynamic secrets injection (e.g., Docker secrets, Kubernetes ConfigMaps) for production environments to prevent exposure during deployment.
