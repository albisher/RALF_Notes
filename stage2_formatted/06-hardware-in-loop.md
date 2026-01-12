**Tags:** #hardware-in-loop, #simulation, #autopilot, #PX4, #real-time-testing, #HITL, #sensors, #ROS2, #MAVSDK, #gazebo
**Created:** 2026-01-12
**Type:** documentation

# 06-hardware-in-loop

## Summary

```
Explains PX4 Hardware-in-the-Loop (HITL) and Software-in-the-Loop (SITL) setups for realistic drone testing.
```

## Details

> This document details **Hardware-in-the-Loop (HITL)** and **Software-in-the-Loop (SITL)** configurations for PX4 autopilots. SITL runs the real firmware in a simulated environment (e.g., Gazebo) without hardware, enabling control algorithm testing. HITL connects real hardware to a simulator for realistic sensor/environment testing. Key components include Gazebo for simulation, MAVSDK for Python integration, and ROS2 with MAVROS2 for ROS-based control.

## Key Functions

### ``make px4_sitl gazebo-classic``

Starts PX4 SITL with Gazebo simulation.

### ``make px4_sitl gazebo-classic_iris``

Runs SITL for a specific vehicle model (e.g., Iris).

### ``asyncio.run(run())` (MAVSDK)`

Connects to SITL via UDP and controls drone via offboard mode.

### ``ros2 launch mavros px4.launch.py``

Launches MAVROS2 for ROS2 integration with SITL.

### ``PX4Controller` (ROS2)`

Publishes position setpoints to control drone via MAVROS2.

## Usage

1. **SITL Setup**:
   - Clone PX4 repo and install dependencies.
   - Run `make px4_sitl gazebo-classic` to start simulation.
   - Use MAVSDK/ROS2 to interact with the simulated drone.

2. **HITL Setup**:
   - Requires real PX4 hardware (e.g., flight controller).
   - Connect hardware to Gazebo via UDP/ROS2 interfaces.
   - Test real autopilot behavior with simulated sensors/environment.

## Dependencies

> `- PX4-Autopilot GitHub repo (recursively cloned)`
> `- Gazebo Classic (for SITL)`
> `- MAVSDK (Python)`
> `- ROS2 (Humble)`
> `MAVROS2`
> `- Python libraries (`python3-pip``
> ``pip3 install --user -r Tools/setup/requirements.txt`).`

## Related

- [[PX4 Documentation]]
- [[MAVROS2 Guide]]
- [[Gazebo User Guide]]

>[!INFO] Important Note
> SITL is ideal for **algorithm development** (e.g., PID tuning) due to full control over simulated sensors/environment. Hardware (HITL) is needed for **real-world robustness testing** (e.g., sensor noise, power constraints).


>[!WARNING] Caution
> Ensure **firewall rules** allow UDP traffic (e.g., port `14540`) for SITL/ROS2 connections. Misconfigured ports may break communication. Always verify **vehicle model compatibility** (e.g., `iris` vs. `classic`).
