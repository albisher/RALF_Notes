**Tags:** #docker, #simulation, #physics, #multirotor, #hardware-in-the-loop, #HMRS, #no-venv
**Created:** 2026-01-13
**Type:** tutorial

# 0001-quick-start

## Summary

```
Quick guide to setting up a Docker-based simulation environment for hardware-in-the-loop systems without requiring Python or virtual environments.
```

## Details

> This guide provides a streamlined 3-step process to deploy a pre-configured Docker container with all necessary dependencies for running a quadcopter simulation. The environment leverages PyBullet for physics simulation, NumPy for numerical tasks, and includes OpenCV for image processing. The Docker container eliminates the need for manual dependency installation or Python environment management, ensuring portability across systems.

## Key Functions

### ``docker-compose build``

Builds the Docker image from the `simulation` directory (only required once).

### ``docker compose run --rm simulator python simple_quadcopter.py --headless``

Executes the quadcopter simulation in headless mode (recommended for performance).

### ``docker compose run --rm simulator python verify_requirements.py``

Validates that all dependencies (e.g., PyBullet, NumPy) are correctly installed in the container.

### ``docker compose run --rm simulator python run_visual_save.py``

Runs a visual demo, saving frames for later analysis.

## Usage

1. Navigate to the `simulation` directory.
2. Run `docker-compose build` to create the container image.
3. Execute simulations via `docker compose run --rm simulator python <script>` (e.g., `simple_quadcopter.py`).
4. Verify dependencies with `verify_requirements.py`.

## Dependencies

> `PyBullet 3.2.7`
> `NumPy 2.2.6`
> `Matplotlib 3.10.8`
> `OpenCV 4.12.0.88`
> `Docker Compose`
> `All HMRS Requirements.`

## Related

- [[README]]

>[!INFO] Important Note
> The `--headless` flag skips GUI rendering, improving speed. Useful for automated testing or performance benchmarks.

>[!WARNING] Caution
> Ensure Docker is running before executing commands. Missing Docker will result in build failures. The container must be built first to avoid dependency conflicts.
