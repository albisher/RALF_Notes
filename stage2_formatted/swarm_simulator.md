**Tags:** #physics-simulation, #swarm-robotics, #pybullet, #drone-control
**Created:** 2026-01-13
**Type:** code

# swarm_simulator

## Summary

```
Simulates a drone swarm with master control, worker drones, and observer camera using PyBullet.
```

## Details

> The `SwarmSimulator` class initializes a drone swarm simulation environment with configurable physics settings. It manages a ground master (truck), multiple worker drones (default 4), and an observer camera. The simulator uses PyBullet for physics simulation, loads a building model, and integrates mission-specific configurations. Key components include physics server setup, drone creation, and simulation loop handling.

## Key Functions

### ``__init__``

Initializes the simulator with physics server, building, and drone configurations.

### ``create_ground_master``

Creates a ground master control station (truck) at a specified position.

### ``create_worker_drone``

Instantiates a worker drone with given ID and position, adding it to the swarm list.

### ``create_observer``

Sets up an observer camera to monitor the swarm.

### ``start_simulation``

Begins the simulation loop.

### ``stop_simulation``

Halts the simulation.

### ``update``

Advances physics simulation and checks for mission completion.

### ``run``

Main loop executing `update` until `stop_simulation` is called.

### ``cleanup``

Disconnects physics server and removes all simulated objects.

## Usage

1. Initialize the simulator with `SwarmSimulator(num_workers=4)`.
2. Create components (e.g., `sim.create_worker_drone(1, (0, 0, 0))`).
3. Start simulation with `sim.start_simulation()`.
4. Run the loop (e.g., in a separate thread) or call `sim.run()`.
5. Clean up with `sim.cleanup()` after use.

## Dependencies

> `pybullet`
> `pybullet_data`
> `numpy`
> `time`
> `threading`
> `.base_drone`
> `.worker_drone`
> `.observer_camera`
> `.ground_master`
> `.mission_config`
> `.model_loader`

## Related

- [[swarm_drone_base]]
- [[mission_config_example]]
- [[pybullet_physics_tutorial]]

>[!INFO] Physics Server Mode
> The simulator uses PyBullet’s `DIRECT` mode by default (headless) for performance. Switch to `GUI` mode if visual debugging is needed.

>[!WARNING] Resource Cleanup
> Ensure `cleanup()` is called to avoid memory leaks and disconnect lingering physics connections.
