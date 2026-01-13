**Tags:** #data-visualization, #log-analysis, #3d-plotting, #autonomous-systems, #matplotlib
**Created:** 2026-01-13
**Type:** code-notes

# visualize_exploration

## Summary

```
Visualizes exploration data from JSON logs, comparing base station and ground truth trajectories in 2D/3D.
```

## Details

> This script dynamically loads JSON logs of exploration scenarios (simple or autonomous) to generate interactive or static plots. It first attempts to locate log files (`base_station_log.json`/`ground_truth_log.json`) in the current directory or a legacy `simulation/` folder. If found, it loads the data and attempts to use an interactive Matplotlib backend (e.g., `Qt5Agg`, `macosx`) for 3D visualization. If no interactive backend is available, it falls back to a static `Agg` backend. The script then processes the data to visualize trajectories, likely using `matplotlib` and `numpy` for plotting and numerical operations.

## Key Functions

### ``run_visualization()``

Core function that:

### ``INTERACTIVE_AVAILABLE`/`backend_used``

Checks and configures Matplotlib backend dynamically.

### ``os.path`/`json`/`numpy`/`matplotlib``

Core dependencies for path handling, JSON parsing, numerical operations, and plotting.

## Usage

1. Run the script after executing a scenario (e.g., `python scenarios/exploration/simple-exploration/simple_exploration_test.py`).
2. The script automatically detects and loads relevant log files.
3. Visualizations are generated based on the loaded data. Interactive plots require a compatible backend (e.g., `PyQt5` on macOS).

## Dependencies

> ``json``
> ``matplotlib.pyplot``
> ``numpy``
> ``matplotlib.mplot3d``
> ``matplotlib``
> ``os``
> ``sys``
> ``datetime``
> ``PyQt5` (optional`
> `for interactive backend).`

## Related

- [[base_station_log]]
- [[simple_exploration_test]]

>[!INFO] Interactive Backend Fallback
> If the script fails to use an interactive backend (e.g., `Qt5Agg`), it defaults to `Agg` (static plots). To enable interactive 3D plots, install `PyQt5` or use system Python on macOS.

>[!WARNING] File Existence Check
> The script exits with an error if log files (`base_station_log.json` or `ground_truth_log.json`) are missing. Ensure logs are generated before running this script.
