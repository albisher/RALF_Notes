**Tags:** #3D-mesh, #drone-visualization, #rotation-transformation, #plotly, #geometry-processing
**Created:** 2026-01-13
**Type:** code-notes

# mesh-generator-box

## Summary

```
Generates 3D mesh models for drones and vehicles using quaternion-based rotations and Plotly visualization.
```

## Details

> This class (`MeshGeneratorBox`) specializes in creating 3D mesh representations for drones and cars. It handles quaternion-to-rotation matrix conversion, vertex rotation, and mesh generation for a quadcopter drone. The drone mesh includes a body and four arms, with configurable dimensions (length, width, height, scale) and orientation via quaternion input. The `createDroneMesh` method constructs a Plotly-compatible mesh trace object, while helper methods (`quaternionToRotationMatrix`, `applyRotation`) manage geometric transformations.
> 
> The code snippet provided truncates after defining the body vertices and faces but includes the full class structure and intended logic for drone mesh generation.

## Key Functions

### `quaternionToRotationMatrix`

Converts quaternion orientation to a 3×3 rotation matrix for applying transformations.

### `applyRotation`

Rotates input vertices using a provided rotation matrix.

### `createDroneMesh`

Constructs a 3D mesh for a drone, including body and arms, with configurable position, orientation, scale, and color.

## Usage

```javascript
const meshGen = new MeshGeneratorBox();
const droneMesh = meshGen.createDroneMesh(
    [0, 0, 0], // Position
    [0, 0, 0, 1], // Orientation (quaternion)
    1.5, // Scale
    '#FF5733' // Custom color
);
```

## Dependencies

> `Plotly.js (for mesh visualization)`
> `Math.js (implicitly for numerical operations).`

## Related

- [[Mesh-Generator-Extensions]]
- [[3D-Rotation-Transformations]]

>[!INFO] Quaternion Format Detection
> The method automatically detects quaternion format ([w,x,y,z] or [x,y,z,w]) by checking if the first element exceeds 0.5 in magnitude.

>[!WARNING] Edge Case Handling
> If quaternion length ≠ 4, it defaults to an identity matrix (no rotation), which may break intended transformations. Ensure quaternion input is valid.
