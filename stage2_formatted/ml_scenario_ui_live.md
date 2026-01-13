**Tags:** #flask, #real-time, #simulation, #pybullet, #multirotor, #live-visualization, #mock-mode, #threading, #ml-integration
**Created:** 2026-01-13
**Type:** code-notes

# ml_scenario_ui_live

## Summary

```
Live ML scenario visualization dashboard with PyBullet/Python mock fallback for quadcopter simulations.
```

## Details

> This Flask-based web application provides a live visualization interface for ML-driven quadcopter simulations. When PyBullet is unavailable, it falls back to a mock simulation using a `MockSimulator` class. The UI renders six-panel frames (matching `frame_0047.png`) showing quadcopter positions, velocities, and trajectory history. A threading-based simulation loop updates data in real-time, while the `MLScenarioManager` handles scenario configuration.

## Key Functions

### ``MockSimulator``

Fallback class for quadcopter state simulation when PyBullet is unavailable.

### ``create_quadcopter()``

Initializes a mock quadcopter with default position/velocity.

### ``get_quadcopter_state(quad_id)``

Returns current state (position/velocity) of a quadcopter.

### ``step()``

Updates quadcopter positions/velocities in a cyclic motion pattern.

### ``generate_simulation_frame()``

(Incomplete snippet) Generates a multi-panel visualization frame (6 panels) for rendering quadcopter data (likely using Matplotlib).

### ``simulation_thread``

Background thread managing real-time simulation updates (threading.Lock ensures thread-safe access to shared data).

### ``scenario_manager``

Manages loaded ML scenarios from `config/ml_scenarios.json`.

## Usage

1. Run with `PYBULLET_AVAILABLE=True` for real simulation or `PYBULLET_AVAILABLE=False` for mock mode.
2. Access via Flask endpoint (e.g., `http://localhost:5000`).
3. Use `MLScenarioManager` to load/switch scenarios.
4. Frontend renders live quadcopter data in six-panel frames.

## Dependencies

> ``flask``
> ``numpy``
> ``matplotlib``
> ``pybullet` (optional)`
> ``swarm.ml_scenario_manager``
> ``pybullet_data`.`

## Related

- [[ml_scenario_manager]]
- [[swarm_project_overview]]

>[!INFO] Thread Safety Note
> The `frame_lock` ensures thread-safe updates to `quadcopters`, `positions_history`, and `time_history` during simulation.

>[!WARNING] Mock Mode Limitation
> Mock simulation lacks physics realism; use PyBullet for accurate flight dynamics.
