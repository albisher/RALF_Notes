**Tags:** #vision, #pybullet, #computer_vision, #image_processing, #robotics, #depth_estimation, #opencv_fallback
**Created:** 2026-01-13
**Type:** code-notes

# camera_processor_box

## Summary

```
Processes camera images from PyBullet to generate RGB, depth, and segmentation outputs.
```

## Details

> The `CameraProcessorBox` class initializes a camera processor for PyBullet simulations, handling image capture with configurable resolution, field of view, and clipping planes. It uses PyBullet’s `getCameraImage` to fetch RGB, depth, and segmentation data from a simulated camera. If OpenCV (`cv2`) is unavailable, it limits processing capabilities with a warning. The class encapsulates single responsibility for camera data processing, abstracting PyBullet-specific rendering logic.

## Key Functions

### ``__init__(self, width, height, fov, near, far)``

Configures camera parameters (resolution, FOV, clipping planes).

### ``capture_image(self, physics_client, camera_position, camera_target, camera_up)``

Captures raw image data (RGB, depth, segmentation) from PyBullet using `getCameraImage`.

## Usage

```python
processor = CameraProcessorBox(width=640, height=480, fov=60.0)
image_data = processor.capture_image(
    physics_client=physics_client_id,
    camera_position=[x, y, z],
    camera_target=[x, y, z],
    camera_up=[0, 0, 1]
)
print(image_data['rgb'].shape)  # Output: (height, width, 3)
```

## Dependencies

> `pybullet`
> `numpy`
> `cv2 (optional fallback)`

## Related

- [[PyBullet documentation]]
- [[OpenCV installation guide]]

>[!INFO] OpenCV Fallback
> If `cv2` is missing, depth/segmentation processing is disabled, but RGB capture persists.

>[!WARNING] PyBullet Dependency
> Requires a running PyBullet physics client (`physics_client_id`). Ensure the client is active before calling `capture_image`.
