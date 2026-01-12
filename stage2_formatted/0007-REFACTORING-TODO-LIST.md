**Tags:** #refactoring, #autonomous_exploration, #box_pattern, #code_reduction, #lidar, #visualization, #simulation, #swarm_robotics, #duplication_elimination
**Created:** 2026-01-12
**Type:** code-notes

# refactoring_todo_list

## Summary

```
A phased refactoring TODO list for autonomous exploration systems to improve modularity and reduce code duplication.
```

## Details

> This document outlines a **3-week phased refactoring plan** to achieve **90%+ compliance with the Box Pattern**, eliminating redundant code across simulation modules. Phase 1 focuses on **critical boxes** (Weeks 1–3) by creating reusable components like `LiDARScannerBox`, `VisualizationBox`, and `GroundTruthLoggerBox`. Each task targets specific files, removes duplication, and ensures modularity while maintaining functionality. The goal is to reduce redundant lines by consolidating logic into standardized classes.

## Key Functions

### `LiDARScannerBox`

Handles LiDAR sensor operations (ray casting, noise simulation, scan statistics).

### `VisualizationBox`

Manages 3D plot generation, point cloud rendering, and path visualization with configurable styles.

### `GroundTruthLoggerBox`

Logs and exports ground-truth data for validation in autonomous exploration scenarios.

## Usage

1. **Implement Phase 1 tasks sequentially** (critical boxes first).
2. **Replace legacy functions** (e.g., `_lidar_scan()`) with new box instances.
3. **Test each box** in isolation before merging into scenarios.
4. **Validate all scenarios** post-refactoring to ensure no regression.

## Dependencies

> `- `/simulation/swarm/boxes/` (parent directory for new box classes)
- `PyBullet` (for physics testing)
- `matplotlib`/`plotly` (for visualization plotting)
- `scenarios/simple_exploration_test.py``
> ``autonomous_exploration_test.py``
> ``autonomous_exploration_live.py` (targeted files for updates)`

## Related

- [[simulation_swarm_architecture]]
- [[autonomous_exploration_system_overview]]

>[!INFO] Critical Impact
> Eliminating 210+ lines of duplication in **LiDARScannerBox** alone reduces redundancy significantly, improving maintainability and scalability for future swarm expansions.

>[!WARNING] Testing Priority
> **PyBullet physics testing** is mandatory for `LiDARScannerBox`—skipping this risks introducing physics inconsistencies in real-world simulations.

>[!INFO] Style Configuration
> `VisualizationBox` must support **dark/light/professional** themes to avoid hardcoding colors, ensuring flexibility for different use cases.
