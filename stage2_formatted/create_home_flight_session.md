**Tags:** #drone_flight, #programmatic_control, #circular_path, #api_integration, #geospatial
**Created:** 2026-01-13
**Type:** code-notes

# create_home_flight_session

## Summary

```
Script programmatically configures a drone to fly in a circular orbit around a predefined "Home" location using API calls.
```

## Details

> This script programmatically simulates a drone flying in a circular pattern around a fixed "Home" location in Kuwait (latitude: 29.234431172766747, longitude: 48.05498783476817). It uses a local API endpoint (`http://localhost:5007`) to control the drone via HTTP requests. The script first ensures the simulation is stopped, then sets the drone’s GPS coordinates to the Home location before generating waypoints for the circular flight path. The waypoints are calculated using trigonometry to define positions in local coordinates (x, y, z) relative to the base station.
> 
> The script includes error handling for API calls and retries up to three times if the simulation is still running. It also logs each step for debugging and verification.

## Key Functions

### `generate_circular_waypoints_around_home`

Generates a list of waypoints forming a circular flight path around a specified center (Home location) with adjustable radius, height, and number of points.

### `API interaction functions`

Handles HTTP requests to `BASE_URL` for stopping/resetting the simulation, setting GPS coordinates, and checking drone status.

## Usage

1. Run the script to start a drone flight session in a circular orbit around the Home location.
2. Ensure the drone simulation server (`http://localhost:5007`) is running.
3. Adjust parameters like `radius`, `height`, and `num_points` in `generate_circular_waypoints_around_home` to customize the flight path.
4. The script automatically stops the simulation if it is running before proceeding.

## Dependencies

> `requests`
> `time`
> `json`
> `numpy`
> `math`

## Related

- [[None]]

>[!INFO] Important Note
> The script assumes the drone simulation server is running on `localhost:5007`. If the server is elsewhere, update `BASE_URL` accordingly.


>[!WARNING] Caution
> If the drone simulation server crashes or fails to respond, the script will retry up to three times. Ensure the server is stable to avoid unexpected behavior.
