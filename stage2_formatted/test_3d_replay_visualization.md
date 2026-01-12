**Tags:** #3D-visualization, #replay-test, #drone-motion, #data-validation
**Created:** 2026-01-12
**Type:** code-notes

# test_3d_replay_visualization

## Summary

```
Validates 3D replay data for drone motion and environmental structures to ensure correct visualization.
```

## Details

> This script fetches replay data from a local API (`http://localhost:5007`) for a specified session (`SESSION_ID`) and verifies its completeness and correctness for 3D visualization. It checks:
> - **Motion history** of drones (position, velocity, orientation, and time stamps).
> - **Buildings** in the replay (position, size, and names).
> - **Base position** of the simulation environment.
> 
> The script uses `requests` to fetch JSON data and performs validation checks via `numpy` for spatial calculations (e.g., distance between positions).

## Key Functions

### `Data Fetching`

Retrieves replay data from the API endpoint `/api/sessions/{SESSION_ID}/replay`.

### `Motion History Validation`

Validates drone motion history by checking completeness of position, velocity, orientation, and time data.

### `Distance Calculation`

Computes Euclidean distance between the first and last positions of a drone using `numpy.linalg.norm`.

### `Time Progression Check`

Evaluates the time span between the earliest and latest timestamps in the motion history.

### `Buildings Validation`

Extracts and displays building metadata (position, size, and name) from the replay data.

## Usage

1. Run the script directly (`python test_3d_replay_visualization.py`).
2. Ensure the API server (`http://localhost:5007`) is running and accessible.
3. The script exits with an error if the API request fails or if critical data is missing.

## Dependencies

> ``requests``
> ``json``
> ``numpy``

## Related

- [[none]]

>[!INFO] Important Note
> The script assumes the API returns JSON data with keys like `motion_history`, `buildings`, and `base_position`. Missing keys or invalid data will trigger error messages.

>[!WARNING] Caution
> If `motion_history` is empty, the script exits immediately with `❌ No motion history - cannot test replay`. Ensure at least two position updates exist per drone for smooth visualization validation.
