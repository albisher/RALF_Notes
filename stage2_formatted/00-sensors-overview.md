**Tags:** #sensor, #drone, #ros, #navigation, #force_torque, #proximity, #imu, #aerial_robotics, #load_cell, #tether_control
**Created:** 2026-01-12
**Type:** documentation

# sensor_addons_overview

## Summary

```
Provides an overview of required sensor addons for HMRS drones, including IMU, force/torque, and proximity sensors for navigation, control, and mission-specific tasks.
```

## Details

> This document outlines the sensor requirements for various HMRS drones, categorized into IMU (for navigation and attitude estimation), force/torque sensors (for load verification and tether tension control), and proximity sensors (for automated hose routing). Each category details integration status, applications, and available sensor options with ROS compatibility, including specific sensor models, drivers, and documentation links.

## Key Functions

### `IMU Integration`

Provides redundancy and motion compensation via flight controllers (PX4/ArduPilot) and Intel RealSense D455.

### `Force/Torque Sensors`

Enables load cell verification (THE TANKER Mule) and tether tension monitoring (THE TANKER Lifeline) with ROS support.

### `Proximity Sensors`

Supports automated obstacle avoidance (e.g., hose routing) using ultrasonic/infrared sensors with ROS wrappers.

## Usage

Refer to this document to select, integrate, and configure sensors based on drone-specific requirements. Follow linked specifications and integration guides for detailed setup.

## Dependencies

> `ROS (Robot Operating System)`
> `PX4/ArduPilot flight controllers`
> `Intel RealSense D455`
> `ROS2 drivers for force/torque sensors (e.g.`
> ``kwr75_force_sensor_ros2`).`

## Related

- [[01-force-torque-sensors-specifications]]
- [[02-force-torque-sensors-integration]]
- [[none]]

>[!INFO] IMU Integration
> IMU redundancy is critical for flight stability; ensure multiple IMU sets are deployed in drones like CUAV X25 Super/EVO.

>[!WARNING] Sensor Selection
> For force/torque sensors, verify ROS compatibility and output formats (e.g., analog/digital) to avoid integration failures.
