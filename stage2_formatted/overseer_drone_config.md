**Tags:** #drone-configuration, #sensor-management, #research-specs, #battery-management, #autonomous-systems
**Created:** 2026-01-13
**Type:** code-notes

# overseer_drone_config

## Summary

```
Defines research-based specifications for HMRS Overseer drone, including physical, battery, mission, and bird deterrent parameters.
```

## Details

> This file defines a `OverseerDroneConfig` dataclass encapsulating drone-specific configurations derived from research. It includes physical attributes (mass, thrust, motor count), battery details (capacity, voltage), mission parameters (scan frequency, detection range), and bird deterrent settings (frequency ranges, pulse intervals, power). The class dynamically initializes a `SensorConfig` if not provided via `__post_init__`, ensuring compliance with research defaults.

## Key Functions

### ``__post_init__``

Initializes `SensorConfig` if not provided.

### ``from_research_specs``

Factory method returning a default `OverseerDroneConfig` based on research specs.

### ``get_battery_config``

Returns a dictionary of battery-related attributes.

### ``get_drone_specs``

Returns a dictionary of drone physical specifications.

### ``get_bird_deterrent_config``

Returns a dictionary of bird deterrent parameters.

## Usage

```python
from overseer_drone_config import OverseerDroneConfig

# Create default config (uses research defaults)
config = OverseerDroneConfig()

# Access specific configs
battery_config = config.get_battery_config()
drone_specs = config.get_drone_specs()
deterrent_config = config.get_bird_deterrent_config()
```

## Dependencies

> ``.sensor_config` (local module)`
> ``dataclasses` (Python standard library)`
> ``typing` (Python standard library)`

## Related

- [[research_specs_overseer_drone]]
- [[sensor_config_module]]

>[!INFO] Dynamic Sensor Initialization
> If `sensor_config` is not provided, it automatically initializes via `SensorConfig.from_research_specs()`.

>[!WARNING] Research-Dependent Values
> Values like `bird_deterrent_power` (10W) and `scan_frequency` (30s) are research-derived and may need validation in production.
