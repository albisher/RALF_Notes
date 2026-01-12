**Tags:** #drone-simulation, #backend-api, #frontend-interaction, #database-verification, #reset-logic
**Created:** 2026-01-12
**Type:** test-reference

# reset-button-drone-loading-verification

## Summary

```
Verifies drone configuration persistence after reset button interaction in a drone simulation system.
```

## Details

> This document details a verification test for the drone loading system, confirming that saved drone configurations persist in the database even after a reset. The test ensures the reset button’s frontend and backend behavior aligns: clearing runtime drone instances while preserving database entries. It includes API checks, frontend confirmation flows, and auto-loading logic for the Config page.

## Key Functions

### ``/api/reset` endpoint`

Clears runtime drone spawning but reloads configurations from the database.

### ``loadDroneConfigurations()``

Frontend function that auto-loads drone data after reset.

### ``handleViewChange()``

Config page handler triggering auto-load on navigation.

### ``executeResetSimulation()``

Backend API call that triggers a page reload post-reset.

## Usage

1. **Test Execution**: Run via API verification (e.g., `curl`) and frontend UI.
2. **Verification Steps**:
   - Confirm 5 drones exist in DB before reset.
   - Trigger reset via UI or API.
   - Verify API returns preserved configurations post-reset.
3. **Debugging**: Use `docker exec` to inspect `drone_configurations.json` in the container.

## Dependencies

> `- Python backend (API endpoint `/api/reset`)`
> `- Database (stores drone configurations)`
> `- Docker container (hosts backend)`
> `- Frontend JavaScript (handles UI reset dialog and reload).`

## Related

- [[drone-simulation-backend]]
- [[drone-configuration-api-docs]]
- [[frontend-drone-ui]]

>[!INFO] Critical Preservation
> The reset endpoint explicitly reloads configurations from `drone_configurations.json` to ensure saved drones persist, bypassing runtime state.

>[!WARNING] API Endpoint
> Ensure `/api/reset` is properly secured (e.g., auth) to prevent unintended resets in production.
