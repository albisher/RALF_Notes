**Tags:** #drone-automation, #sensor-configuration, #swarm-management, #api-integration
**Created:** 2026-01-13
**Type:** code-notes

# add_sensor_drones

## Summary

```
Script to programmatically add drones with specialized sensor configurations to a drone swarm system.
```

## Details

> This script fetches the current drone configuration from a local API (`http://localhost:5007`), checks for existing drones, and dynamically adds drones with distinct sensor capabilities (RGB, IR, thermal, polarization, LiDAR). Each drone inherits a base configuration (e.g., `quadcopter` type, `gyroscope` sensor) while adding a unique sensor module. The script uses `requests` for HTTP interactions and `json` for data serialization.

## Key Functions

### `get_current_config()`

Retrieves the current drone configurations from the API endpoint `/api/drone-configurations`.

### `save_config(config)`

Saves a new drone configuration to the API via a POST request.

### `add_sensor_drones()`

Orchestrates drone creation by fetching existing configs, defining new drones with sensor-specific add-ons, and submitting them to the system.

## Usage

1. Run the script to fetch existing drone configurations.
2. Define new drones with unique sensor configurations in the `new_drones` list.
3. Call `add_sensor_drones()` to add drones to the system.
4. Verify changes via the API or manually inspect the updated config.

## Dependencies

> `requests`
> `json`
> `pathlib (Python standard libraries)`

## Related

- [[none]]

>[!INFO] Important Note
> The script assumes the API endpoint (`http://localhost:5007`) is running and accessible. If the API fails to respond, the script exits gracefully with an error message.

>[!WARNING] Caution
> Modifying drone configurations directly may disrupt existing operations. Always test in a controlled environment before deploying to production.
