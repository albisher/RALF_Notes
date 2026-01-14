**Tags:** #backend-troubleshooting, #redis-configuration, #docker-compose, #environment-variables, #hash-generation-system, #storytelling-tools, #deterministic-generation, #space-time-coordinates
**Created:** 2026-01-13
**Type:** documentation

# backend-troubleshooting

## Summary

```
A troubleshooting guide for backend issues affecting hash generation features, including Redis authentication, environment variable checks, and demo script alternatives.
```

## Details

> This document outlines backend troubleshooting steps for a system relying on Redis and environment variables for hash generation. It details common issues like Redis authentication failures, missing environment variables, and backend health checks. The guide provides quick fixes using Docker Compose commands and suggests using a standalone demo script to demonstrate core functionality (character generation, space-time mapping, and story consistency) while the backend is resolved. The system emphasizes deterministic, multi-dimensional storytelling through hash-based coordinates.

## Key Functions

### ``docker-compose exec cache redis-cli -a redis123 ping``

Verify Redis authentication.

### ``docker-compose ps backend``

Check backend service status.

### ``docker-compose logs backend --tail=20``

Inspect backend logs.

### ``curl -s http`

//localhost:5000/health`**: Test backend health endpoint.

### ``python3 scripts/demo-hash-generation.py``

Run demo script for standalone hash generation.

### ``curl -s http`

//localhost:5000/api/characters/generate/hash`**: Test hash generation API endpoint.

## Usage

1. **Troubleshoot**:
   - Verify Redis authentication with `docker-compose exec cache redis-cli -a redis123 ping`.
   - Check `.env` for correct `REDIS_URL` and `REDIS_PASSWORD`.
   - Restart services with `docker-compose restart backend/cache`.
2. **Test Backend**:
   - Use `docker-compose ps backend` to confirm service is running.
   - Check logs with `docker-compose logs backend`.
3. **Use Demo Script**:
   - Run `python3 scripts/demo-hash-generation.py` to bypass backend issues.
4. **API Testing**:
   - Call `/api/characters/generate/hash` with a JSON payload (e.g., `{"seed": "test_character"}`) to test hash generation.

## Dependencies

> `Docker Compose`
> `Redis`
> `Python 3`
> ``curl``
> ``.env` file (with `REDIS_URL``
> ``REDIS_PASSWORD`).`

## Related

- [[Space Pearl Documentation]]
- [[Hash Generation System Design]]
- [[Docker Compose Configuration Guide]]

>[!INFO] **Core Functionality**
> The demo script (`demo-hash-generation.py`) replicates all backend hash generation features, including character/location generation, space-time coordinates, and deterministic storytelling. Use this to validate system potential before fixing backend issues.

>[!WARNING] **Environment Variables Critical**
> Missing or misconfigured `REDIS_URL`/`REDIS_PASSWORD` in `.env` will break Redis authentication. Always verify these before restarting services.

>[!INFO] **Deterministic Storytelling**
> The hash system guarantees consistent results for the same seed, enabling reproducible world-building. This is its primary strength despite backend hiccups.

>[!WARNING] **Service Order Matters**
> Redis must be running before the backend can connect. Use `docker-compose ps` to confirm Redis is healthy before restarting the backend.
