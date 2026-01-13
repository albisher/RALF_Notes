**Tags:** #simulation, #docker, #robotics, #ml-training, #development, #testing, #visualization, #containerization, #pybullet
**Created:** 2026-01-13
**Type:** code-notes

# HMRS_SIMULATOR_TASKS

## Summary

```
Standalone HMRS simulation container for running multi-robot physics simulations, ML training, and testing without web dependencies.
```

## Details

> The `hmrs-simulator` container is a standalone simulation environment built on Docker, designed to execute PyBullet-based HMRS simulations independently. It supports multiple drone types (Scout, Tanker-Mule, Tanker-Lifeline, Overseer, etc.) and provides manual execution capabilities for tasks like standalone simulation runs, ML training data generation, debugging, visual demonstrations, and custom script execution. The container reuses the same backend image (`hmrs-backend:latest`) for consistency but operates separately from production services. It lacks auto-restart and requires explicit manual execution via Docker Compose.

## Key Functions

### ``run_simulation.py``

Executes standalone PyBullet physics simulations in headless or GUI mode.

### ``run_ml_sessions.py``

Generates ML training datasets from simulation scenarios.

### ``verify_requirements.py``

Checks system dependencies (PyBullet, sensors, etc.) for HMRS compatibility.

### ``simple_quadcopter_visual.py``

Runs visualization demos with matplotlib to generate frames/images.

### `Custom scripts`

Allows arbitrary Python execution for one-off tasks or data analysis.

## Usage

1. **Run standalone simulation**:
   ```bash
   docker compose run --rm simulator python run_simulation.py
   ```
2. **Generate ML training data**:
   ```bash
   docker compose run --rm simulator python run_ml_sessions.py
   ```
3. **Debug/testing**:
   ```bash
   docker compose run --rm simulator bash
   python run_simulation.py
   ```
4. **Custom scripts**:
   ```bash
   docker compose run --rm simulator python your_script.py
   ```

## Dependencies

> `PyBullet`
> `Docker Compose`
> `Python 3.x`
> `X11 (for GUI support)`
> `project-specific simulation libraries.`

## Related

- [[hmrs-backend:latest]]
- [[PyBullet documentation]]
- [[HMRS system architecture]]

>[!INFO] Key Renaming
> The container was renamed from `quadcopter-simulator` to `hmrs-simulator` to reflect broader drone type support beyond quadcopters.

>[!WARNING] Manual Execution Required
> Unlike auto-starting services, this container must be manually triggered via Docker Compose (`docker compose run`). No auto-restart policy is applied.
