**Tags:** #GeoJSON, #BiomeDataExtraction, #CoordinateProcessing, #TextOutput
**Created:** 2026-01-13
**Type:** code-notes

# extract_biomes

## Summary

```
Extracts biome IDs and their coordinates from a GeoJSON file into a structured text output.
```

## Details

> This script reads a GeoJSON file containing biome data (likely from a game or map generator) and processes its `FeatureCollection` to extract biome identifiers and their associated coordinates. It validates the input file, checks for proper GeoJSON structure, and writes formatted output to a text file. The script handles errors for missing files, invalid JSON, or malformed GeoJSON data.

## Key Functions

### ``json.load()``

Parses the GeoJSON file into a Python dictionary.

### `Feature validation`

Checks if the input is a `FeatureCollection` with valid `features` and `properties`/`geometry` structures.

### `Coordinate extraction`

Retrieves biome IDs and coordinates from each feature’s properties and geometry.

### `Output formatting`

Writes structured text to a file with biome IDs and JSON-serialized coordinates.

## Usage

1. Set `geojson_filepath` to the path of the input GeoJSON file.
2. Define `output_filepath` for the text output file.
3. Run the script. It will:
   - Extract biome IDs and coordinates.
   - Write results to `output_filepath` in a readable format.
   - Print success/error messages.

## Dependencies

> ``json``
> ``os` (standard library modules)`

## Related

- [[None]]

>[!INFO] Important Note
> The script assumes the GeoJSON file is a `FeatureCollection` with `features` containing `properties` (e.g., `biome`) and `geometry` (e.g., coordinates). If the structure differs, extraction may fail.
>

>[!WARNING] Caution
> Hardcoded paths (`/Users/amac/Downloads/...`) may break if the script is moved. Use environment variables or relative paths for portability.
