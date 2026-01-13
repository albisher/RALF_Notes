**Tags:** #simulation, #robotics, #sensor, #pybullet, #lidar, #camera, #swarm, #exploration
**Created:** 2026-01-13
**Type:** code-notes

# test_sensor_simulation

## Summary

```
Tests LiDAR and camera sensor simulation for detecting hidden buildings in a swarm exploration environment.
```

## Details

> This script simulates a drone’s sensor suite (LiDAR and camera) to detect hidden buildings using PyBullet physics engine. It generates a tower-like structure (hidden from command & control) and tests sensor data collection as the drone moves through predefined positions. The script initializes a drone, LiDAR (Velodyne VLP-16), and camera (Intel RealSense D455) to simulate real-world sensor behavior, capturing data for hidden object discovery.
> 
> The script uses a `HiddenBuildingSystem` to create an invisible building in the physics world, then moves a drone through scan positions to collect sensor data. The LiDAR and camera are initialized with specific configurations (e.g., 16 channels, ±3cm accuracy for LiDAR, 1280x720 resolution for camera).

## Key Functions

### ``HiddenBuildingSystem``

Creates and manages hidden structures in the simulation environment.

### ``LiDARAddon``

Simulates a Velodyne VLP-16 LiDAR with 16 channels, 10Hz rotation, and 100m max range.

### ``CameraProcessorBox``

Simulates an Intel RealSense D455 camera with 1280x720 resolution and 87° FOV.

### ``main()``

Orchestrates the simulation workflow: physics setup, building generation, drone placement, and sensor initialization.

## Usage

1. Run the script to initialize PyBullet, load a ground plane, and generate a hidden building.
2. Create a drone and initialize LiDAR/camera sensors.
3. Move the drone through predefined scan positions to collect sensor data.
4. Analyze sensor outputs (e.g., LiDAR points, camera frames) to detect hidden structures.

## Dependencies

> `pybullet`
> `pybullet_data`
> `numpy`
> `swarm.exploration.hidden_building_system`
> `swarm.addons.lidar_addon`
> `swarm.boxes.camera_processor_box`

## Related

- [[swarm.exploration]]
- [[swarm.addons]]
- [[swarm.boxes]]

>[!INFO] Important Note
> The hidden building is generated in the physics world but remains invisible to the command & control system. The drone’s sensors must detect it to confirm its presence.


>[!WARNING] Caution
> Ensure PyBullet is running in GUI mode (`p.connect(p.GUI)`) for visualization. If running in non-GUI mode, remove the `print("="*80)` lines to avoid console clutter.
