**Tags:** #legacy, #drone_systems, #aerial_mapping, #vertical_robotics, #3d_mapping, #HMRS, #deprecated, #open_source_alternatives
**Created:** 2026-01-13
**Type:** research-documentation

# 90-hmrs-original-specification

## Summary

```
Legacy technical spec for a three-drone system enhancing vertical-surface window cleaning robot operations via dynamic aerial mapping and hazard detection.
```

## Details

> This document describes the **Heterogeneous Multi-Robot Support System (HMRS)**—a three-drone architecture designed to precompute and dynamically map surfaces ahead of a climbing robot ("The Climber"). The system addresses critical gaps in perception, logistics, and quality assurance by deploying specialized drones (e.g., Scout) to generate centimeter-accurate 3D maps and detect hazards. The Scout drone (e.g., DJI Matrice 350 RTK) operates 10 minutes ahead of the Climber, using a LiDAR suite (Velodyne VLP-16 Lite) for high-precision mapping and an Intel RealSense D455 for photogrammetry. The document is deprecated, with consolidated details moved to the `HMRS/` directory, and emphasizes the need for open-source alternatives for proprietary components.

## Key Functions

### `Scout Drone`

Pre-computes 3D surface maps and hazard detection for the Climber’s path.

### `LiDAR Suite (Velodyne VLP-16 Lite)`

Provides centimeter-accurate 3D mapping with 16 channels and 300k points/sec.

### `Intel RealSense D455`

Enhances photogrammetry with depth accuracy <2% at 4m and motion compensation via IMU.

### `Dynamic Mapping`

Real-time hazard identification for vertical-surface operations.

## Usage

The system integrates Scout drones with the Climber’s path planning to enable autonomous hazard avoidance and quality assurance. The deprecated document directs users to the `HMRS/` directory for updated specifications, including verification notes and open-source alternatives.

## Dependencies

> `- DJI Matrice 350 RTK (primary platform)
- Velodyne VLP-16 Puck LITE (LiDAR)
- Intel RealSense D455 (depth camera)
- NDAA-compliant alternatives (e.g.`
> `Inspired Flight IF800 Tomcat)`

## Related

- [[README]]
- [[00-executive-overview]]

>[!INFO] Important Note
> This document is **deprecated** and superseded by the `HMRS/` directory, which includes verified specs, pricing, and open-source alternatives for proprietary components.


>[!WARNING] Verification Required
> All claims (e.g., LiDAR accuracy, drone specs) must be cross-verified against current market availability and compliance standards.
