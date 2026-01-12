**Tags:** #camera-systems, #drones, #depth-sensing, #sensor-integration, #HMRS, #polarization, #quality-inspection, #ROS2, #intel-realsense, #open-source-sdk
**Created:** 2026-01-12
**Type:** documentation

# 00-camera-overview

## Summary

```
Provides an overview of camera addons for HMRS drones, detailing depth and polarization camera specifications and applications.
```

## Details

> This document outlines the camera requirements for various HMRS drones, focusing on depth and polarization cameras for applications like depth sensing, quality inspection, and visual servoing. It specifies key specifications for each camera type, including Intel RealSense D455 (for depth sensing) and Sony IMX250MZR (for streak detection and quality inspection), along with their integration capabilities, SDKs, and documentation resources.

## Key Functions

### `Depth Camera (Intel RealSense D455)`

- Enables stereoscopic depth sensing with high accuracy and frame rates.

### `Polarization Camera (Sony IMX250MZR)`

- Supports streak detection and quality inspection via multi-directional polarization filters.

## Usage

- **Depth Camera**: Deployed in THE SCOUT drone for depth mapping and motion compensation.
- **Polarization Camera**: Used in THE OVERSEER drone for streak detection and quality inspection.
- **Processing**: Leverages open-source libraries (OpenCV, DoLP algorithms) for real-time image analysis.

## Dependencies

> `OpenCV`
> `ROS2`
> `Intel RealSense SDK 2.0 (librealsense)`
> `nvTorchCam`

## Related

- [[01-realsense-d455-specifications]]
- [[02-realsense-d455-integration]]
- [[03-realsense-d455-documentation-links]]
- [[04-sony-imx250mz]]

>[!INFO] Key Integration
> The Intel RealSense D455 is production-ready with ROS2 support, ensuring seamless integration into drone systems for depth sensing.

>[!WARNING] Hardware Constraints
> Polarization cameras like Sony IMX250MZR require careful handling due to their specialized sensor technology and limited weight (~67g). Ensure proper mounting to avoid mechanical stress.
