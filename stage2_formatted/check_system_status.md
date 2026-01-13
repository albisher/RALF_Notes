**Tags:** #system-monitoring, #python-api, #docker-integration
**Created:** 2026-01-13
**Type:** code-notes

# check_system_status

## Summary

```
Checks and displays real-time system health metrics for a web application and Docker containers.
```

## Details

> This script fetches and formats health statuses from a local API (`http://localhost:5007`) and Docker containers via `docker-compose`. It uses HTTP requests to query `/api/health` and `/api/state`, then processes container status via `docker ps` in JSON format. The script formats responses with emojis for clarity (e.g., ✅ for "up," ❌ for "error") and prints structured output with timestamps. Error handling ensures graceful failure if API or container checks fail.

## Key Functions

### `get_api_health()`

Fetches and parses JSON from `/api/health`; returns `None` on failure.

### `get_api_state()`

Fetches and parses JSON from `/api/state`; returns `None` on failure.

### `get_container_status()`

Executes `docker-compose ps` in JSON format, filters valid containers, and returns a list.

### `format_status()`

Maps text statuses (e.g., "up") to emoji icons (✅/❌).

### `format_running()`

Converts boolean running status to emoji (✅/⏸️).

### `print_section()`

Prints a formatted header for sections (e.g., "API Health").

### `print_key_value()`

Displays key-value pairs with indentation and formatted values (e.g., boolean → emoji).

### `main()`

Orchestrates the entire workflow, calling helper functions and printing results.

## Usage

1. Run as a standalone script (`python check_system_status.py`).
2. Outputs a timestamped summary of:
   - API health status (status, running state).
   - Docker container status (parsed from `docker-compose ps`).
3. Logs errors silently (e.g., network failures) but continues execution.

## Dependencies

> `requests`
> `json`
> `subprocess`
> `typing`
> `datetime`

## Related

- [[none]]

>[!INFO] Important Note
> The script assumes `docker-compose` is in the PATH and the `docker-compose.yml` file exists in the specified directory (`/Users/amac/Documents/code/WindowCleanner/simulation`). Adjust `BASE_URL` or `cwd` if the target environment differs.

>[!WARNING] Caution
> Timeout settings (e.g., `timeout=2` for API calls) may truncate responses if services are unresponsive. Increase timeouts for production use.
