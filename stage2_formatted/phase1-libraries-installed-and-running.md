**Tags:** #docker, #drone-swarm, #simulation, #collision-avoidance, #orbslam3, #mission-planning, #pyswarming, #backend-integration
**Created:** 2026-01-12
**Type:** code-notes

# phase1-libraries-installed-and-running

## Summary

```
Phase 1 open-source libraries installed in Docker backend container for drone swarm simulation, enabling collision avoidance, SLAM, and mission optimization.
```

## Details

> This document records the successful installation of Phase 1 libraries (`pyswarming`, `uav-collision-avoidance`, `orbslam3-python`, `droneops`, `DSSE`) in the `hmrs-backend` Docker container via `docker compose`. The backend container is verified running, with integrations enabling real-time collision avoidance, Visual SLAM, and mission optimization. The simulation is accessible via `http://localhost:5007`, with active boxes (`AttentionCollisionAvoidanceBox`, `VisualSLAMBox`, `MissionPlanningOptimizerBox`) applied across drones (`HMRSScoutDrone`, `HMRSTankerMuleDrone`, etc.). The setup supports obstacle avoidance, GPS-free localization, and optimized mission planning.

## Key Functions

### ``docker compose exec backend pip install ...``

Installs libraries directly in the running container.

### ``AttentionCollisionAvoidanceBox``

Implements obstacle avoidance for drones via control barrier functions.

### ``VisualSLAMBox``

Enables pose tracking and localization in GPS-denied environments.

### ``MissionPlanningOptimizerBox``

Optimizes drone missions using multi-objective algorithms.

### ``HMRSScoutDrone.update()``

Triggers automatic collision avoidance in drones.

### ``HMRSSimulationLive``

Hosts pre-flight optimization for missions.

## Usage

1. **Access Simulation**: Open `http://localhost:5007` in a browser.
2. **Test Features**:
   - **Collision Avoidance**: Spawn multiple drones near targets.
   - **Visual SLAM**: Use drones in indoor/urban canyons.
   - **Mission Planning**: Configure complex missions in `HMRSSimulationLive`.
3. **Verify Installation**: Run the provided Python verification script in the container.

## Dependencies

> ``docker``
> ``docker-compose``
> `Python 3.x (for `pip install` and verification scripts).`

## Related

- [[all-phases-integration-complete]]
- [[0020-integration-complete]]

>[!INFO] Important Note
> The backend container must be running (`docker compose up -d backend`) before installing libraries. Libraries are installed in-place to avoid breaking existing functionality.

>[!WARNING] Caution
> Manual edits to container files may invalidate Docker layer integrity. Use `docker compose exec` commands exclusively for library management.
