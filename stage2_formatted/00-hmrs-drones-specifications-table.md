**Tags:** #drones, #specification-table, #HMRS, #vertical-surface-cleaning, #robotics, #aerial-logistics, #sensors, #octocopter, #quadcopter, #mission-role
**Created:** 2026-01-12
**Type:** documentation

# 00-hmrs-drones-specifications-table

## Summary

```
Comprehensive drone specifications table for a heterogeneous multi-robot system (HMRS) focused on vertical-surface window cleaning.
```

## Details

> This document outlines detailed specifications for four specialized drones—**THE SCOUT**, **THE TANKER (Mule)**, **THE TANKER (Lifeline)**, and **THE OVERSEER**—designed for vertical-surface window cleaning operations. Each drone serves a distinct mission role, with configurations tailored to tasks like reconnaissance, logistics, resupply, and quality assurance. The table includes technical details such as payload capacity, flight duration, sensor compatibility, environmental resistance, and operational constraints.

## Key Functions

### `THE SCOUT`

Pre-computes dynamic maps and identifies hazards 10 minutes ahead of climbers using LiDAR and depth cameras.

### `THE TANKER (Mule)`

Automatically resupplies climbers with fluids when levels drop below 20% via autonomous cartridge swaps.

### `THE TANKER (Lifeline)`

Manages continuous power and fluid supply via a 15N tension tether, ensuring uninterrupted operations.

### `THE OVERSEER`

Inspects cleaning quality and deters birds using lightweight sensors and active deterrence mechanisms.

## Usage

This table is intended for engineers, operators, and system integrators to design, deploy, and maintain the HMRS drones. Key applications include:
- **Mission planning** for vertical-surface operations.
- **Sensor compatibility checks** for LiDAR and cameras.
- **Environmental compliance** (IP ratings, temperature ranges).
- **Logistics coordination** for resupply and tether management.

## Dependencies

> `- PX4/ArduPilot flight controllers (CUAV X25 Super or Pixhawk series)
- LiDAR sensors (Velodyne VLP-16 Puck LITE`
> `Ouster OS1/OS2`
> `Livox)
- Depth cameras (Intel RealSense D455)
- Octocopter/Quadcopter platforms`

## Related

- [[HMRS System Architecture]]
- [[Window Cleaning Operations Guide]]
- [[Drone Sensor Calibration]]

>[!INFO] **Critical Sensor Selection**
> The **THE SCOUT** must use **Velodyne VLP-16 Puck LITE** or alternatives (Ouster OS1/OS2, Livox) for centimeter-accurate mapping. Depth cameras (Intel RealSense D455) are mandatory for environmental hazard detection.

>[!WARNING] **Tether Management Risks**
> **THE TANKER (Lifeline)** must include redundant power sources (backup battery) to prevent failures during tethered operations, as unlimited battery life is only guaranteed under ideal conditions.
