**Tags:** #open-source-integration, #drone-simulation, #collision-avoidance, #SLAM, #mission-planning, #box-architecture
**Created:** 2026-01-12
**Type:** code-notes

# 

## Summary

```
Integrated Phase 1 open-source libraries into the HMRS simulation system using a modular box architecture for drone functionality.
```

## Details

> The project implemented three core open-source libraries as standalone "boxes" within the HMRS simulation framework. Each box handles a distinct drone capability:
> 1. **Attention-Based Collision Avoidance** – Uses object tracking and control barrier functions for real-time safety.
> 2. **Visual SLAM** – Implements ORB-SLAM3 for localization in GPS-denied environments.
> 3. **Mission Planning Optimizer** – Performs simulation-based optimization for drone routes and resource allocation.
> 
> The boxes integrate into existing drone classes (`HMRSScoutDrone`, `HMRSTankerMuleDrone`, etc.) via hooks in `BaseDrone.update()`. Fallback mechanisms ensure compatibility if dependencies fail.

## Key Functions

### ``attention_collision_avoidance_box.py``

- Implements `attention_collision_avoidance_box.AttentionCollisionAvoidance` class.

### ``visual_slam_box.py``

- Uses `ORB-SLAM3` for pose tracking and map management.

### ``mission_planning_optimizer_box.py``

- Integrates with `HMRSSimulationLive` for pre-flight and real-time replanning.

## Usage

1. **Install Dependencies**: Add Phase 1 libraries to `simulation/config/requirements.txt`.
2. **Integrate Boxes**: Attach boxes to drone classes via `BaseDrone.update()` hooks.
3. **Test**: Run unit tests (`test_*.py`) to validate functionality.

## Dependencies

> ``pyswarming>=1.0.0``
> ``uav-collision-avoidance>=1.0.0``
> ``orbslam3-python>=1.0.0``
> ``droneops>=1.0.0``
> ``DSSE>=1.0.0``

## Related

- [[requirements]]
- [[__init__]]

>[!INFO] **Fallback Mechanisms**
> Each box includes optional fallbacks (e.g., `pyswarming`/`uav-collision-avoidance`) to ensure compatibility if dependencies fail.

>[!WARNING] **Dependency Conflicts**
> Ensure all optional dependencies are version-compatible (e.g., `orbslam3-python>=1.0.0`). Conflicts may require manual patching.
