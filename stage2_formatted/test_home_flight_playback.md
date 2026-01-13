**Tags:** #test, #drone_simulation, #flight_playback, #api_integration, #home_location
**Created:** 2026-01-13
**Type:** code-notes

# test_home_flight_playback

## Summary

```
Tests drone flight simulation at a predefined home location and validates playback functionality.
```

## Details

> This script automates the process of verifying a drone flight simulation at a fixed home GPS coordinate. It checks service readiness, configures GPS coordinates, spawns a drone, and initiates a simulation to ensure the system behaves as expected. The script uses HTTP requests to interact with a local drone simulation API, with retry logic for transient failures.

## Key Functions

### `wait_for_service`

Polls the API endpoint `/api/health` to confirm the drone simulation service is operational.

### `set_gps_location`

Sets the drone’s GPS coordinates to predefined home coordinates (latitude/longitude).

### `spawn_drone`

Creates a drone instance (e.g., "Scout-001") at a specified position (x, y, z).

### `start_simulation`

Triggers the drone flight simulation from the home location.

## Usage

1. Run the script to:
   - Wait for the drone service to start.
   - Set the drone’s GPS to home coordinates.
   - Spawn a drone and begin a simulated flight.
2. Monitor console output for success/failure messages.

## Dependencies

> `requests`
> `time`
> `json`
> `datetime (Python standard libraries)
External API: `http://localhost:5007` (drone simulation service)`

## Related

- [[drone_simulation_api_spec]]
- [[home_location_coordinates]]

>[!INFO] Important Note
> The script assumes the drone service runs on `localhost:5007`. Adjust `BASE_URL` if the service uses a different port or host.

>[!WARNING] Caution
> Retries for service readiness may delay execution. Increase `max_retries` or `delay` if the service is slow to start.
