**Tags:** #environment-variables, #docker-secrets, #database-configuration, #security-best-practices, #containerization, #openproject, #n8n, #continue-ai, #postgresql, #redis, #flask
**Created:** 2026-01-13
**Type:** documentation

# 2025-08-17_environment-variables-and-secrets-required-for-ope

## Summary

```
Provides a structured guide on required environment variables and secrets for OpenProject, n8n, Continue AI, PostgreSQL, Redis, and Flask in Docker containers, emphasizing secure handling of sensitive data.
```

## Details

> This document outlines the essential environment variables and secrets needed for each service (OpenProject, n8n, Continue AI, PostgreSQL, Redis, and Flask) when deployed in Docker containers. It emphasizes secure management of secrets (e.g., database passwords, API keys) using Docker secrets or encrypted `.env` files, while non-sensitive configurations are managed via environment variables. Best practices for isolation, rotation, and secure access are detailed, particularly for production environments.

## Key Functions

### `Database Credentials Management`

Secure storage of PostgreSQL credentials (user/password) for each service (OpenProject, n8n, Continue AI, Flask) via Docker secrets.

### `Secrets Injection`

Secure injection of secrets (e.g., API keys, encryption keys) into containers using Docker secrets or sidecar containers (e.g., Hashicorp Vault).

### `Environment Variable Configuration`

Defining environment variables for non-sensitive configurations (e.g., host/port settings) in `docker-compose.yml`.

### `Isolation of Services`

Using separate database users and configurations to isolate services (e.g., OpenProject vs. n8n) to prevent credential leaks.

### `API Key and OAuth Integration`

Secure handling of external API keys (e.g., Perplexity API key for Continue AI) via secrets or environment variables.

## Usage

1. **Define Secrets**: Store sensitive data (e.g., passwords, API keys) in files (e.g., `secrets/openproject_db_password.txt`) with restricted permissions (e.g., `chmod 600`).
2. **Configure `docker-compose.yml`**: Reference secrets in the `secrets` section and environment variables in the `environment` section for each service.
3. **Deploy with Secrets**: Use Docker secrets (for Swarm) or mount `.env` files securely (for Compose) during deployment.
4. **Rotate Secrets**: Implement automated rotation for secrets (e.g., database passwords, API keys) using tools like Vault or manual scripts.

## Dependencies

> `Docker`
> `Docker Compose`
> `PostgreSQL`
> `Redis`
> `Hashicorp Vault (optional for dynamic secrets management)`
> ``.env` files (restricted permissions)`
> `and external services (e.g.`
> `Perplexity API).`

## Related

- [[Docker Secrets Documentation]]
- [[OpenProject Docker Setup Guide]]
- [[n8n Environment Variables]]
- [[PostgreSQL Secrets Management]]
- [[Hashicorp Vault for Secrets Management]]

>[!INFO] Secure Secrets Storage
> Always use Docker secrets (for Swarm) or encrypted `.env` files (restricted permissions) to store sensitive credentials. Avoid committing `.env` files to version control.

>[!WARNING] Avoid Plaintext Secrets
> Never hardcode secrets in Dockerfiles, source code, or public `.env` files. Use secrets management tools like Vault or Docker secrets to mitigate risks.

>[!INFO] Service Isolation
> Ensure each service (e.g., OpenProject, n8n) has isolated database credentials to prevent credential leaks across services. Use separate users/databases for each service.

>[!WARNING] Secrets Rotation
> Regularly rotate secrets (e.g., database passwords, API keys) to maintain security. Implement automated rotation or manual scripts to avoid credential exposure.
