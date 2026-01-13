**Tags:** #drone-configuration, #sensor-config, #research-specs, #octocopter, #battery-management
**Created:** 2026-01-13
**Type:** code-notes

# scout_drone_config

## Summary

```
Defines research-based specifications for the HMRS Scout drone, including physical, battery, and mission parameters.
```

## Details

> This file defines a `ScoutDroneConfig` dataclass encapsulating drone-specific configurations derived from research. It includes physical attributes (mass, thrust, motor count), battery details (capacity, voltage), mission parameters (lookahead time), and sensor configurations. The `__post_init__` method automatically initializes a `SensorConfig` if none is provided, while `from_research_specs` returns a default configuration based on research benchmarks.

## Key Functions

### ``__post_init__``

Initializes `sensor_config` to `SensorConfig.from_research_specs()` if not provided.

### ``from_research_specs``

Factory method returning a default `ScoutDroneConfig` instance with research-derived defaults.

### ``get_battery_config``

Returns a dictionary of battery-related attributes (capacity, voltage, charge).

### ``get_drone_specs``

Returns a dictionary of physical drone specifications (mass, thrust, motor count, battery life).

## Usage

```python
from scout_drone_config import ScoutDroneConfig

# Create a default config (auto-populates sensor_config)
config = ScoutDroneConfig()

# Access specific configs
print(config.get_battery_config())  # Battery details
print(config.get_drone_specs())     # Physical specs
```

## Dependencies

> ``.sensor_config` (local module)`
> ``dataclasses` (Python standard library)`
> ``typing` (Python standard library)`

## Related

- [[sensor_config]]
- [[research_notes_on_drones]]

>[!INFO] Default Sensor Initialization
> If `sensor_config` is not explicitly set, it defaults to `SensorConfig.from_research_specs()`, ensuring consistent sensor integration.

>[!WARNING] Research-Dependent Values
> Values like `mass` (3-5 kg) and `battery_life_minutes` (30-45 min) are research-derived and may vary in real-world applications. Validate against actual hardware specs.
