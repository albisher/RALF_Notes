# 00-hmrs-drones-specifications-table

RAW MODEL OUTPUT (JSON error):

```text
```json
{
  "filename": "00-hmrs-drones-specifications-table",
  "tags": ["#drone-specs", "#hmsr", "#ros2", "#autonomous", "#window-cleaning"],
  "type": "code-notes",
  "summary": "Comprehensive specifications table for HMRS drones, detailing roles, sensors, flight capabilities, and ROS2 communication protocols for vertical-surface window cleaning operations.",
  "details": "
  The document outlines specifications for four HMRS drones: **THE SCOUT**, **THE TANKER (Mule)**, **THE TANKER (Lifeline)**, and **THE OVERSEER**. Each drone serves distinct roles in a heterogeneous multi-robot system for vertical-surface window cleaning.
  - **THE SCOUT** focuses on dynamic mapping and hazard detection using LiDAR, depth cameras, and RTK GPS.
  - **THE TANKER variants** handle logistics (fluid resupply and tether management).
  - **THE OVERSEER** ensures quality assurance and safety with polarization cameras and bird deterrence.
  The system uses ROS2 with DDS for real-time communication, with a master ground station coordinating tasks across drones. Battery life, payload capacity, and environmental resilience (IP ratings, temperature ranges) are critical parameters.
  ",
  "key_functions": [
    {
      "name": "Dynamic Mapping (THE SCOUT)",
      "purpose": "Generates centimeter-accurate 3D surface maps using LiDAR (Velodyne VLP-16) and photogrammetry with depth cameras, enabling real-time obstacle detection and hazard identification."
    },
    {
      "name": "Autonomous Logistics (THE TANKER - Mule/Lifeline)",
      "purpose": "Manages fluid and payload resupply via autonomous docking (Mule) or tether management (Lifeline), with real-time tension control and obstacle avoidance."
    },
    {
      "name": "Quality Assurance (THE OVERSEER)",
      "purpose": "Performs real-time inspection using polarization cameras and bird deterrence via acoustic emitters, ensuring cleaning quality and safety compliance."
    },
    {
      "name": "ROS2 DDS Communication (Master-Drone Bridge)",
      "purpose": "Enables low-latency (<50ms) data exchange between drones and the master ground station using Fast DDS/Cyclone DDS, with reliable QoS policies for critical tasks."
    }
  ],
  "dependencies": [
    "ROS2 (with DDS/Cyclone DDS)",
    "PX4/ArduPilot Flight Controllers",
    "Velodyne VLP-16 LiDAR (or Ouster OS1/OS2)",
    "Intel RealSense D455 Depth Camera",
    "CUAV C-RTK 9Ps/Here+ V2 RTK GPS",
    "Sony IMX250MZR Polarization Camera",
    "Load Cells/Force/Torque Sensors",
    "5G Mesh/WiFi 6 Networking",
    "High-capacity Li-ion Batteries"
  ],
  "usage": "
  **Setup:**
  1. Configure master ground station with mission parameters (building CAD model, geofencing, RTH coordinates).
  2. Deploy drones based on mission requirements (e.g., 1 Scout + 1 Tanker-Mule + 1 Overseer).
  3. Initialize ROS2 nodes with DDS agents for inter-drone communication.
  4. Execute mission workflows:
     - **Scout:** Pre-mission mapping → real-time mapping → obstacle detection.
     - **Tanker:** Fluid monitoring → autonomous docking → resupply.
     - **Overseer:** Follow cleaned path → quality inspection → bird deterrence.
  5. Monitor mission progress via ROS2 topics (e.g., `/scout/surface_map`, `/overseer/qa_alert`).
  **Key Topics:**
  - `/scout/surface_map` (3D maps for climber)
  - `/tanker/cartridge_status` (resupply status)
  - `/overseer/coverage_report` (inspection results)
  **Emergency Handling:**
  - Trigger `RTH` via master ground station or drones' emergency abort commands.
  **Optimization:**
  - Adjust motor management (e.g., reduce motor power during forward flight).
  - Upgrade batteries (Li-S or high-energy-density LiPo) for extended flight time.
  ",
  "related": [
    "[[0023-drone-efficiency-enhancements.md]]",
    "[[research/HMRS/]]"
  ],
  "callouts": [
    "> [!INFO]- **Key Drone Roles:**
      - **Scout:** Preemptive mapping to reduce climber risk.
      - **Tanker:** Critical for fluid/payload resupply (Mule swaps cartridges; Lifeline manages tether).
      - **Overseer:** Real-time quality control and safety monitoring.
    ",
    "> [!INFO]- **ROS2 DDS Configuration:**
      - Uses **Micro XRCE-DDS Agent** for PX4→ROS2 bridge.
      - QoS policies enforce **RELIABLE** commands and **BEST_EFFORT** LiDAR streams.
    ",
    "> [!INFO]- **Environmental Resilience:**
      - IP55/IP67-rated drones for harsh vertical-surface conditions.
      - Operates in **-20°C to 50°C** temperature range.
    ",
    "> [!INFO]- **Tethered Power (Lifeline):**
      - Unlimited battery life via active tether management (15N tension).
      - Backup battery ensures fail-safe operation.
    "
  ],
  "code_summary": "
```python
# Example ROS2 DDS Agent Configuration (PX4 to ROS2 Bridge)
import rclpy
from dds_agent import DDSAgent
from rclpy.node import Node

class DroneNode(Node):
    def __init__(self):
        super().__init__('hmrs_drone')
        self.dds_agent = DDSAgent(
            domain_id=1,
            participant_qos=1,
            publisher_qos=2,
            subscriber_qos=3,
            reliability=4  # RELIABLE for critical commands
        )
        self.dds_agent.start()

    def publish_surface_map(self, map_data):
        self.dds_agent.publish('/scout/surface_map', map_data)

    def subscribe_to_fluid_level(self, callback):
        self.dds_agent.subscribe('/climber/fluid_level', callback)

def main():
    rclpy.init()
    drone = DroneNode()
    drone.publish_surface_map({'type': '3D_map', 'accuracy': 'centimeter'})
    drone.subscribe_to_fluid_level(lambda level: print(f'Fluid level: {level}%'))
    rclpy.spin(drone)
    drone.dds_agent.stop()
    rclpy.shutdown()
```
"
}
```
```