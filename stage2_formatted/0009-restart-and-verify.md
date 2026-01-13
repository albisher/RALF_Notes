**Tags:** #restart, #verification, #docker, #api-endpoints, #debugging, #session-management, #curl-testing, #error-handling, #cors
**Created:** 2026-01-13
**Type:** documentation

# 0009-restart-and-verify

## Summary

```
Provides instructions for restarting and verifying API session endpoints in a simulation server.
```

## Details

> This document outlines procedures for restarting a server running `hmrs_simulation_live.py` and verifying its API routes. It includes instructions for Docker, direct execution, and virtual environments, along with methods to restart and validate routes via scripts or manual testing. The verification ensures endpoints return correct responses (e.g., `200 OK` with JSON) after restart, confirming proper route registration and error handling.

## Key Functions

### ``hmrs_simulation_live.py``

Main server script hosting session endpoints (`/select`, `/replay`, `/db/list`).

### ``verify_routes_after_restart.sh``

Automated script to test route availability post-restart.

### ``test_session_endpoints.py``

Python test script for manual API validation.

### `CORS headers & error handling`

Ensures secure and fault-tolerant API interactions.

## Usage

1. **Restart**:
   - Use Docker: `docker compose restart hmrs-live` or `docker restart hmrs-live-simulation`.
   - Use direct commands: `Ctrl+C` to stop, then `python hmrs_simulation_live.py` (with venv activation if needed).
2. **Verify**:
   - Run `./verify_routes_after_restart.sh` or `python3 test_session_endpoints.py`.
   - Manually test endpoints via `curl` (e.g., `curl -X POST .../select`).

## Dependencies

> `- Docker (for containerized execution)
- Python 3.x (for direct/script execution)
- `hmrs_simulation_live.py` (core server file)
- `docker-compose` (if using Docker)`

## Related

- [[`0009-restart-and-verify`]]
- [[`hmrs_simulation_live]]
- [[`docker-compose]]
- [[`test_session_endpoints]]

>[!INFO] Important Note
> Ensure the server logs confirm all routes (`/select`, `/replay`, `/db/list`) are registered after restart. Missing logs may indicate route misconfiguration.


>[!WARNING] Caution
> If using Docker, verify the container’s port (`5007`) matches the expected endpoint URL. A misconfigured port will cause `404` errors during testing.
