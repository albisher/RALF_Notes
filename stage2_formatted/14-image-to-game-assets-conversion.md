**Tags:** #open-source, #3d-modeling, #photogrammetry, #game-assets, #gpu-acceleration, #alicevision, #node-based, #simulation, #image-processing, #cu-da, #batch-processing
**Created:** 2026-01-12
**Type:** documentation

# Meshroom

## Summary

```
Open-source 3D reconstruction tool for converting images into textured meshes via photogrammetry, optimized for game asset generation.
```

## Details

> Meshroom is a free, node-based software by AliceVision designed for photogrammetry. It processes multiple 2D images to reconstruct 3D models with textures, supporting GPU acceleration via CUDA. The workflow involves importing images, automatic feature extraction, mesh generation, and exporting assets in formats like OBJ, GLTF, or FBX. It requires a minimum of 20 images (preferably 20–100+) with overlapping angles and good lighting for accurate results.

## Key Functions

### `Node-Based Workflow`

Visual pipeline editor for drag-and-drop image processing.

### `Automatic Processing`

Handles feature extraction, matching, and reconstruction without manual input.

### `GPU Acceleration`

CUDA support speeds up depth map and mesh generation.

### `Batch Processing`

Command-line mode (`Meshroom_batch`) for large-scale workflows.

### `Python Integration`

AliceVision Python bindings for custom scripting.

## Usage

1. **Prepare Images**: Capture 20+ photos from varied angles with 60–80% overlap.
2. **Import**: Drag images into Meshroom’s "Images" node.
3. **Process**: Click "Start" to auto-analyze and reconstruct the model.
4. **Export**: Right-click the "Texturing" node to save as OBJ/PLY/FBX + textures.

## Dependencies

> `- NVIDIA GPU with CUDA support (recommended)
- Python (for custom scripts via AliceVision bindings)
- Open-source dependencies (AliceVision framework)`

## Related

- [[AliceVision Framework]]
- [[Open-Source 3D Tools]]
- [[Photogrammetry Workflows]]

>[!INFO] **GPU Requirement**
> Meshroom leverages CUDA for faster processing. Without a compatible GPU, performance may degrade significantly.

>[!WARNING] **Image Quality Matters**
> Poor lighting, blurriness, or lack of overlap will result in incomplete or inaccurate 3D models. Always test with a scale reference if possible.
