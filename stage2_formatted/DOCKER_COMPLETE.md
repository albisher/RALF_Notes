**Tags:** #docker, #self-contained, #python, #simulation, #dependency-management, #containerization, #pybullet, #nodenv, #headless
**Created:** 2026-01-13
**Type:** code-notes

# DOCKER_COMPLETE

## Summary

```
Self-contained Docker environment for Python simulations with PyBullet, ensuring no virtual environment dependencies.
```

## Details

> This document describes a fully independent Docker setup for running Python simulations, particularly for robotic or physics-based applications. The environment avoids virtual environments (`venv`) entirely, installing all Python packages directly into the container’s system Python (e.g., `/usr/local/bin/python`). The architecture leverages a lightweight `python:3.10-slim` base image, pre-installed with system dependencies like `build-essential`, `cmake`, and graphics libraries (`libgl1`). Key packages (`pybullet`, `numpy`, `matplotlib`, `opencv-python`) are installed system-wide, ensuring compatibility across platforms (including macOS). The setup includes verification steps to confirm all dependencies work without host interference, such as running a Python script that imports `pybullet` and `numpy` directly inside the container.

## Key Functions

### ``docker-compose build``

Builds the Docker image with pre-installed dependencies.

### ``docker compose run --rm simulator python <script>``

Executes a Python script inside the container, leveraging the pre-installed packages.

### ``docker-run.sh``

A convenience script to simplify container execution (likely a wrapper for `docker-compose`).

### ``Dockerfile``

Defines the container with system-level Python package installation and system dependencies.

### ``docker-compose.yml``

Configures multi-container orchestration (if applicable) and resource allocation for the `simulator` service.

## Usage

1. **Build the container**:
   ```bash
   docker-compose build
   ```
2. **Run a simulation script** (e.g., a quadcopter demo):
   ```bash
   docker compose run --rm simulator python simple_quadcopter.py --headless
   ```
3. **Verify installation**:
   ```bash
   docker compose run --rm simulator pip list  # List installed packages
   docker compose run --rm simulator python -c "import pybullet; print('✅ Works!')"  # Test PyBullet
   ```
4. **Use the convenience script**:
   ```bash
   ./docker-run.sh  # Executes a pre-defined command (likely `docker-compose`).
   ```

## Dependencies

> `- Docker Engine
- Docker Compose
- Python 3.10 (included in `python:3.10-slim`)
- System libraries: `build-essential``
> ``cmake``
> ``libgl1``
> ``libglib2.0-0``
> ``opencv-python`
- Python packages: `pybullet``
> ``numpy``
> ``matplotlib``
> ``opencv-python``

## Related

- [[DOCKER_INDEPENDENT]]
- [[DOCKER_SETUP]]

>[!INFO] Key Advantage
> This setup eliminates dependency conflicts (e.g., PyBullet failures on macOS) by isolating Python packages into the container’s system environment, avoiding host Python or `venv` entirely.


>[!WARNING] Platform Considerations
> Ensure Docker and Docker Compose are installed and running. The `python:3.10-slim` base image may require additional system libraries (e.g., `libgl1`) for graphics-dependent packages like `pybullet`. Test on target platforms before deployment.
