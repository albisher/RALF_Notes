**Tags:** #sensor, #drone, #addon, #IMU, #physics, #noise, #simulation
**Created:** 2026-01-13
**Type:** code-notes

# sensor_addon

## Summary

```
A modular sensor addon for simulating IMU, force/torque, proximity, and acoustic sensors in drone systems.
```

## Details

> This file defines an `IMUAddon` class inheriting from `BaseAddon`, simulating an Inertial Measurement Unit (IMU) with accelerometer, gyroscope, and magnetometer components. It initializes sensor properties like update rate, noise characteristics, and physical dimensions. The `generate_data` method simulates realistic IMU readings by combining drone state data with simulated noise and bias drift, accounting for typical sensor inaccuracies. The code uses NumPy for numerical operations and random noise generation to model real-world sensor behavior.

## Key Functions

### ``IMUAddon.__init__()``

Initializes IMU attributes (update rate, noise std devs, sensor capabilities).

### ``generate_data(dt`

float) -> Dict[str, Any]`**: Simulates IMU data by combining drone state with noise/bias, returning simulated accelerations, angular velocities, and magnetometer readings.

## Usage

1. Inherit `IMUAddon` in a drone simulation or control system.
2. Call `generate_data()` to produce simulated IMU readings with noise/bias.
3. Integrate with drone state tracking for closed-loop control.

## Dependencies

> `numpy`
> `custom `base_addon` module (contains `BaseAddon` and `AddonType` classes).`

## Related

- [[sensor_types]]
- [[drone_simulation_physics]]

>[!INFO] Noise Modeling
> The code uses typical noise values (e.g., `accel_noise_std=0.01 m/s²`) but lacks manufacturer-specific specs. For accuracy, replace with real sensor specs.

>[!WARNING] Bias Drift
> Simulated bias (e.g., `accel_bias = acceleration * 0.001`) is arbitrary. In real systems, bias drift varies by sensor and environment; calibrate empirically.
