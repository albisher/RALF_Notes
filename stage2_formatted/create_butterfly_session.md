**Tags:** #drone-automation, #path-planning, #figure-8-movement, #3d-coordinates, #butterfly-pattern
**Created:** 2026-01-13
**Type:** code-notes

# create_butterfly_session

## Summary

```
Generates a drone flight session with a 3D figure-8 (butterfly) movement pattern for simulation testing.
```

## Details

> This script creates a new simulation session, stops any existing one, and defines a parametric path for a drone to follow a butterfly (figure-8) trajectory in 3D space. The script uses trigonometric functions to generate smooth, oscillating coordinates for X, Y, and Z axes, incorporating height variation for dynamic flight. It interacts with a local API (`http://localhost:5007`) to manage drone sessions and simulate movement.

## Key Functions

### `generate_butterfly_path`

Computes a series of 3D coordinates forming a figure-8 pattern with adjustable center, radii, and height variation.

### `Session creation logic`

Handles API calls to create a demo session with specified buildings and checks simulation status.

## Usage

1. Run the script to stop any existing simulation (up to 3 retries).
2. Create a new session named "ButterflyFlight" with 3 buildings.
3. The drone will follow a predefined butterfly path in 3D space based on parameters passed to `generate_butterfly_path`.

## Dependencies

> `requests`
> `time`
> `json`
> `numpy`
> `math`

## Related

- [[none]]

>[!INFO] Important Note
> The script assumes the API endpoint (`BASE_URL`) is `http://localhost:5007`. If the drone simulation server is running on a different host/port, update `BASE_URL` accordingly.

>[!WARNING] Caution
> If the simulation server is unresponsive, the script may fail silently. Ensure the server is running and accessible before execution. The retry logic limits attempts to 3.
