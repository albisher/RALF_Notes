**Tags:** #autonomous-drone, #data-logging, #visualization, #scenario-management, #drone-exploration, #simulation-output, #json-logging, #path-resolution, #backward-compatibility
**Created:** 2026-01-13
**Type:** documentation

# OUTPUT_CONFIGURATION

## Summary

```
Configures automated output handling for drone exploration scenarios, ensuring logs are saved to a standardized visualization directory.
```

## Details

> This document outlines the standardized output configuration for drone exploration scenarios, where all log files are automatically saved to `scenarios/exploration/visualization/` to facilitate visualization. The system ensures backward compatibility by checking legacy paths if primary logs are missing. Both simple and autonomous exploration scenarios generate JSON telemetry logs, with ground truth data excluded from control-and-command access.

## Key Functions

### ``GroundTruthLogger``

Logs ground truth objects to `ground_truth_log.json` in the visualization folder.

### ``BaseStation``

Records telemetry data (e.g., drone position) as `base_station_log.json` (or `_autonomous.json` for autonomous modes).

### ``visualize_exploration.py``

Renders 3D visualizations using the latest log files from the visualization directory.

### ``visualize_logs.py``

Provides 2D visualizations from JSON logs, with fallback to legacy simulation paths.

## Usage

1. **Run Scenarios**:
   - Execute `simple_exploration_test.py` or `autonomous_exploration_test.py` to generate logs.
2. **View Results**:
   - Use `visualize_exploration.py` for 3D visualization (auto-detects latest logs).
   - Use `visualize_logs.py` for 2D analysis (supports both formats).

## Dependencies

> `- Python libraries: `os``
> ``json` (standard library)`
> `custom modules (`GroundTruthLogger``
> ``BaseStation`).
- Simulation framework (e.g.`
> `Gazebo/PX4) for drone telemetry.`

## Related

- [[simple_exploration_test]]
- [[autonomous_exploration_test]]
- [[visualize_exploration]]
- [[visualize_logs]]

>[!INFO] **Automatic Path Resolution**
> The `_save()` method dynamically resolves paths using `os.path.abspath(__file__)`, ensuring logs are saved relative to the scenario’s directory (e.g., `../visualization/`).

>[!WARNING] **Legacy Fallback Risk**
> Visualization scripts check legacy paths (`simulation_dir`) if primary logs are missing, which may cause misalignment if paths are updated without backward compatibility. Test scripts thoroughly before deployment.
