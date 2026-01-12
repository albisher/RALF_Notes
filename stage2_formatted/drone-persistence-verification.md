**Tags:** #verification, #drone-configuration, #database-persistence, #api-testing, #sensor-config
**Created:** 2026-01-12
**Type:** test-reference

# drone-persistence-verification

## Summary

```
Verifies that drone sensor configurations persist through random webapp interactions and API calls.
```

## Details

> This document outlines a test to confirm that drone configurations—including sensor attachments—remain intact in the database after simulating common user actions like navigation, API calls, and page refreshes. The test ensures that five predefined drones (each with unique sensor combinations) persist through operations such as health checks, simulation resets, and UI interactions. The verification includes database checks via a JSON file and frontend UI validation via browser navigation.

## Key Functions

### ``loadDroneConfigurations()``

Fetches and loads drone configurations from `/api/drone-configurations` when navigating to the Config page.

### ``handleViewChange()``

Triggers `loadDroneConfigurations()` on page navigation to Config.

### ``/api/reset``

Clears runtime drone state but preserves saved configurations in the database.

### ``simulation/scripts/add_sensor_drones.py``

Script to programmatically add drones with sensor configurations (updates existing or adds new).

## Usage

1. **Backend**: Ensure `/app/drone_configurations.json` contains valid drone configurations with sensor data.
2. **Frontend**:
   - Navigate to Config page via sidebar.
   - Verify loaded drones and sensor configurations via UI.
   - Test persistence by resetting simulation and reloading Config page.
3. **Database Verification**:
   - Use `curl` to fetch `/api/drone-configurations` and validate JSON structure.
   - Run `python3 -m json.tool` to pretty-print and inspect configurations.

## Dependencies

> `- `/app/drone_configurations.json` (backend container)
- `/api/drone-configurations` (REST API endpoint)
- `curl` (for database verification)
- Python (`json.tool` for JSON formatting)`

## Related

- [[add_sensor_drones]]
- [[drone-configurations]]

>[!INFO] Database Location
> The drone configurations are stored in `/app/drone_configurations.json` within the backend container. Ensure this file is updated with correct sensor configurations before running tests.

>[!WARNING] Reset Behavior
> The `/api/reset` endpoint clears runtime drone state but **preserves** saved configurations. Misconfiguration here could lead to stale UI if configurations are not reloaded post-reset. Verify `loadDroneConfigurations()` is called after reset to restore configurations.
