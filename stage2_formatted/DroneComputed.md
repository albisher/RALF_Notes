**Tags:** #computed-properties, #drone-management, #reactive-data, #data-filtering, #drone-classification
**Created:** 2026-01-13
**Type:** code-notes

# DroneComputed

## Summary

```
Handles computed drone data properties for categorization, filtering, and analytics.
```

## Details

> This module provides computed properties for drone data, encapsulating logic to filter, group, and aggregate drone information. It assumes `this.drones` is an array of drone objects with properties like `status`, `type`, `flightTime`, and `battery`. Methods return derived data (e.g., active/inactive drones, grouped by type) or aggregated metrics (e.g., total flight time, average battery).

## Key Functions

### `activeDrones()`

Returns drones with status `'active'` or `'flying'`.

### `inactiveDrones()`

Returns drones with status `'inactive'` or `'landed'`.

### `dronesByType()`

Groups drones into an object keyed by their `type` (default: `'unknown'`).

### `scoutDrones()`

Filters drones by type `'scout'`.

### `overseerDrones()`

Filters drones by type `'overseer'`.

### `tankerMuleDrones()`

Filters drones by type `'tanker_mule'`.

### `tankerLifelineDrones()`

Filters drones by type `'tanker_lifeline'`.

### `droneCount()`

Returns the total number of drones.

### `activeDroneCount()`

Returns the count of drones from `activeDrones()`.

### `totalFlightTime()`

Sums `flightTime` (or `0`) across all drones.

### `averageBatteryLevel()`

Computes the mean battery percentage of all drones.

### `lowBatteryDrones()`

Returns drones with battery < 20% (incomplete).

## Usage

```javascript
const droneComputed = new DroneComputed();
const activeDrones = droneComputed.activeDrones();
const groupedDrones = droneComputed.dronesByType();
const lowBatteryDrones = droneComputed.lowBatteryDrones(); // Incomplete
```
**Note:** Initialize `this.drones` before use (e.g., via a parent component or state management).

## Dependencies

> ``this.drones` (assumed to be an array of drone objects with properties like `status``
> ``type``
> ``flightTime``
> ``battery`).`

## Related

- [[DroneDataModel]]
- [[DroneStatusTracker]]

>[!INFO] Data Safety
> Always handle `this.drones` as a fallback array (`|| []`) to avoid errors if undefined.

>[!WARNING] Incomplete Method
> `lowBatteryDrones()` is cut off; ensure it returns drones with `battery < 20` (e.g., `filter(drone => drone.battery < 20)`).
