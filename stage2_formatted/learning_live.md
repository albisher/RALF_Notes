**Tags:** #flask, #pybullet, #drones, #real-time-simulation, #swarm-robotics, #machine-learning, #threading, #visualization
**Created:** 2026-01-13
**Type:** code-notes

# learning_live

## Summary

```
A real-time drone swarm simulation with automated spawning and learning visualization.
```

## Details

> This script initializes a **LiveLearningSimulator** that integrates **PyBullet** for physics simulation, **Flask** for a web interface, and **Matplotlib** for 3D visualization. It manages drone spawning, task assignment, and learning progression in a swarm environment. The simulator uses a **threading.Lock** to safely handle concurrent operations, while a **Flask server** (port 5005) provides a web interface for controlling spawning, scenario selection, and visualization. The `LearningSimulator` component handles drone behavior and learning dynamics, while spawning logic enforces constraints like `max_drones` and randomized configurations (positions, orientations, weather, tasks).

## Key Functions

### ``__init__``

Initializes the simulator with default mission configurations, spawning settings, and scenario selections. Sets up visual and learning states.

### ``generate_frame_image``

(Incomplete snippet) Generates a 3D visualization frame using Matplotlib for rendering the drone swarm and simulation state.

### ``LearningSimulator``

(External dependency) Core physics/learning engine for drone behavior and task execution.

### ``ScenarioType``

(External dependency) Defines predefined drone movement scenarios (e.g., `base_to_building`).

### ``WeatherCondition``

(External dependency) Manages environmental factors like wind or rain affecting drone performance.

## Usage

1. **Run the simulator**:
   ```bash
   python learning_live.py
   ```
2. **Access the web interface**: Open `http://localhost:5005` in a browser to control spawning, scenarios, and visualize drones.
3. **Manual spawning**: Use the Flask API to trigger drone spawns via HTTP requests (e.g., `/spawn` endpoint).
4. **Customize settings**: Modify `MissionConfig`, `ScenarioType`, or `WeatherCondition` in `swarm/` modules for dynamic behavior.

## Dependencies

> ``pybullet``
> ``pybullet_data``
> ``numpy``
> ``matplotlib``
> ``flask``
> ``swarm.scenario_generator``
> ``swarm.learning_simulator``
> ``swarm.weather_system``
> ``swarm.mission_config``
> ``swarm.mission_tasks``

## Related

- [[swarm]]
- [[swarm]]
- [[swarm]]

>[!INFO] Threading Safety
> The `frame_lock` ensures thread-safe updates to visualization state (e.g., drone positions) when multiple threads (e.g., Flask requests, PyBullet physics) access `self.current_frame`.

>[!WARNING] Incomplete Frame Generation
> The `generate_frame_image` method is truncated; it must be completed to render drone trajectories and learning metrics (e.g., task completion rates) in real-time. Ensure `self.learning_sim.get_learning_stats()` returns structured data (e.g., `dict` with keys like `drones`, `tasks`, `weather`).
