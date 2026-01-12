**Tags:** #sensor-integration, #drone-configuration, #api-verification, #backend-deployment, #automation-script
**Created:** 2026-01-12
**Type:** code-notes

# add_sensor_drones.py

## Summary

```
Script to programmatically add and verify drones with specialized sensor configurations in a drone simulation system.
```

## Details

> This script automates the addition of five drones with distinct sensor configurations (gyroscope, RGB, IR, thermal, polarization, LiDAR) to a drone simulation system. It fetches the current configuration via an API, updates it with the new drones, saves the configuration, and verifies the changes in both the database (`/app/drone_configurations.json`) and API responses. The implementation ensures all drones meet specified requirements, including mandatory gyroscope inclusion and unique sensor assignments.

## Key Functions

### ``add_sensor_drones.py``

Orchestrates drone creation, sensor assignment, and API/database updates.

### ``simulation/drone_configurations.json``

Stores drone configurations post-update (backend container).

## Usage

1. Execute the script via command line: `python simulation/scripts/add_sensor_drones.py`.
2. Verify results in the browser by navigating to the drone configuration page in the UI.

## Dependencies

> `Python (for script execution)`
> `drone simulation API`
> `backend container with `/app/drone_configurations.json`.`

## Related

- [[drone_configurations]]
- [[backend-container-deployment]]

>[!INFO] Important Note
> Ensure the backend container (`/app/drone_configurations.json`) is running before executing the script to avoid file access errors.

>[!WARNING] Caution
> Manual edits to `drone_configurations.json` may invalidate API verification if the script hasn’t been run. Always verify via API first.
