**Tags:** #aerial-drones, #open-source-platforms, #uav-selection, #pixhawk, #px4, #ardupilot, #ros2, #inspection-missions
**Created:** 2026-01-13
**Type:** research

# 01-platform-selection

## Summary

```
Document compares platform options for lightweight UAVs, prioritizing open-source solutions for cost and programmability in inspection missions.
```

## Details

> This document evaluates UAV platforms for inspection missions, emphasizing open-source alternatives like PX4/ArduPilot-based quadcopters for their programmability, cost-effectiveness, and ROS2 integration. It contrasts them with commercial options like the Freefly Astro, highlighting trade-offs in payload capacity, flight time, and customization. The analysis also explores alternatives like the DJI M350 RTK (with modifications) and open-source FPV solutions, noting verification requirements for feasibility and support.

## Key Functions

### `PX4/ArduPilot Quadcopter Platform`

Full programmability, ROS2 integration, cost-effective DIY options.

### `Freefly Astro/Astro Max`

High payload capacity, foldable design, but expensive (~$15K).

### `QGroundControl/Mission Planner`

Ground control software for MAVLink/ROS2 communication.

### `MAVLink Protocol`

Open-source communication standard for UAVs.

### `ROS2 Integration`

Enables modular software development via Micro XRCE-DDS Agent.

## Usage

1. **For DIY Developers**: Use PX4/ArduPilot with a custom quadcopter frame to balance cost and flexibility.
2. **For Commercial Inspection**: Evaluate Freefly Astro for high payload/flight time but high upfront cost.
3. **For Compact/All-Weather Use**: Consider DJI M350 RTK (with modifications) if programming support is critical.
4. **For Open-Source Exploration**: Research alternative platforms with open firmware (e.g., FPV cameras).

## Dependencies

> `- PX4/ArduPilot firmware`
> `Pixhawk flight controllers`
> `ROS2 (Micro XRCE-DDS Agent)`
> `MAVLink-compatible ground software.`

## Related

- [[Platform-Selection-Comparison]]
- [[Open-Source-UAV-Firmware-Guide]]
- [[ROS2-UAV-Integration-Tutorial]]

>[!INFO] Important Note
> **PX4/ArduPilot Advantage**: ROS2 integration via Micro XRCE-DDS Agent enables seamless software modularity, critical for inspection missions requiring real-time data processing (e.g., polarization cameras + acoustic emitters).
>

>[!WARNING] Caution
> **Modification Risks**: DJI M350 RTK modifications (e.g., payload reduction) may void warranties or compromise flight safety. Always verify hardware compatibility with open-source firmware.
