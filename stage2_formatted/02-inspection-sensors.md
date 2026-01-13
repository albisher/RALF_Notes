**Tags:** #inspection, #sensors, #open-source, #image_processing, #polarization, #real_time, #ros2, #mavlink, #defect_detection
**Created:** 2026-01-13
**Type:** research-notes

# 02-inspection-sensors

## Summary

```
Explores open-source and commercial solutions for detecting water streaks and defects using polarization cameras and image processing.
```

## Details

> This document outlines a **Streak Detection System** leveraging **polarization cameras** (e.g., Sony IMX250MZR) to identify defects like water streaks via polarization anomalies. The system employs **OpenCV** for real-time image processing, including **DoLP (Degree of Linear Polarization) analysis**, **HSV color space conversion**, and **edge detection** (Canny/Sobel). The hardware (commercial cameras) is paired with open-source software for defect detection, achieving **95-99% accuracy**. Quality metrics include a **<2 mm width threshold** for water streaks and **>5 cm² coverage gaps** for missed spots. The system transmits **real-time XY coordinates** via **MAVLink/ROS2** to climbers.

## Key Functions

### `Polarization Camera Integration`

Detects defects via polarization anomalies (e.g., Sony IMX250MZR).

### `OpenCV Processing`

Edge detection, HSV analysis, and DoLP calculation for defect segmentation.

### `ROS2/MAVLink Communication`

Transmits defect coordinates in real-time to robotic/climbing systems.

### `Quality Validation`

Ensures <2 mm defect width and >5 cm² coverage gaps for reliability.

## Usage

1. Deploy **polarization cameras** (e.g., Alkeria CELERA P Series) for defect detection.
2. Use **OpenCV** for image processing pipelines (DoLP, edge detection, HSV analysis).
3. Integrate **ROS2/MAVLink** for real-time defect data transmission to robotic systems.
4. Validate metrics (e.g., defect width, coverage gaps) to ensure system accuracy.

## Dependencies

> `OpenCV`
> `ROS2 perception packages`
> `TF2 (ROS2 transform library)`
> `MAVLink`
> `nvTorchCam.`

## Related

- [[MIT Polarization Camera Research]]
- [[ROS2 Perception Packages]]
- [[MAVLink Protocol Documentation]]

>[!INFO] Important Note
> **Sensor Hardware**: Commercial cameras (e.g., Sony IMX250MZR) are required, but all processing is open-source.

>[!WARNING] Caution
> **Real-Time Constraints**: Ensure ROS2/MAVLink latency is <100 ms to maintain defect detection accuracy.
