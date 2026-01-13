**Tags:** #live-updates, #ml-visualization, #simulation-integration, #real-time-data, #ui-development, #automation, #visualization, #multimedia
**Created:** 2026-01-13
**Type:** code-notes

# 0004-ml-scenario-ui-live-update

## Summary

```
Enhanced ML scenario UI with real-time live simulation visualization for active scenarios.
```

## Details

> This update introduces a live simulation visualization system that dynamically generates 6-panel visualizations (3D view, top view, height/velocity graphs, LiDAR scan) for ML scenarios. The system automatically starts simulations when scenarios begin, refreshes at ~10 FPS, and provides mock fallback support. The UI updates seamlessly via a `/stream` endpoint with auto-refreshing browser integration.

## Key Functions

### ``/stream` endpoint`

Generates 6-panel visualization frames (~10 FPS).

### `Automatic simulation start`

Background thread triggers live simulation on scenario activation.

### `Real-time data visualization`

Uses matplotlib for dynamic graphs and LiDAR plots.

### `Mock fallback`

Gracefully degrades if PyBullet unavailable.

## Usage

1. Run server: `python ml_scenario_ui.py` in `simulation` folder.
2. Access live UI at `http://localhost:5006`.
3. Start scenarios—visualization updates automatically in "Ongoing Scenarios."

## Dependencies

> `matplotlib`
> `PyBullet (optional)`
> `Flask (for `/stream` endpoint)`
> `HTML/CSS (UI rendering).`

## Related

- [[ml_scenario_ui]]
- [[frame_0047]]
- [[PyBullet documentation]]

>[!INFO] Important Note
> Live updates refresh every **100ms** via timestamp query (`?t=12345`), preventing browser caching.

>[!WARNING] Caution
> If PyBullet fails, the system falls back to a **mock simulator** but may reduce fidelity in 3D/LiDAR visuals.
