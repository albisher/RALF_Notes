**Tags:** #Blender, #3D-Robot, #Mesh-Generation, #Material-Definition
**Created:** 2026-01-13
**Type:** code-notes

# bishy2

## Summary

```
Creates a stylized red robot model in Blender using procedural mesh generation and material assignment.
```

## Details

> This script clears existing objects, defines custom materials with adjustable properties (color, metallic, roughness), and constructs a humanoid robot with a helmet-like head, arms, legs, and functional details. The robot features a red helmet, metallic gray components, and blue accents for visual distinction. Subdivision modifiers smooth key surfaces, while lighting and camera setup enhance rendering quality. The robot is designed with symmetrical left/right components for balance.

## Key Functions

### `create_material`

Generates a Blender material with Principled BSDF shader settings.

### `add_sphere`

Creates a sphere mesh with specified location, scale, name, and material.

### `add_cylinder`

Creates a cylinder mesh with optional rotation for angled placement.

### `add_cube`

Creates a cube mesh for flat surfaces like visors or grilles.

### `smooth_object`

Applies subdivision modifiers to reduce polygon count for smoother surfaces.

### `Camera & Light Setup`

Configures a directional camera and sun/area lights for rendering.

## Usage

1. Run in Blender’s Scripting workspace.
2. Clear existing objects first (script handles this automatically).
3. Customize materials (e.g., adjust metallic/roughness values).
4. Modify object positions/sizes by editing the coordinates in the script.
5. Ensure Cycles render engine is active (script enforces this).

## Dependencies

> `bpy (Blender Python API)`
> `bmesh (Blender mesh operations)`
> `mathutils (Vector math)`
> `math (for trigonometric functions).`

## Related

- [[Blender Robotics Tutorials]]
- [[Blender Material Customization Guide]]

>[!INFO] Important Note
> The script uses Blender’s `bpy` module to dynamically create objects and materials. Ensure Blender is running with Cycles render engine enabled before execution.

>[!WARNING] Caution
> Overly complex geometry may cause performance issues. The subdivision modifier (levels=2) is applied only to the head and body for efficiency. Adjust values if needed.
