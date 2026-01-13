**Tags:** #test, #drone, #persistence, #api, #webapp, #verification, #simulation, #database
**Created:** 2026-01-13
**Type:** code-notes

# test_drone_persistence

## Summary

```
Tests drone configuration persistence after simulated webapp interactions to ensure data integrity.
```

## Details

> This script verifies whether drone configurations remain intact after a series of random API calls and webapp operations, including health checks, state retrievals, realtime status queries, and resets. It simulates typical user interactions and then checks if the drone configurations (including sensor addons) persist in the database. The test specifically validates that each drone has the expected sensors (e.g., RGB camera for `Drone-RGB`) and gyroscopes, ensuring no data corruption during simulated usage.

## Key Functions

### `test_api_call(endpoint, method, data)`

Makes HTTP requests to the drone API and validates success (status code 200) and optional JSON response.

### `verify_drones()`

Checks if drones are loaded from the database, validates their configurations (sensor addons), and reports correctness.

### `simulate_random_usage()`

Performs a sequence of API calls (health, state, realtime status, reset, sessions, buildings) to simulate random webapp usage.

## Usage

1. Run the script to simulate random webapp interactions and verify drone persistence.
2. The script logs each step and checks if drone configurations remain valid after the simulated operations.
3. Expected output includes success/failure messages for each drone and API call.

## Dependencies

> `requests`
> `time`
> `json (standard Python libraries)`

## Related

- [[none]]

>[!INFO] Important Note
> The script assumes the drone API is running at `http://localhost:5007`. Adjust `BASE_URL` if the endpoint differs.

>[!WARNING] Caution
> If the database or API fails during testing, the script will exit early with error messages. Ensure the backend is operational before execution.
