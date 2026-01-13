**Tags:** #drone-configuration, #aerial-research, #tanker-mule, #sensor-config, #battery-specs
**Created:** 2026-01-13
**Type:** code-notes

# tanker_mule_config

## Summary

```
Research-based drone configuration for HMRS Tanker Mule drone, defining physical, battery, and mission parameters.
```

## Details

> This file defines a `TankerMuleConfig` dataclass encapsulating research-derived specifications for an octocopter-based drone designed for heavy-lift missions. It includes physical attributes (mass, thrust, motor count), battery metrics (capacity, voltage), mission thresholds (fluid detection), and sensor defaults. The `__post_init__` method auto-populates a `SensorConfig` if none is provided, while class methods (`from_research_specs`, `get_battery_config`, `get_drone_specs`) expose configurable data structures.

## Key Functions

### ``TankerMuleConfig``

Core dataclass holding all drone configurations.

### ``__post_init__``

Initializes `sensor_config` via `SensorConfig.from_research_specs()` if missing.

### ``from_research_specs``

Factory method returning defaults aligned with research specs.

### ``get_battery_config``

Returns a dictionary of battery parameters (capacity, voltage, charge).

### ``get_drone_specs``

Returns a dictionary of physical drone specs (mass, thrust, motors, battery life).

## Usage

```python
# Initialize with defaults
config = TankerMuleConfig()

# Override specific values
config = TankerMuleConfig(mass=130.0, max_thrust=220.0)

# Access data via methods
battery_data = config.get_battery_config()
drone_data = config.get_drone_specs()
```

## Dependencies

> ``.sensor_config` (local module)`
> ``dataclasses` (Python standard library)`
> ``typing` (Python standard library).`

## Related

- [[research_specs_tanker_mule]]
- [[sensor_config]]

>[!INFO] Default Sensor Handling
> If `sensor_config` is not provided, `__post_init__` automatically initializes it using `SensorConfig.from_research_specs()`.

>[!WARNING] Research-Based Values
> Values like `mass` (120–150 kg) and `battery_life` (62 min) are research-derived; adjust for real-world testing.
