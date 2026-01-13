**Tags:** #autonomous-robotics, #frontier-exploration, #simulation, #3d-mapping, #swarm-intelligence
**Created:** 2026-01-13
**Type:** code-notes

# AUTONOMOUS_EXPLORATION_COMPLETE

## Summary

```
Frontier-based autonomous exploration system for drones in unknown environments using LiDAR and voxel mapping.
```

## Details

> This system implements a complete autonomous exploration framework where drones detect and navigate to unexplored frontiers in 3D environments. It uses a state machine to manage exploration phases (scanning, moving, idle) and integrates frontier detection via BFS clustering, LiDAR mapping, and collision avoidance. The test scenario spawns hidden objects and evaluates coverage metrics without predefined waypoints.

## Key Functions

### ``detect_frontiers()`** (in `FrontierExplorerBox`)`

Identifies boundaries between known/unknown space using voxel occupancy maps.

### ``select_best_frontier()`** (in `FrontierExplorerBox`)`

Scores frontiers by information gain and proximity for prioritization.

### ``_cluster_frontiers()`** (in `FrontierExplorerBox`)`

Uses BFS to group frontier voxels into clusters.

### ``_estimate_information_gain()`** (in `FrontierExplorerBox`)`

Computes heuristic scores for frontier selection.

### `State Machine** (in `ExplorationManagerBox`)`

Orchestrates transitions between idle, scanning, moving, and completed states.

## Usage

1. Initialize the system with a drone and LiDAR setup.
2. Run the test scenario (`autonomous_exploration_test.py`), which spawns hidden objects and triggers autonomous exploration.
3. Monitor metrics (LiDAR points, waypoints, map size) to evaluate coverage and frontier discovery.

## Dependencies

> ``/simulation/swarm/boxes/frontier_explorer_box.py``
> ``/simulation/swarm/boxes/exploration_manager_box.py``
> ``/simulation/swarm/boxes/advanced_liдар_box.py``
> ``/simulation/swarm/boxes/attention_collision_avoidance_box.py``
> ``simple_exploration_test.py` (GroundTruthLogger`
> `BaseStation).`

## Related

- [[`simple_exploration_test]]
- [[frontier_explorer_box]]
- [[exploration_manager_box.py`.]]

>[!INFO] Important Note
>Frontiers are detected as voxels with at least one empty 26-connected neighbor, ensuring accurate boundary detection. The BFS clustering ensures contiguous frontier regions are grouped for efficient navigation.


>[!WARNING] Caution
>LiDAR noise (±3cm) may introduce false positives in frontier detection. Tested with 50m range but adjustable for real-world constraints.
