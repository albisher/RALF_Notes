**Tags:** #open-source, #drone-operations, #mission-management, #autonomous-systems, #PX4, #ArduPilot, #ROS2, #pre-flight-checks, #geofencing, #LiDAR, #photogrammetry, #path-planning, #SLAM
**Created:** 2026-01-13
**Type:** research

# 00-operational-workflow

## Summary

```
Document outlines an open-source-based operational workflow for drone missions, emphasizing pre-flight checks, mission execution, and real-time adjustments.
```

## Details

> This document details a structured **open-source mission management workflow** for autonomous drone operations, covering pre-mission setup, real-time execution, and post-mission tasks. It emphasizes using open-source tools like **QGroundControl, MAVProxy, PX4, and ArduPilot** for mission planning, geofencing, and sensor validation. The workflow includes phases like **scout launch (LiDAR mapping), climber work (obstacle avoidance), tanker operations (fluid monitoring), and overseer tasks (path correction)**. Key challenges (e.g., timing, calibration) and open-source alternatives are highlighted for verification.

## Key Functions

### `Mission Planning`

QGroundControl/MAVProxy for waypoint management and upload.

### `Pre-Flight Checks`

PX4/ArduPilot for GPS/sensor validation and battery monitoring.

### `Geofencing`

Built-in PX4/ArduPilot or custom implementations for restricted zones.

### `Scout Launch`

LiDAR mapping (ROS2 topic `/scout/surface_map`) to generate real-time 3D maps.

### `Climber Work`

Obstacle avoidance via obstacle map integration; fluid spray calibration (solenoid valve control).

### `Tanker Operations`

Fluid-level monitoring (Mule) or tether tension management (Lifeline).

### `Overseer`

Polarization camera for path correction (30-second scans).

## Usage

1. **Pre-Mission**: Upload CAD/flight plan, configure geofencing, and validate pre-flight checks.
2. **Execution**:
   - Scout drone maps terrain (T+0) and sends data to Climber’s path planner.
   - Climber avoids obstacles and calibrates fluid spray (T+10).
   - Tanker (Mule/Lifeline) refuels or stabilizes tether (T+10–end).
   - Overseer corrects path via polarization scans (T+12–end).
3. **Verification**: Test timing, mapping accuracy, and system integrations.

## Dependencies

> `PX4`
> `ArduPilot`
> `ROS2`
> `QGroundControl`
> `MAVProxy`
> `LiDAR sensors`
> `polarization cameras`
> `ROS2 topics (`/scout/surface_map`).`

## Related

- [[Drone-Sensor-Calibration-Guide]]
- [[Open-Source-Drone-Control-Systems]]
- [[ROS2-Mapping-Packages]]

>[!INFO] Important Note
> **Mission Phases**: Timing (e.g., Scout launch at +10 min) and sensor data (e.g., LiDAR standoff distance) are critical for real-time adjustments. Verify these before deployment.


>[!WARNING] Caution
> **Fluid Spray Calibration**: Solenoid valve response times (0.05s) and spray patterns (electronically switchable) must align with climber’s workflow. Test under real conditions to avoid miscalibration errors.


>[!WARNING] Caution
> **Tether Management**: Wind gust compensation in Lifeline mode requires dynamic ROS2-based adjustments. Simulate tether failures to validate reliability.
