**Tags:** #flight-path, #quadcopter, #simulation, #waypoints, #circular-flight, #automation
**Created:** 2026-01-13
**Type:** code-notes

# create_circular_flight_session

## Summary

```
Generates and orchestrates a circular flight session for three quadcopters around a 3m diameter path for 1 minute at uniform height.
```

## Details

> This script automates the creation of a circular flight session for three small quadcopters. It first generates waypoints for a 3-meter diameter circular path using trigonometric calculations, then interacts with a local simulation server (`http://localhost:5007`) to stop, reset, create a demo session, and start the simulation. The script includes error handling for retries and API communication.

## Key Functions

### `generate_circular_waypoints`

Computes evenly spaced waypoints along a circular trajectory based on center coordinates, radius, height, and number of points.

### `Session creation/management`

Handles API calls to create a demo session with specified parameters (e.g., session name, number of buildings).

## Usage

1. Run the script to generate waypoints and trigger a circular flight session.
2. Ensure the local simulation server (`http://localhost:5007`) is running.
3. The script will:
   - Stop any existing simulation (with retries).
   - Create a demo session named "CircularFlight".
   - Start the simulation with the generated waypoints.

## Dependencies

> `requests`
> `time`
> `json`
> `numpy`
> `math`

## Related

- [[Simulation Server API Documentation]]
- [[Flight Path Generation Guide]]

>[!INFO] Important Note
> The script assumes the simulation server is running on `localhost:5007`. If the server is elsewhere, update `BASE_URL` accordingly.

>[!WARNING] Caution
> If the simulation server is unresponsive, the script will retry up to 3 times. Ensure the server is operational before execution.
