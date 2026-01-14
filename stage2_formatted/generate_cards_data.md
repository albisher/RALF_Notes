**Tags:** #data-processing, #documentation-parsing, #robot-data, #coordinate-extraction
**Created:** 2026-01-13
**Type:** documentation

# generate_cards_data

## Summary

```
Processes robot documentation files to extract structured card data for embedding in a JavaScript file.
```

## Details

> This script reads robot documentation files from a `KnownRobots` directory within a `Documentation` folder, extracts metadata such as names, descriptions, and optional images, and organizes them into a structured format. It handles coordinate extraction from text (e.g., latitude/longitude) and appends basic metadata like IDs and source references. The extracted data is stored in a list (`cards`) for later use in generating a JavaScript file (`cards-data.js`).
> 
> The script supports two main data sources: robot-specific files (e.g., `X1001.txt`) and story logs (though the latter is partially cut off). It processes filenames to derive display names (e.g., `X1001` → `X1`), extracts descriptions from sections like `Description`, and attempts to locate associated images. Coordinates are parsed from text patterns like `"31.1° N, 33.9° E"`.

## Key Functions

### `extract_location(text)`

Extracts latitude/longitude coordinates from text using regex, converting directional indicators (N/S/E/W) into signed values.

### `load_robots()`

Loads robot card data from `KnownRobots` subdirectory. For each file:

### `load_story_logs()`

(Incomplete) Loads story log files from `StoryLogs` directory (cutoff point in provided code).

## Usage

1. Place robot documentation files (e.g., `X1001.txt`) in `Documentation/KnownRobots/`.
2. Run the script to populate the `cards` list with structured data.
3. Use the `cards` list to generate `cards-data.js` by serializing it to JSON and embedding it in a JavaScript file.

## Dependencies

> ``os``
> ``json``
> ``re``
> ``pathlib` (Python standard libraries)
External: `Documentation/KnownRobots` and `Documentation/StoryLogs` directories with `.txt` files.`

## Related

- [[Structure]]
- [[cards-data]]
- [[KnownRobots]]
- [[StoryLogs]]

>[!INFO] Coordinate Parsing
> The `extract_location()` function uses regex to parse coordinates like `"31.1° N, 33.9° E"` into signed values (e.g., `31.1` for latitude, `-33.9` for longitude if direction is W/S). This assumes consistent formatting in documentation files.


>[!WARNING] Fallback Descriptions
> If no `Description` section is found, the script defaults to the first 5 non-empty lines of the file. Truncates descriptions to 200 characters to avoid excessive data.
