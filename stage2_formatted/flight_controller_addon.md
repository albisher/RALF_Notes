**Tags:** #PX4, #ArduPilot, #FlightController, #Addon, #DroneAutomation, #SensorIntegration, #StateManagement
**Created:** 2026-01-13
**Type:** code-notes

# flight_controller_addon

## Summary

```
Core flight controller addon for PX4/ArduPilot drones, managing arming, modes, and sensor integration.
```

## Details

> This class extends `BaseAddon` to provide flight control capabilities for PX4/ArduPilot systems. It initializes with configurable firmware/model-specific attributes (weight, power, dimensions) and tracks flight state (armed status, mode). The addon integrates with a drone object, fetching IMU data via an IMU addon if available. Core methods include arming/disarming, mode switching, and generating status updates.

## Key Functions

### ``__init__(self, firmware`

str = "px4", model: str = "pixhawk")`**: Initializes flight controller with model-specific specs and state variables.

### ``arm(self)``

Arms the controller if safety checks pass; returns boolean success.

### ``disarm(self)``

Disarms the controller, resetting armed status.

### ``set_flight_mode(self, mode`

str)`**: Updates and logs the current flight mode.

### ``generate_data(self, dt`

float) -> Dict[str, Any]`**: Generates a status dictionary combining drone state and IMU data (if available).

## Usage

```python
addon = FlightControllerAddon(firmware="px4", model="pixhawk")
addon.arm()  # Arm the drone
addon.set_flight_mode("STABILIZE")  # Switch to stabilize mode
data = addon.generate_data(0.1)  # Fetch status updates
```

## Dependencies

> ``.base_addon``
> ``numpy``
> ``typing``
> ``time` (internal dependencies).`

## Related

- [[PX4 Documentation]]
- [[ArduPilot Guide]]
- [[BaseAddon Implementation]]

>[!INFO] Model-Specific Overrides
> Weights/power values are dynamically adjusted for models like `cuav_x25_super` (e.g., 0.080 kg, 2.0 W).

>[!WARNING] IMU Dependency
> If `drone.imu_addon` is missing, `generate_data()` returns a placeholder `_generate_no_data()` result.
