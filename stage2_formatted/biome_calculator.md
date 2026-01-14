**Tags:** #biome-classification, #environmental-simulation, #climate-modelling, #terrain-analysis
**Created:** 2026-01-13
**Type:** code-library

# biome_calculator

## Summary

```
Simulates biome classification using height, temperature, and precipitation inputs.
```

## Details

> This `BiomeCalculator` class implements a simplified biome classification system by mapping environmental variables (height, temperature, and precipitation) to predefined biome types. It uses a matrix-based lookup for land biomes and handles water-based biomes separately. The system calculates temperature and precipitation adjustments based on elevation and assigns biome labels through predefined thresholds and indices.

## Key Functions

### ``calculate_temperature``

Computes temperature reduction with elevation using a lapse rate formula.

### ``calculate_precipitation``

Estimates precipitation increase with elevation, capped at 1.0.

### ``assign_biome``

Determines biome type based on temperature, precipitation, and height thresholds.

### ``_temperature_to_index``

Maps temperature ranges to numerical indices for matrix lookup.

### ``_precipitation_to_index``

Converts precipitation values (0-1) to a 0-9 scale for matrix compatibility.

### ``_create_biome_matrix``

Defines biome assignments for each precipitation/temperature combination.

### ``_create_biome_list``

Generates biome definitions with associated colors for visualization.

### ``get_biome_list``

Returns a list of biome definitions (names + colors).

## Usage

```python
calculator = BiomeCalculator()
temperature = calculator.calculate_temperature(height=0.5, coastal_temp=15.0)
precipitation = calculator.calculate_precipitation(height=0.5)
biome = calculator.assign_biome(temperature, precipitation, height)
print(biome)  # Outputs biome name (e.g., 'forest')
```

## Dependencies

> `typing`
> `None (no external libraries required beyond Python’s standard library).`

## Related

- [[None]]

>[!INFO] **Elevation Handling**
> Water biomes (height < `sea_level`) are assigned directly; land biomes use elevation-adjusted calculations. The `sea_level` constant (0.2) defines the boundary between water and land.


>[!WARNING] **Simplification Note**
> Precipitation and temperature calculations are linear approximations. Real-world biomes require more complex climate data (e.g., seasonal variations).
