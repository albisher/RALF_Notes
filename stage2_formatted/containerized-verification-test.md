**Tags:** #containerization, #docker, #microservices, #verification, #devops
**Created:** 2026-01-13
**Type:** test-reference

# containerized-verification-test

## Summary

```
Verifies that all application services run in Docker containers, ensuring no local development servers interfere.
```

## Details

> This script performs a containerized services verification by checking if the application and its dependencies (frontend, backend, database, cache) are running exclusively within Docker containers. It uses `axios` to confirm the main application endpoint (`https://localhost:8443`) is accessible, bypassing local Node.js/Python servers. The script logs container statuses, service ports, and manual verification steps, validating Docker orchestration and containerized dependencies.

## Key Functions

### `testContainerizedServices()`

Orchestrates the verification by checking containerized services, logging statuses, and handling errors.

### `axios.get()`

Fetches the main application endpoint with HTTPS agent configuration to bypass SSL certificate validation.

## Usage

1. Run the script directly (`node containerized-verification-test.js`).
2. Verify logs confirm:
   - No local development servers are running.
   - All Docker containers (`space-pearl-*`) are active.
   - Application (`localhost:8443`) loads successfully.
3. Cross-check with manual commands (`docker-compose ps`, `docker logs`).

## Dependencies

> `axios`
> `Node.js runtime`
> ``https` module (built-in)`
> `Docker CLI tools (for manual verification steps).`

## Related

- [[Docker Compose Configuration]]
- [[Application Deployment Guide]]

>[!INFO] Important Note
> The script assumes Docker is running and containers (`space-pearl-*`) are pre-deployed. Manually verify container statuses if logs show inconsistencies.

>[!WARNING] Caution
> Disabling SSL validation (`rejectUnauthorized: false`) is for testing only. In production, enforce strict SSL checks.
