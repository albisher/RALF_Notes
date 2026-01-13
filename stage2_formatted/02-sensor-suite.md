**Tags:** #open-source, #LiDAR, #sensor-integration, #ROS, #point-cloud-processing, #intel-realsense, #pcl, #open3d, #aerial-deployment
**Created:** 2026-01-13
**Type:** research

# 02-sensor-suite

## Summary

```
Explores open-source sensor suite recommendations for LiDAR and visual systems, emphasizing cost-effectiveness and compatibility.
```

## Details

> This document outlines a production-ready approach for integrating open-source sensors, focusing on LiDAR and complementary visual systems. It prioritizes **Ouster OS1/OS2**, **Livox LiDAR**, and **Velodyne VLP-16 Puck LITE** for LiDAR, detailing their SDKs, ROS/ROS2 support, and processing compatibility with **PCL** and **Open3D**. The complementary visual system recommends the **Intel RealSense D455** with the **librealsense SDK**, emphasizing its open-source nature, depth/color streaming, and ROS2 integration.

## Key Functions

### `Ouster OS1/OS2`

Open Python SDK for cross-platform LiDAR integration with PCL/Open3D and ROS2.

### `Livox SDK`

Provides ROS1/ROS2 support and compatibility with PCL/Open3D for LiDAR processing.

### `Velodyne VLP-16 Puck LITE`

Commercial LiDAR with proprietary SDK but widely used in aerial deployments.

### `librealsense SDK`

Open-source depth/color streaming for Intel RealSense D455, enabling ROS2 integration.

### `PCL (Point Cloud Library)`

C++ library for advanced LiDAR point cloud processing.

### `Open3D`

Open-source 3D data processing toolkit (Python/C++).

### `FAST_LIO_LC`

LiDAR-inertial odometry with loop closure for ROS1/ROS2.

### `GroundLoc`

LiDAR-only localization pipeline supporting Ouster and Livox.

## Usage

1. **LiDAR Selection**: Choose Ouster/Livox for open-source compatibility or Velodyne for commercial reliability.
2. **SDK Integration**: Install respective SDKs (`pip install ouster-sdk`, Livox SDK, or ROS packages).
3. **Processing**: Use PCL/Open3D for point cloud analysis or FAST_LIO_LC/GroundLoc for localization.
4. **Visual System**: Deploy Intel RealSense D455 with librealsense SDK for depth/color streams.
5. **ROS Integration**: Leverage ROS2 for sensor fusion and publish/subscribe workflows.

## Dependencies

> ``ouster-sdk``
> ``livox-sdk``
> ``librealsense2``
> `PCL (C++)`
> `Open3D (Python/C++)`
> `ROS2`
> `ROS1 (for Livox)`
> `FAST_LIO_LC`
> `GroundLoc.`

## Related

- [[Sensor Suite Architecture]]
- [[LiDAR Processing Workflow]]
- [[ROS2 Sensor Integration Guide]]

>[!INFO] Important Note
> **Ouster/Livox**: Prioritize these for open-source advantages; Velodyne is commercial but robust for aerial use.

>[!WARNING] Caution
> **ROS1/ROS2 Compatibility**: Livox supports both versions; ensure ROS version alignment during deployment.
