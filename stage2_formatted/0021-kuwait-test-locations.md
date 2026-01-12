**Tags:** #kuwait, #test-locations, #osm, #geospatial, #simulation, #cesium, #python, #openstreetmap
**Created:** 2026-01-12
**Type:** test-reference

# kuwait-test-locations

## Summary

```
Document outlining Kuwait test locations for validating OSM building data and Cesium integration.
```

## Details

> This document provides test coordinates for two locations in Kuwait—**Home** (residential area) and **PAAET** (Shuwaikh campus)—to verify OSM building coverage, street availability, and 3D rendering accuracy. It includes Python and CesiumJS test scripts to fetch and visualize buildings within specified radii, alongside verification links to OpenStreetMap and Overpass Turbo for manual validation.

## Key Functions

### `OSMBuildingsIntegration.get_buildings_in_radius()`

Retrieves buildings within a radius of a given latitude/longitude.

### `Cesium.createOsmBuildingsAsync()`

Loads OSM building data for visualization in Cesium.

### `testKuwaitLocation()`

Script to load OSM buildings and fly to specified coordinates in Cesium.

## Usage

1. **Python Test**: Run the script to count buildings within 500m (Home) or 1km (PAAET) radius.
2. **Cesium Test**: Load the script in a Cesium viewer to visualize buildings and verify 3D rendering.
3. **Manual Verification**: Use OpenStreetMap links or Overpass Turbo to cross-check building density and coverage.

## Dependencies

> `- Python: `simulation.swarm.integrations.osm_buildings`
- JavaScript: Cesium library (CesiumJS)
- OpenStreetMap (OSM) data via Overpass API`

## Related

- [[0021-real-world-street-maps-from-gps]]

>[!INFO] Important Note
>Coordinates are in **Decimal Degrees (latitude, longitude)**. Ensure Cesium/Python scripts use the exact values to avoid mismatches.

>[!WARNING] Caution
>Overpass Turbo queries may require adjustments if coordinates are slightly off (e.g., rounding errors). Test with the provided links for accuracy.
