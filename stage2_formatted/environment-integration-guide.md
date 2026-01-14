**Tags:** #docker, #environment-variables, #secrets-management, #docker-compose, #configuration-management, #security, #development-prod-migration, #api-integration, #database-configuration
**Created:** 2026-01-13
**Type:** documentation

# environment-integration-guide

## Summary

```
Explains how to integrate environment variables and Docker secrets in the Space Pearl project for secure and scalable Docker Compose deployments.
```

## Details

> This guide provides two methods for managing sensitive data in the Space Pearl Docker Compose setup: environment variables (for development) and Docker secrets (for production). It details setup scripts, configuration files (`docker-compose.yml`, `docker-compose.secrets.yml`), and usage examples for backend, OpenProject, n8n, and Continue AI services. Environment variables offer a medium-security approach with fallback defaults, while Docker secrets provide high-security encrypted storage. The guide emphasizes secure credential handling and service-specific configurations.

## Key Functions

### ``docker-compose.yml``

Main configuration file for environment variables approach.

### ``docker-compose.secrets.yml``

Configuration file for Docker secrets approach.

### ``./scripts/setup-environment.sh``

Script to initialize environment variables.

### ``./scripts/create-docker-secrets.sh``

Script to generate Docker secrets.

### ``./scripts/validate-secrets.sh``

Script to validate Docker secrets.

### ``docker-compose up -d``

Command to deploy services with environment variables.

### ``docker-compose -f docker-compose.secrets.yml up -d``

Command to deploy services with Docker secrets.

### ``docker exec <container> env | grep <variable>``

Command to inspect environment variables in containers.

### ``docker exec <container> cat /run/secrets/<secret>``

Command to inspect Docker secrets in containers.

## Usage

1. **For Development**:
   - Use `docker-compose.yml` and `.env` file.
   - Set up variables via `./scripts/setup-environment.sh` or manually edit `env.template`.
   - Deploy with `docker-compose up -d`.

2. **For Production**:
   - Use `docker-compose.secrets.yml`.
   - Generate secrets with `./scripts/create-docker-secrets.sh`.
   - Deploy with `docker-compose -f docker-compose.secrets.yml up -d`.

## Dependencies

> `Docker`
> `Docker Compose`
> `Bash scripting`
> `PostgreSQL`
> `Redis`
> `OpenProject`
> `n8n`
> `Continue AI services.`

## Related

- [[Space Pearl Project Docker Setup]]
- [[Docker Secrets Best Practices]]
- [[Environment Variables Security Guide]]

>[!INFO] Important Note
> Always use Docker secrets for production environments to avoid hardcoding sensitive data in configuration files. Docker secrets are mounted as files in containers, ensuring they are encrypted and inaccessible outside the container.


>[!WARNING] Caution
> Avoid using default or placeholder values (e.g., `your-secret-key-change-in-production`) in production. Validate secrets before deployment to prevent unauthorized access. Use secure passwords and keys for databases and APIs.
