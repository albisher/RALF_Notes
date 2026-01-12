**Tags:** #LiDAR, #Aerial-Drones, #3D-Mapping, #Sensor-Technology, #Open-Source-SDKs, #PCL, #Open3D, #ROS, #Commercial-OpenSource
**Created:** 2026-01-12
**Type:** documentation

# 00-lidar-overview

## Summary

```
Provides an overview of LiDAR sensor options for THE SCOUT drone, detailing specifications, compatibility, and integration for centimeter-accurate 3D mapping.
```

## Details

> This document compares LiDAR sensors required for THE SCOUT drone, emphasizing their technical specifications, statuses (production-ready/open-source), and integration capabilities with open-source libraries like PCL, Open3D, and ROS. It highlights key features such as range, accuracy, field of view, and SDK support, with references to documentation and related files for deeper exploration.

## Key Functions

### `LiDAR Sensor Selection`

Identifies and evaluates LiDAR options (Velodyne VLP-16 Puck LITE, Ouster OS1/OS2, Livox LiDAR) for drone applications.

### `Technical Specifications`

Lists critical metrics (weight, range, accuracy, power consumption) for each sensor.

### `Integration Guidance`

Documents compatibility with PCL, Open3D, ROS, and SDK availability (e.g., `ouster-sdk`, Livox ROS drivers).

### `Documentation Links`

Provides direct access to user manuals, datasheets, and SDK references.

## Usage

To use this document:
1. **Select a LiDAR**: Choose based on weight, range, and SDK support for THE SCOUT drone.
2. **Review Specifications**: Verify accuracy, FOV, and power consumption for deployment constraints.
3. **Integrate with Software**: Use PCL/Open3D for processing or ROS for real-time applications.
4. **Access Documentation**: Refer to linked files/datasheets for detailed integration steps.

## Dependencies

> `- PCL (Point Cloud Library)
- Open3D
- ROS (Robot Operating System) / ROS2
- `ouster-sdk` (Python package for Ouster LiDAR)
- Livox ROS drivers (ROS1/ROS2 packages)`

## Related

- [[01-velodyne-vlp16-lite-specifications]]
- [[02-velodyne-vlp16-lite-integration]]
- [[04-ouster-os1-os2-specifications]]
- [[05-ouster-os1-os2-integration]]
- [[06-ouster-os1-os2-documentation-links]]
- [[Livox ROS Driver GitHub]]

>[!INFO] Weight Consideration
> Velodyne VLP-16 Puck LITE’s 590g weight is critical for aerial deployment; ensure drone payload capacity accommodates it.

>[!WARNING] Accuracy Trade-offs
> While Ouster OS1/OS2 offers open-source advantages, commercial sensors (e.g., Velodyne) may provide tighter accuracy (±3 cm) for critical applications.

>[!INFO] SDK Dependency
> Livox’s SDK includes ROS packages; ensure ROS version compatibility (ROS1/ROS2) for seamless integration.
