**Tags:** #verification, #drone-configuration, #database-persistence, #api-testing, #sensor-config
**Created:** 2026-01-12
**Type:** test-reference

# drone-config-browser-verification

## Summary

```
Verification of drone sensor configurations across database, API, and browser persistence for five drones.
```

## Details

> This document confirms that five drones—each equipped with distinct sensor configurations—are correctly stored in a database, persisted to a JSON file (`/app/drone_configurations.json`), and accessible via API endpoints. Verification includes database checks, API responses, and browser-based UI validation. Persistence tests ensure configurations survive random API calls and simulation resets, with sensor-specific configurations (e.g., RGB, IR, LiDAR) validated through UI interactions.

## Key Functions

### ``loadDroneConfigurations()``

Loads drone configurations from the database into the browser UI.

### ``GET /api/drone-configurations``

Retrieves all drone configurations from the backend.

### ``POST /api/drone-configurations``

Saves drone configurations to the database and JSON file.

### ``resetSimulation()``

Clears spawned drones but preserves saved configurations (confirmed via persistence tests).

## Usage

1. **Backend Setup**:
   - Ensure `/app/drone_configurations.json` exists and contains valid drone entries.
   - Deploy API endpoints (`GET/POST /api/drone-configurations`) to serve configurations.
2. **Browser Testing**:
   - Access `http://localhost:5007` and navigate to the Config page.
   - Verify UI displays all 5 drones with correct sensor addons.
   - Test persistence by resetting the simulation and confirming configurations persist.

## Dependencies

> `- Database (likely SQLite/PostgreSQL) for storing drone configurations.
- Backend API (e.g.`
> `Flask/FastAPI) handling `/api/drone-configurations` endpoints.
- Frontend framework (e.g.`
> `React) rendering drone configurations in the browser UI.
- Simulation engine (e.g.`
> `PX4/ArduPilot) for drone state management.`

## Related

- [[drone-configuration-api-spec]]
- [[simulation-reset-protocol]]
- [[database-backup-policy]]

>[!INFO] Important Note
> **Sensor-Specific Validation**: Each drone’s "Special Sensor" (e.g., `rgb_camera`, `lidar`) must be explicitly checked in the UI’s "Addons" section. Missing or misconfigured sensors will fail verification.
>

>[!WARNING] Caution
> **API Endpoint Dependencies**: If `/api/drone-configurations` fails, configurations may not load in the browser. Test endpoints independently before UI validation.
