**Tags:** #bash-script, #docker, #simulation, #live-testing, #quadcopter
**Created:** 2026-01-13
**Type:** code-notes

# run_live

## Summary

```
A Bash script to launch a live simulation environment using Docker Compose.
```

## Details

> This script automates the setup and execution of a live simulation of a quadcopter system. It sets up the environment by navigating to the parent directory of the script, then runs a Docker Compose service (`simulator`) mapped to port `5000` using a predefined Python script (`simple_quadcopter_live.py`). The script includes error handling (`set -e`) and provides user feedback via terminal output, including the simulation URL and instructions to stop it.

## Key Functions

### ``set -e``

Exits script on any error.

### ``SCRIPT_DIR``

Determines the directory of the script for relative path resolution.

### ``SIMULATION_DIR``

Resolves the root directory of the simulation project.

### ``docker compose``

Executes the Docker Compose command to run the simulation container.

## Usage

1. Navigate to the directory containing `run_live`.
2. Execute the script: `./run_live`.
3. The simulation will start at `http://localhost:5000`. Press `Ctrl+C` to stop.

## Dependencies

> `docker`
> `docker-compose`
> ``simple_quadcopter_live.py` (Python script for the quadcopter simulation)`
> ``docker/docker-compose.yml` (Docker Compose configuration file).`

## Related

- [[docker-compose]]
- [[simple_quadcopter_live]]

>[!INFO] Important Note
> This script assumes Docker and Docker Compose are installed and running. Ensure the `docker/docker-compose.yml` file is correctly configured for the simulation service.

>[!WARNING] Caution
> Stopping the simulation abruptly may cause data loss or resource leaks. Use `Ctrl+C` to terminate gracefully.
