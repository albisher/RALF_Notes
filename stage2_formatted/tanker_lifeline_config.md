**Tags:** #drone-configuration, #aerial-research, #tethered-systems, #sensor-integration
**Created:** 2026-01-13
**Type:** code-notes

# tanker_lifeline_config

## Summary

```
Research-based drone configuration for a tethered lifeline system for HMRS.
```

## Details

> This file defines a `TankerLifelineConfig` dataclass containing specifications for a research-based HMRS (Human-Machine Responsive System) drone equipped with a tether system. It includes physical drone attributes (mass, thrust, motor count), tether parameters (length, tension thresholds), battery details (capacity, voltage), and sensor configurations. The class ensures sensor initialization via `__post_init__` if not provided, and provides utility methods to retrieve configurations in dictionary format.

## Key Functions

### ``__post_init__``

Initializes `SensorConfig` if not provided via `from_research_specs()`.

### ``from_research_specs``

Factory method returning a default `TankerLifelineConfig` instance.

### ``get_battery_config``

Returns a dictionary of battery specifications (capacity, voltage, charge).

### ``get_drone_specs``

Returns a dictionary of drone physical attributes (mass, thrust, motor count, battery life).

### ``get_tether_config``

Returns a dictionary of tether parameters (length, tension thresholds, snag detection).

## Usage

```python
from tanker_lifeline_config import TankerLifelineConfig

# Create default config (automatically initializes sensors)
config = TankerLifelineConfig()

# Retrieve specific configs
battery_specs = config.get_battery_config()
drone_specs = config.get_drone_specs()
tether_specs = config.get_tether_config()
```

## Dependencies

> ``.sensor_config` (local module)`
> `typing (Python standard library)`
> `dataclasses (Python standard library)`

## Related

- [[research_specs_docs]]
- [[sensor_config_implementation]]

>[!INFO] Sensor Auto-Initialization
> Sensors are automatically initialized via `__post_init__` if not explicitly set, ensuring research defaults are applied.

>[!WARNING] Tether Safety Limits
> Exceeding `max_tension` (20N) or falling below `min_tension` (10N) may trigger snag detection or fail-safes. Monitor `target_tension` (15N) for optimal performance.
