**Tags:** #open-source, #simulation, #robotics, #HMRS, #drone, #multi-robot, #python, #hardware-in-loop, #ROS, #sensor-simulation, #physics-simulation
**Created:** 2026-01-12
**Type:** research

# 00-simulation-tools-overview

## Summary

```
Research document mapping open-source simulation tools for HMRS window-cleaning project, prioritizing Python, performance, and real-time capabilities.
```

## Details

> This document serves as a high-level overview of open-source simulation frameworks tailored for the Heterogeneous Multi-Robot System (HMRS) window cleaning project. It categorizes tools based on their primary use cases—such as full robotics simulators, Python-based environments, ROS/ROS2 integration, and sensor simulation—while emphasizing computational efficiency, real-time feedback, and hardware-in-the-loop (HITL) support. The research focuses on balancing accuracy with performance, avoiding photorealistic rendering in favor of fast iteration and realistic physics/sensor emulation.
> 
> The document links to detailed sections for each category, ensuring further exploration of specific tools like Gazebo, PyBullet, or ROS2-based simulations. It also highlights academic and CAD tools for 3D modeling and asset conversion, bridging simulation and real-world deployment.

## Key Functions

### `Executive Summary`

Highlights key priorities (Python, performance, real-time, HITL) and research scope.

### `Research Categories`

Organizes tools into structured groups (e.g., Gazebo, ROS2, sensor simulation).

### `Performance Prioritization`

Guides selection based on computational efficiency and accuracy trade-offs.

### `HITL Integration`

Emphasizes compatibility with real hardware for testing and validation.

## Usage

Read as a reference for selecting simulation tools. Use linked sections (e.g., `01-full-featured-simulators.md`) to dive deeper into specific tools. Apply findings to evaluate which tools best fit HMRS requirements (e.g., Python support, multi-robot coordination).

## Dependencies

> `None (documentation-focused; links to external resources for tool-specific dependencies).`

## Related

- [[01-full-featured-simulators]]
- [[02-python-simulators]]
- [[04-ros-simulation]]
- [[05-sensor-simulation]]
- [[06-hardware-in-loop]]
- [[07-academic-research-tools]]
- [[08-3d-modeling-tools]]
- [[13-3d-isometric-game-assets]]
- [[14-image-to-game-assets-conversion]]

>[!INFO] Performance Trade-off
> Prioritize tools like PyBullet or Ignition Gazebo for speed/accuracy over visual fidelity. Avoid over-engineering for simulation quality—focus on physics and sensor realism.

>[!WARNING] Hardware Dependency
> HITL tools (e.g., PX4 SITL) require real hardware or emulated devices. Test compatibility early to avoid integration bottlenecks.
