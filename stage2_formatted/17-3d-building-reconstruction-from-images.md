**Tags:** #photogrammetry, #3d-reconstruction, #drone-imaging, #building-mapping, #sparse-reconstruction, #structure-from-motion, #multi-view-stereo, #LiDAR-complement, #window-cleaning, #pre-analytics
**Created:** 2026-01-13
**Type:** research

# 17-3d-building-reconstruction-from-images

## Summary

```
Explores 3D building reconstruction techniques using drone camera images to enhance HMRS window cleaning workflows.
```

## Details

> This document outlines methods for generating high-fidelity 3D models of buildings via photogrammetry, leveraging drone-captured images. The approach integrates **Structure from Motion (SfM)** and **Multi-View Stereo (MVS)** to estimate building geometry, complementing LiDAR-based mapping. Key focus areas include accuracy benchmarks (horizontal/vertical), workflows for prescans and pre-analytics, and cost-effective implementation using existing camera systems.

## Key Functions

### `Photogrammetry`

Extracts 3D geometry from overlapping 2D images via feature matching and triangulation.

### `Structure from Motion (SfM)`

Estimates camera poses and sparse 3D point clouds from image collections.

### `Multi-View Stereo (MVS)`

Converts SfM outputs into dense 3D point clouds and optional surface meshes.

### `COLMAP`

Open-source SfM/MVS pipeline with GPU acceleration for production-grade reconstruction.

## Usage

1. Capture drone images with 60–80% overlap.
2. Process via COLMAP (CLI or GUI) to generate sparse/dense reconstructions.
3. Export results (PLY/OBJ) for LiDAR integration or window cleaning analytics.

## Dependencies

> `Open-source libraries (e.g.`
> `OpenCV for feature detection)`
> `drone camera hardware`
> `and photogrammetry software (e.g.`
> `COLMAP).`

## Related

- [[LiDAR-based Building Mapping]]
- [[HMRS Window Cleaning System]]

>[!INFO] **Accuracy Trade-offs**
> Horizontal accuracy (1–3 cm) is higher than vertical (2–5 cm); depends on GSD (Ground Sample Distance) and camera calibration.

>[!WARNING] **Overlap Critical**
> Insufficient overlap (>80%) degrades triangulation and reconstruction quality. Test with 60–80% overlap thresholds.
