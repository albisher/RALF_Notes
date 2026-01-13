**Tags:** #drone_simulation, #configuration_management, #simulation_spawner, #window_cleaning, #automation
**Created:** 2026-01-13
**Type:** code-notes

# load_and_spawn_window_cleaning_drones

## Summary

```
Manages loading saved drone configurations and spawning them in a simulation environment for window cleaning drones.
```

## Details

> This script initializes a `WindowCleaningDroneSpawner` class to handle loading preconfigured drone missions and creating simulation sessions. It interacts with a simulation server via HTTP requests, listing available configurations, loading them, and spawning drones based on those configurations. The `WindowCleaningDronePreparer` (from `prepare_window_cleaning_drones`) handles configuration file parsing and storage.

## Key Functions

### ``__init__(self, base_url`

str, config_dir: str)`**: Sets up the spawner with server URL and config directory, initializing the drone preparer.

### ``load_mission_config(self, config_filename`

str)`**: Loads a saved configuration file into a dictionary using the preparer.

### ``list_available_configs(self)``

Retrieves a list of saved configuration filenames from the preparer.

### ``create_session(self, num_buildings`

int, session_name: str)`**: Initiates a new simulation session with specified buildings, returning the session ID if successful.

### ``spawn_drone_from_config(self, drone_config`

Dict[str, Any])**: *(Incomplete in snippet; likely intended to spawn drones with loaded configurations.)*

## Usage

1. Initialize the spawner with a base URL and config directory.
2. List available configs: `spawner.list_available_configs()`.
3. Load a config: `config = spawner.load_mission_config("config.json")`.
4. Create a session: `session_id = spawner.create_session(num_buildings=3)`.
5. Spawn drones (if implemented): `spawner.spawn_drone_from_config(config)`.

## Dependencies

> ``json``
> ``time``
> ``requests``
> ``pathlib``
> ``typing``
> ``prepare_window_cleaning_drones` (custom module).`

## Related

- [[`prepare_window_cleaning_drones`]]
- [[`simulation_server_api` (hypothetical server documentation).]]

>[!INFO] Important Note
> The `spawn_drone_from_config` method is incomplete in the snippet and may require additional logic to integrate with the simulation server’s drone-spawning API.


>[!WARNING] Caution
> Ensure the `base_url` points to a running simulation server. Timeout errors may occur if the server is unavailable.
