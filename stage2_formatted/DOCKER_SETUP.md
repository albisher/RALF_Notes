**Tags:** #docker, #simulation, #pybullet, #macos, #headless, #x11, #containerization, #dependency-management
**Created:** 2026-01-13
**Type:** code-notes

# DOCKER_SETUP

## Summary

```
Self-contained Docker environment for running PyBullet simulations with pre-installed dependencies, avoiding macOS compilation issues.
```

## Details

> This Docker setup provides an isolated Python environment with PyBullet and all required dependencies pre-installed in a container. It avoids macOS-specific compilation challenges by leveraging Docker’s containerization capabilities. The container uses a lightweight base image (`python:3.10-slim`) and installs packages directly via `pip`, eliminating the need for a virtual environment (`venv`) inside the container. The `simulation/` directory is mounted into the container, enabling live code changes and seamless file access between host and container.

## Key Functions

### ``docker compose build``

Builds the Docker image with PyBullet and dependencies.

### ``docker compose run --rm simulator python run_simulation.py``

Executes the main simulation script inside the container.

### ``docker-compose run --rm simulator python verify_requirements.py``

Validates installed dependencies.

### ``docker-compose run --rm simulator bash``

Opens an interactive shell inside the container for debugging.

### ``Dockerfile``

Defines the container configuration, including base image, Python version, and package installation.

### ``requirements.txt``

Lists all dependencies for PyBullet and related libraries.

## Usage

1. Navigate to the `simulation/` directory and run `docker compose build` to build the image.
2. Use `docker compose run --rm simulator python <script>` to execute simulations (e.g., `run_simulation.py`).
3. For GUI support on macOS, install XQuartz and forward the display (`DISPLAY=host.docker.internal:0`).
4. For headless mode, omit the GUI flag (e.g., `--headless`).

## Dependencies

> `- Docker Compose`
> `Docker CLI`
> ``python:3.10-slim``
> `PyBullet 3.2.7`
> `NumPy`
> `Matplotlib`
> `OpenCV`
> `XQuartz (macOS GUI support).`

## Related

- [[Dockerfile]]
- [[requirements]]
- [[PyBullet Documentation]]
- [[XQuartz Installation Guide]]

>[!INFO] Important Note
> The container uses a **direct `pip` installation** of packages at the system level, not a virtual environment (`venv`). This ensures compatibility with PyBullet but requires careful dependency management.


>[!WARNING] Caution
> On macOS, **XQuartz must be installed** and `xhost +localhost` enabled for GUI applications to work. Failure to do so will result in display errors.
