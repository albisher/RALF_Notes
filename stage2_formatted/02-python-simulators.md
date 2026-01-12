**Tags:** #python, #simulation, #uav, #drone, #reinforcement-learning, #lightweight, #multirobot, #control-algorithms, #open-source, #research-tools, #matplotlib, #openai-gym
**Created:** 2026-01-12
**Type:** code-notes

# 02-python-simulators

## Summary

```
Lightweight Python simulators for rapid prototyping of UAVs, drone swarms, and control algorithms.
```

## Details

> This file documents two Python-based simulators: **RotorPy** (6-DoF quadrotor dynamics) and **Drone Swarm Simulator** (multi-agent drone modeling). Both are designed for educational and research purposes, emphasizing ease of modification and compatibility with Python ML/AI frameworks. RotorPy focuses on single UAVs with built-in controllers and sensor models, while the Drone Swarm Simulator supports swarm algorithms and multi-drone interactions. Both leverage Matplotlib for visualization but lack full realism compared to Gazebo/AirSim.

## Key Functions

### ``RotorPy.vehicles.multirotor.Multirotor``

Manages 6-DoF quadrotor dynamics.

### ``RotorPy.controllers.quadrotor_control.SE3Control``

Implements state-space error-based control.

### ``DroneSwarm` (from `drone_swarms`)`

Core class for multi-drone swarm simulation.

### ``World` (RotorPy)`

Manages simulation environment and physics.

### ``DroneSwarm.step()``

Updates drone states and applies swarm algorithms.

## Usage

**RotorPy**:
1. Install via `pip install rotorpy`.
2. Initialize a `World` and `Multirotor` object.
3. Define a controller (e.g., `SE3Control`).
4. Loop over time steps, updating state and applying controls.

**Drone Swarm Simulator**:
1. Install via `pip install drone-swarms` or clone from GitHub.
2. Create a `DroneSwarm` instance with desired drone count.
3. Use built-in swarm algorithms (e.g., consensus, collision avoidance).
4. Visualize in real-time with Matplotlib/Tkinter.

## Dependencies

> `- `rotorpy` (for RotorPy)`
> `- `drone-swarms` (for Drone Swarm Simulator)`
> `- `numpy` (for numerical operations)`
> `- `matplotlib` (for visualization)`
> `- `openai-gym` (optional`
> `for RL compatibility).`

## Related

- [[rotorpy]]
- [[drone-swarms]]

>[!INFO] **Educational Focus**
> Both simulators prioritize simplicity and documentation, making them ideal for teaching control theory, swarm intelligence, and Python-based prototyping. RotorPy’s Matplotlib plots are basic but sufficient for learning; consider extending with PyQt for richer visuals.


>[!WARNING] **Physics Limitations**
> RotorPy’s physics models are simplified (e.g., no wind/terrain effects). For production, integrate with Gazebo/AirSim for realism. Drone Swarm Simulator’s physics are even more basic—validate swarm behaviors empirically.
