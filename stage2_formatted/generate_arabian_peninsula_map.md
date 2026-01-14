**Tags:** #map-generation, #geospatial-coordinates, #arabian-peninsula, #quran-world, #fantasy-map
**Created:** 2026-01-13
**Type:** documentation

# generate_arabian_peninsula_map

## Summary

```
Script provides guidance and validation for generating an Earth-focused map centered on the Arabian Peninsula for a fantasy world.
```

## Details

> This script documents the requirements for creating a map centered on the Arabian Peninsula using Azgaar’s Fantasy Map Generator format. It defines geographic coordinates (latitude and longitude) for the peninsula’s boundaries and key locations (e.g., Mecca, Medina) to ensure accurate placement of Quraan World cards. The script checks if an existing processed map (`processed_map.json`) already covers the region and validates whether coordinates remain valid even if the map boundaries shift. It guides users on generating a new map or reusing an existing one while ensuring card coordinates remain functional.

## Key Functions

### `document_map_requirements()`

Prints formatted instructions for setting map bounds and key locations (e.g., Mecca, Cave of Hira) using Azgaar’s generator.

### `check_current_map()`

Loads `processed_map.json` and verifies if the Arabian Peninsula is covered by checking if Mecca’s coordinates fall within the map’s latitude/longitude bounds.

### `main()`

Orchestrates execution by calling both functions and summarizing results.

## Usage

1. Run the script to display requirements and validate the current map.
2. If no valid `processed_map.json` exists, manually generate a map using Azgaar’s tool with the specified bounds:
   - Latitude: 12°N to 32°N
   - Longitude: 35°E to 60°E
3. Export as `map.json` and process with `python3 app/process_map_data.py map.json processed_map.json`.

## Dependencies

> ``json``
> ``os``
> ``sys` (Python standard libraries)`

## Related

- [[Azgaar’s Fantasy Map Generator Documentation]]
- [[Quraan World Map Coordinates]]

>[!INFO] Important Note
> The script assumes `processed_map.json` is located in `app/processed_map.json`. If missing, the system defaults to generating a new map with the provided bounds.

>[!WARNING] Caution
> If the existing map’s bounds are misaligned, card coordinates may still function outside the map’s visible area, but visual accuracy could be compromised. Always verify coverage with `check_current_map()`.
