**Tags:** #world-generation, #biome-simulation, #context-aware, #procedural-worlds, #space-science
**Created:** 2026-01-13
**Type:** documentation

# world_type_biome_calculator

## Summary

```
Dynamic biome calculator for various world types, adapting climate and environmental factors based on context.
```

## Details

> This class dynamically generates biome matrices and environmental conditions (temperature, precipitation) for different world types, including fantasy planets, galaxies, space stations, ships, asteroids, and moons. It categorizes the world type via input parameters and applies context-specific calculations for temperature and precipitation, using height-based metrics to simulate elevation effects. The system defaults to fantasy planet logic if no matching category is found.

## Key Functions

### ``WorldTypeBiomeCalculator``

Main class initializing biome systems based on world type and description.

### ``_categorize_world``

Determines the world category (e.g., "fantasy_planet", "galaxy") from input strings.

### ``calculate_temperature``

Computes temperature variations based on height and world type (e.g., nebula cores in galaxies, crater peaks on moons).

### ``calculate_precipitation``

Estimates moisture levels (0-1 scale) for non-galactic worlds, capped at 1.0 for gas-rich regions.

### ``_create_fantasy_biome_matrix``

Generates fantasy-themed biome data structures (e.g., forests, deserts).

### ``_create_galaxy_region_matrix``

Creates matrices for nebula clusters, star systems, or cosmic voids.

### ``_create_station_section_matrix``

Defines habitat zones for space stations (e.g., living quarters, research labs).

## Usage

```python
calculator = WorldTypeBiomeCalculator(world_type="Planet", world_description="A lush fantasy world")
temperature = calculator.calculate_temperature(cell_height=0.3)  # Returns adjusted temperature
precipitation = calculator.calculate_precipitation(cell_height=0.7)  # Returns adjusted moisture
```

## Dependencies

> `typing`
> `no external libraries required`

## Related

- [[World Generation Framework]]
- [[Biome Data Specifications]]

>[!INFO] Context Sensitivity
> Temperature/precipitation calculations adapt to world type (e.g., a space station’s decks are cooler than a fantasy planet’s sea level).

>[!WARNING] Hardcoded Defaults
> If `world_type` doesn’t match any category, it defaults to fantasy planet logic—consider adding validation for edge cases.
