**Tags:** #drone_simulation, #session_management, #api_integration, #python
**Created:** 2026-01-13
**Type:** code-notes

# create_specific_drone_sessions

## Summary

```
Script to dynamically create and manage drone simulation sessions for specific drone types.
```

## Details

> This script automates the creation of simulation sessions for predefined drone types (Butterfly, Owl, Bee, Quadcopter) by interacting with a local simulation API. It handles cleanup (stopping/resetting simulations), spawns sessions with optional custom names, and spawns drones of specific types at given positions. The script relies on HTTP requests to manage simulation lifecycle and drone placement.

## Key Functions

### ``stop_simulation_if_running()``

Checks and stops any active simulation before proceeding.

### ``reset_simulation()``

Resets the simulation state to a clean state.

### ``spawn_session()``

Creates a new simulation session with configurable building count and optional session name.

### ``spawn_drone()``

Spawns a drone of a specified type (e.g., "insect_like", "quadcopter") at a given position.

### ``start_simulation()``

Starts the simulation with a default duration (180 seconds).

## Usage

1. Initialize the `SpecificDroneSessionCreator` with the base API URL.
2. Call `stop_simulation_if_running()` to ensure no active simulation exists.
3. Use `spawn_session()` to create a session (e.g., `creator.spawn_session(num_buildings=3)`).
4. Use `spawn_drone()` to place drones (e.g., `creator.spawn_drone("insect_like", [0.0, 0.0])`).
5. Optionally start the simulation with `start_simulation()`.

## Dependencies

> `requests`
> `datetime`
> `typing`
> `json (standard Python libraries)`
> `custom `DRONE_SESSIONS` list.`

## Related

- [[none]]

>[!INFO] Important Note
> The script assumes the simulation API is running on `http://localhost:5007`. Adjust `BASE_URL` if needed.

>[!WARNING] Caution
> Error handling is minimal; unexpected API failures may corrupt session state. Test thoroughly in a controlled environment.
