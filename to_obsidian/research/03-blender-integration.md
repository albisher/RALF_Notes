# 03-blender-integration

RAW MODEL OUTPUT (JSON error):

```text
```json
{
  "filename": "03-blender-integration",
  "tags": ["#blender", "#robotics", "#3d-modeling", "#simulation", "#python"],
  "type": "code-notes",
  "summary": "Explores Blender's integration capabilities for robotics simulation, emphasizing its use for modeling, visualization, and scripting.",
  "details": "
  Blender is used primarily for **3D modeling, visualization, and scripting** in robotics workflows. While not a dedicated physics simulator, it excels in:
  - Creating detailed robot and environment models.
  - Physics simulations (rigid/soft bodies, fluids).
  - Python scripting for automation and custom workflows.
  - Exporting models to other simulators (e.g., Gazebo, AirSim).
  The integration involves leveraging Blender’s Python API (`bpy`) for automation and custom tools, alongside add-ons like DroneCam for real-time drone control and Skybrush Studio for choreography.
  **Key trade-offs**: Blender is strong in visualization but lacks advanced physics/sensor simulation compared to dedicated simulators like Gazebo or PyBullet.
  ",
  "key_functions": [
    {
      "name": "bpy.ops.mesh.primitive_cube_add",
      "purpose": "Creates a cube primitive for modeling in Blender."
    },
    {
      "name": "bpy.ops.rigidbody.object_add",
      "purpose": "Adds rigid body physics to an object for simulation."
    },
    {
      "name": "bpy.ops.export_scene.obj",
      "purpose": "Exports a Blender scene as an OBJ file for compatibility with other tools."
    },
    {
      "name": "bpy.app.handlers.frame_change_pre",
      "purpose": "Hooks into Blender’s animation system for real-time updates (e.g., drone animation)."
    }
  ],
  "dependencies": ["numpy", "bmesh", "mathutils", "socket", "json"],
  "usage": "
  **Basic Workflow**:
  1. **Model**: Use Blender’s Python API (`bpy`) to create/modify objects (e.g., drones, environments).
  2. **Physics**: Enable rigid/soft body physics via `bpy.ops.rigidbody.object_add`.
  3. **Animation**: Use `bpy.app.handlers.frame_change_pre` for dynamic updates (e.g., drone movement).
  4. **Export**: Convert models to formats like OBJ/URDF for simulators.
  5. **Visualize**: Import simulation results back into Blender for post-processing.
  **Example Use Cases**:
  - Pre-processing models for Gazebo/AirSim.
  - Real-time visualization of drone paths or formations.
  - Custom add-ons for robotics-specific tasks (e.g., path planning).
  ",
  "related": [
    "[[00-simulation-tools-overview.md]]",
    "[[01-full-featured-simulators.md]]",
    "[[04-ros-simulation.md]]",
    "[[08-3d-modeling-tools.md]]"
  ],
  "callouts": [
    "> [!TIP]- **Python API Advantage**: Blender’s `bpy` module allows full control over modeling/physics, enabling custom workflows like dynamic drone animations.",
    "> [!CAUTION]- **Physics Limitations**: Blender’s physics is less accurate than Gazebo/PyBullet. Use for visualization/pre-processing, not control algorithms.",
    "> [!INFO]- **Add-ons**: Extend functionality with tools like DroneCam (real-time control) or Skybrush Studio (drone choreography)."
  ],
  "code_summary": "
```python
# Example: Create a drone with propellers and physics in Blender
import bpy
import mathutils

# Clear existing objects
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# Create drone body
bpy.ops.mesh.primitive_cube_add(size=0.2, location=(0, 0, 0))
drone_body = bpy.context.active_object
drone_body.name = "DroneBody"

# Add propellers
for i in range(4):
    angle = i * math.pi / 2
    x, y = 0.15 * math.cos(angle), 0.15 * math.sin(angle)
    bpy.ops.mesh.primitive_cylinder_add(radius=0.05, depth=0.01, location=(x, y, 0.1))
    prop = bpy.context.active_object
    prop.name = f"Propeller_{i}"
    prop.parent = drone_body

# Enable physics
bpy.ops.rigidbody.world_add()
drone_body.rigid_body.type = 'ACTIVE'
drone_body.rigid_body.mass = 1.0

# Animation loop
def animate_drone(scene):
    frame = scene.frame_current
    drone_body.location.z = 1.0 + 0.5 * math.sin(frame * 0.1)
    for prop in bpy.data.objects:
        if prop.name.startswith("Propeller_"):
            prop.rotation_euler.z += 0.1
bpy.app.handlers.frame_change_pre.append(animate_drone)
```
  "
}
```
```