**Tags:** #drone-motion-analysis, #data-processing, #numerical-computation, #real-time-systems
**Created:** 2026-01-13
**Type:** code-notes

# analyze_drone_motion

## Summary

```
Analyzes drone motion history to validate realistic movement patterns using position, velocity, and time data.
```

## Details

> This script loads motion history data from a JSON file, extracts position, velocity, and timestamp sequences, and computes movement metrics such as total distance traveled, average speed, and velocity magnitudes. It checks for realistic motion by validating the data completeness (at least 2 points) and calculates statistical properties of movement segments.
> 
> The script first validates the existence of the motion history file and checks if the drone’s data exists within the loaded session. It then processes the motion history data to extract numerical arrays for positions, velocities, and timestamps. After computing basic movement metrics (distances between consecutive points, time span, and average speed), it analyzes velocity magnitudes to determine if the drone’s motion appears physically plausible.

## Key Functions

### `Data Loading`

Loads and validates motion history JSON data from a specified session directory.

### `Position/Velocity Extraction`

Parses position, velocity, and timestamp data from each motion point into structured NumPy arrays.

### `Movement Metrics Calculation`

Computes total distance, average speed, and segment length statistics.

### `Velocity Analysis`

Evaluates average and maximum velocity magnitudes across all axes.

## Usage

1. Set `SESSION_ID` and `DRONE_NAME` variables to match your data.
2. Run the script to analyze motion history stored in `training_sessions/{SESSION_ID}/motion_history.json`.
3. Outputs key movement statistics and flags if data is insufficient or missing.

## Dependencies

> `numpy`
> `json`
> `pathlib`

## Related

- [[drone_data_structure]]
- [[motion_validation_guide]]

>[!INFO] Important Note
> The script assumes motion history JSON follows a consistent format with keys `position`, `velocity`, and `sim_time`/`timestamp` for each entry. Missing keys default to zero values.

>[!WARNING] Caution
> If the motion history has fewer than 2 points, the script exits with an error, as at least two points are required to compute meaningful movement metrics.
