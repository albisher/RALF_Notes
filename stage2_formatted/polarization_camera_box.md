**Tags:** #polarization, #image_processing, #streak_detection, #computer_vision, #stokes_parameters, #opencv
**Created:** 2026-01-13
**Type:** code-notes

# polarization_camera_box

## Summary

```
Processes polarization camera data to detect water streaks and assess image quality using DoLP (Degree of Linear Polarization).
```

## Details

> This module implements a polarization camera processing pipeline for detecting streaks (e.g., water droplets) in images captured with four directional polarizing filters (0°, 45°, 90°, 135°). It computes the Degree of Linear Polarization (DoLP) from Stokes parameters and applies streak detection using OpenCV (or fallback logic if unavailable). The system evaluates streak width thresholds and coverage gaps to classify streaks and assess image quality.

## Key Functions

### ``compute_dolp``

Computes DoLP from four polarizing filter intensity images using Stokes parameters (S0, S1, S2) and clamps results to [0.0, 1.0].

### ``detect_streaks``

Detects streaks in a DoLP map and intensity image, converting pixel coordinates to physical dimensions (e.g., mm) based on `pixel_size_mm`. Returns structured results including streak coordinates, count, and coverage assessment.

## Usage

1. Initialize `PolarizationCameraBox` with resolution and thresholds.
2. Call `compute_dolp` with four intensity images (I0, I45, I90, I135) to generate a DoLP map.
3. Call `detect_streaks` with the DoLP map and intensity image to produce streak detection results.

## Dependencies

> `numpy`
> `opencv-python (optional`
> `falls back to pure NumPy logic if unavailable)`

## Related

- [[none]]

>[!INFO] Stokes Parameter Calculation
> The DoLP formula relies on Stokes parameters (S0, S1, S2), derived from the sum/difference of intensity images. Division by `S0` (with a small epsilon to avoid NaN) normalizes polarization strength.

>[!WARNING] OpenCV Dependency
> If OpenCV (`cv2`) is unavailable, the streak detection logic defaults to a simplified approach, potentially missing advanced features like edge tracking. Ensure `CV2_AVAILABLE` is checked before calling `detect_streaks`.
