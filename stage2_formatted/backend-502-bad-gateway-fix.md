**Tags:** #backend, #docker, #error-fix, #web-api, #restart-loop, #attribute-error, #hmrs, #simulation
**Created:** 2026-01-12
**Type:** code-notes

# backend-502-bad-gateway-fix

## Summary

```
Fixed backend 502 Bad Gateway error by correcting initialization order and adding volume mounts for live updates.
```

## Details

> The issue stemmed from an `AttributeError` in `hmrs_simulation_live.py` where `self.base_position` was accessed before initialization. The fix involved reordering attribute initialization to ensure `base_position` was set before use in `HMRSDroneSpawner`. Additionally, a volume mount was added to `docker-compose.yml` to enable live code updates during development without container rebuilds. This resolved crashes, restored API/WebSocket functionality, and prevented JSON parsing errors.

## Key Functions

### ``hmrs_simulation_live.py``

Contains `HMRSSimulationLive` class with initialization fixes for `base_position`.

### ``HMRSDroneSpawner``

Initialization logic updated to rely on pre-set `base_position`.

### ``docker-compose.yml``

Volume mount configuration for live code updates.

## Usage

1. Apply the code fix in `simulation/hmrs_simulation_live.py`.
2. Update `docker-compose.yml` with the volume mount.
3. Restart containers:
   ```bash
   docker compose down && docker compose up -d
   ```
4. Verify with:
   ```bash
   curl http://localhost:5007/api/health
   ```

## Dependencies

> `numpy (for array initialization)`
> `Docker Compose (for container orchestration).`

## Related

- [[backend-deployment-guide]]
- [[hmrs-docker-config]]
- [[api-error-handling]]

>[!INFO] Initialization Order Fix
> The critical fix was moving `self.base_position` initialization to line ~97 to ensure it was set before use in `HMRSDroneSpawner` initialization (line 121).

>[!WARNING] Production Considerations
> While the volume mount enables development convenience, ensure it does not interfere with production deployments. Test thoroughly before applying to production.
