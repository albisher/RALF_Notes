**Tags:** #bash-script, #docker, #server-startup, #hmrs-simulation, #live-server
**Created:** 2026-01-13
**Type:** code-notes

# start_server

## Summary

```
Script to launch the HMRS simulation server using Docker or direct Python execution.
```

## Details

> This Bash script automates the startup of the HMRS (Haptic Multi-Robot Simulation) simulation server. It first checks for Docker availability and uses Docker Compose to launch the backend service in detached mode. If Docker is unavailable, it falls back to running the server via Python directly, optionally activating a virtual environment. The script includes checks for Docker’s presence, waits briefly for the server to initialize, and provides commands for manual verification and logging.

## Key Functions

### `Docker Compose Check`

Verifies Docker and runs `docker compose` for backend startup.

### `Fallback to Python`

Executes `python hmrs_simulation_live.py` if Docker is unavailable.

### `Virtual Environment Support`

Includes instructions for activating a virtual environment before running the script.

## Usage

1. Run the script directly:
   ```bash
   ./start_server
   ```
2. If Docker is unavailable, manually execute:
   ```bash
   python hmrs_simulation_live.py
   ```
   (or activate a virtual environment first).

## Dependencies

> `- Docker (optional`
> `but preferred for containerized execution)
- Python 3 (for fallback execution)
- Docker Compose (if using Docker)
- `hmrs_simulation_live.py` (main simulation script)`

## Related

- [[docker-compose]]
- [[hmrs_simulation_live]]

>[!INFO] Important Note
> The script prioritizes Docker Compose for consistency but ensures compatibility with direct Python execution. Always ensure the correct Python environment is activated if using the fallback method.

>[!WARNING] Caution
> If Docker is unavailable, the script will exit gracefully but requires manual intervention. Ensure the simulation environment is set up before running the fallback command.
