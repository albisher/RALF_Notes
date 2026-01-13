**Tags:** #drone-simulation, #energy-model, #battery-management, #physics-based
**Created:** 2026-01-13
**Type:** code-notes

# battery_model

## Summary

```
Simulates battery energy consumption and flight time for drone simulations using physics-based power calculations.
```

## Details

> This `BatteryModel` class implements a physics-based energy model for drone batteries, tracking capacity, voltage, charge state, and power consumption. It calculates real-time power draw based on thrust, velocity, altitude, and payload mass using simplified aerodynamic and mechanical relationships. The model integrates C-rate discharge limits and environmental factors like temperature, with logging for initialization and power tracking.

## Key Functions

### ``__init__``

Initializes battery parameters (capacity, voltage, charge level) and tracks state variables (power history, flight time, voltage decay).

### ``calculate_power_consumption``

Computes instantaneous power consumption via quadratic thrust scaling, drag (velocity-dependent), altitude correction, and payload mass adjustment.

## Usage

```python
model = BatteryModel(capacity_wh=150.0, initial_charge=0.5)  # 50% charge
thrusts = [0.8, 0.8, 0.8, 0.8]  # Example thrust values
velocity = np.array([10.0, 0.0, 0.0])  # m/s
power = model.calculate_power_consumption(thrusts, velocity, 500.0, payload_mass=0.5)
```

## Dependencies

> `numpy`
> `time`

## Related

- [[drone_physics_simulation]]
- [[energy_conservation_guide]]

>[!INFO] Voltage Decay
> Voltage decreases linearly with charge state (`voltage_current = voltage * initial_charge`), simulating real-world LiPo degradation.

>[!WARNING] C-Rate Limitation
> Exceeding `max_c_rate` (default: 10.0) risks battery damage; enforce via `self.c_rate <= self.max_c_rate` checks.
