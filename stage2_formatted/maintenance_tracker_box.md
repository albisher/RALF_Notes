**Tags:** #maintenance_tracking, #IoT, #operational_metrics, #alert_system, #single_responsibility
**Created:** 2026-01-13
**Type:** code-notes

# maintenance_tracker_box

## Summary

```
Tracks maintenance cycles for equipment based on area cleaned, operation time, and mission cycles, generating alerts when thresholds are exceeded.
```

## Details

> The `MaintenanceTrackerBox` class monitors operational metrics (area cleaned, time spent, mission cycles) to determine when maintenance is required. It initializes thresholds for cleaning cycles (m²), time (hours), and mission cycles, then updates tracked metrics via `update_operation_metrics`. The internal `_check_maintenance_needs` method evaluates these metrics against thresholds and populates `maintenance_alerts` with warnings (e.g., "Drive track cleaning needed") if limits are exceeded.

## Key Functions

### ``__init__``

Configures thresholds (cleaning limit, time limit, cycle limit) and initializes tracking variables (e.g., `total_area_cleaned_m2`, `mission_cycles`).

### ``update_operation_metrics``

Adds incremental values to tracked metrics (area, time) and increments `mission_cycles` if a full cycle completes.

### ``_check_maintenance_needs``

Private method that triggers alerts when any threshold (area, time, or cycles) is breached, storing results in `maintenance_alerts`.

## Usage

1. Instantiate the tracker with desired thresholds:
   ```python
   tracker = MaintenanceTrackerBox(cleaning_cycle_limit_m2=1000.0, time_limit_hours=200.0)
   ```
2. Update metrics after each operation:
   ```python
   tracker.update_operation_metrics(area_cleaned_m2=500.0, operation_time_hours=5.0, mission_completed=True)
   ```
3. Retrieve alerts:
   ```python
   alerts = tracker.maintenance_alerts  # List of dicts with alert details
   ```

## Dependencies

> `numpy (via `import numpy as np`)`
> `datetime (standard library)`
> `typing (standard library)`

## Related

- [[none]]

>[!INFO] Thresholds are configurable
> Customize `cleaning_cycle_limit_m2`, `time_limit_hours`, or `cycle_limit` during initialization to adapt to equipment-specific needs.

>[!WARNING] Alerts are cumulative
> Repeated updates may generate duplicate alerts if thresholds are crossed multiple times in a single operation. Consider deduplication logic for production use.
