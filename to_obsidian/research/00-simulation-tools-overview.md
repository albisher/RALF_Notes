# 00-simulation-tools-overview

RAW MODEL OUTPUT (JSON error):

```text
```json
{
  "filename": "00-simulation-tools-overview",
  "tags": ["#python", "#ros2", "#gazebo", "#simulation", "#drone", "#multi-robot", "#physics", "#sensor-simulation", "#hardware-in-loop", "#open-source"],
  "type": "code-notes",
  "summary": "Comprehensive overview of open-source simulation tools for the HMRS window cleaning project, prioritizing Python-based solutions for performance and accuracy over visual fidelity.",
  "details": "
  The document evaluates open-source simulation tools categorized by their primary use cases: full robotics simulators, Python-based simulators, Blender integrations, ROS/ROS2 tools, sensor simulations, HITL, academic/research tools, 3D modeling, and isometric game assets.
  **Key focus:** Performance (speed, headless mode) and accuracy (physics/sensor fidelity) over visual quality. Recommended stack includes PyBullet (headless) for fastest iteration, ROS2+Gazebo for sensor/ROS integration, and RotorPy for lightweight Python-based prototyping.
  **Trade-offs:** Speed vs. accuracy (e.g., RotorPy is fastest but less physics-accurate; PyBullet balances both). Headless mode is critical for all tools to maximize performance.
  **Workflow:** Proposed phased approach: RotorPy/PyBullet → PyBullet → Gazebo → Real hardware for validation.
  **Sensor focus:** LiDAR, camera, IMU, and polarization simulations are prioritized for HMRS accuracy.
  **Dependencies:** Python, ROS2, and physics engines (e.g., Bullet, Gazebo) are core dependencies.",
  "key_functions": [
    {
      "name": "PyBullet (Headless Mode)",
      "purpose": "Fast, lightweight physics simulation with headless rendering for maximum performance. Supports multi-robot coordination, GPU acceleration, and ROS2 bridge."
    },
    {
      "name": "Gazebo (Headless Mode)",
      "purpose": "Comprehensive robotics simulator with ROS2 integration, sensor simulation, and headless mode for high accuracy and performance. Best for sensor-fidelity and ROS-based workflows."
    },
    {
      "name": "RotorPy",
      "purpose": "Pure Python drone simulator with minimal overhead, ideal for rapid algorithm development. Fastest option but limited physics/sensor accuracy."
    },
    {
      "name": "ROS2 + Ignition Gazebo",
      "purpose": "Industry-standard ROS2 integration with Gazebo’s sensor and physics capabilities. Headless mode enables performance optimization."
    },
    {
      "name": "PX4 SITL/ArduPilot HITL",
      "purpose": "Hardware-in-the-loop simulation for drone control validation, compatible with all headless simulators."
    }
  ],
  "dependencies": [
    "Python 3.x",
    "PyBullet",
    "Gazebo/Ignition Gazebo",
    "ROS2",
    "RotorPy",
    "PX4/ArduPilot",
    "NVIDIA CUDA (optional for GPU acceleration)",
    "Blender (for Blender integrations)",
    "Libraries: NumPy, Matplotlib (for visualization)",
    "ROS2 DDS middleware (e.g., Micro XRCE-DDS)"
  ],
  "usage": "
  **Setup Steps:**
  1. Install dependencies (e.g., `pip install pybullet ros2cli`).
  2. Configure headless mode in simulators (e.g., PyBullet: `p.DIRECT` mode; Gazebo: `--headless` flag).
  3. Integrate with ROS2 if using Gazebo/PyBullet bridges.
  4. Develop test scenarios for drone types (Scout, Tanker, Overseer) in the recommended tools.
  5. Validate sensor models against real hardware (e.g., LiDAR/RealSense D455).
  6. Test HITL workflows with PX4/ArduPilot.
  **Example Workflow:**
  - Phase 1: Use RotorPy for control algorithm prototyping.
  - Phase 2: Switch to PyBullet headless for physics validation.
  - Phase 3: Deploy in Gazebo headless for ROS2 integration.
  - Phase 4: Validate with real hardware.
  **Key Commands:**
  - PyBullet: `python -m pybullet_client.launch --headless`
  - Gazebo: `ros2 run gazebo_ros gazebo --headless`
  - ROS2 + Gazebo: `ros2 launch gazebo_ros gazebo.launch.py --launch-prefix='--headless'`,
  ",
  "related": [
    "[[01-full-featured-simulators.md]] (Gazebo, Webots, AirSim)",
    "[[02-python-simulators.md]] (RotorPy, Drone Swarm Simulator)",
    "[[04-ros-simulation.md]] (ROS2 + Ignition Gazebo)",
    "[[05-sensor-simulation.md]] (LiDAR/RealSense D455 simulations)",
    "[[06-hardware-in-loop.md]] (PX4 SITL, ArduPilot HITL)",
    "[[09-performance-optimization.md]] (Headless mode tuning)",
    "[[13-3d-isometric-game-assets.md]] (Visualization assets for PyBullet/Matplotlib)"
  ],
  "callouts": [
    "> [!INFO]- **Performance Priority:** Headless mode is mandatory for all tools to avoid rendering overhead. Example: PyBullet’s `p.DIRECT` mode reduces execution time by 2-5x.",
    "> [!INFO]- **Sensor Accuracy:** LiDAR/camera simulations (e.g., RealSense D455) are critical for HMRS. Tools like Gazebo provide the most accurate sensor models.",
    "> [!INFO]- **Multi-Robot Support:** PyBullet and ROS2+Gazebo excel in swarm coordination. RotorPy is limited to single/drone swarms.",
    "> [!INFO]- **Hardware Integration:** PX4 SITL/ArduPilot HITL bridges simulation to real hardware, enabling closed-loop testing.",
    "> [!INFO]- **Phased Workflow:** Start with RotorPy/PyBullet for speed, then Gazebo for accuracy, and finally real hardware for validation."
  ],
  "code_summary": "
```python
# Example: PyBullet headless mode setup (Python)
import pybullet_client as p

# Connect to headless mode (no GUI)
client = p.connect(p.DIRECT)  # Fastest mode

# Load a simple drone model (example)
urdf_file = "drone.urdf"
robot_id = p.loadURDF(urdf_file, [0, 0, 0], useFixedFrame=True)

# Simulate physics loop (headless)
for _ in range(100):
    p.stepSimulation()

# Cleanup
p.disconnect()
```
"
}
```
```