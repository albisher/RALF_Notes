**Tags:** #screenshot-verification, #map-generation, #deterministic-algorithm, #world-type-validation
**Created:** 2026-01-13
**Type:** code-script

# verify_map_generation_screenshots

## Summary

```
Script automates screenshot verification for map generation tests, ensuring consistency between world types and hash-based deterministic outputs.
```

## Details

> This Bash script organizes and structures screenshots for verifying map generation logic. It dynamically creates a timestamped directory (`YYYYMMDD/HHMM`) under a base path (`screenshots/map_generation_ui_tests`) to store screenshots. The script guides users to capture screenshots for:
> - **World-type validation** (Planet, Galaxy, Cloud World) in initial states and generated maps.
> - **Hash-based reproducibility** (e.g., same hash input → identical map output).
> 
> The script suggests naming conventions (e.g., `planet-map-generated-1.png` vs. `planet-map-generated-2.png` for comparison). Users must manually trigger browser automation to capture screenshots, which are then saved for later verification.

## Key Functions

### ``date +%Y%m%d``

Generates a date-based directory identifier (e.g., `20240101`).

### ``date +%H%M``

Generates a time-based subdirectory (e.g., `1430`).

### ``mkdir -p``

Creates nested directories without errors if they exist.

### `User prompts`

Guides screenshot naming conventions for deterministic validation.

## Usage

1. Run the script in a terminal to generate a timestamped directory.
2. Manually capture screenshots using browser automation tools, following naming conventions.
3. Verify generated maps match expected outputs (e.g., identical for same hash inputs).

## Dependencies

> `- Bash shell (for directory creation and date formatting).
- Browser automation tools (e.g.`
> `Puppeteer`
> `Selenium) for capturing screenshots.`

## Related

- [[none]]

>[!INFO] Important Note
> **Directory Structure**: Screenshots must follow `YYYYMMDD/HHMM/` to align with script logic. Delete old directories if space is limited.
>

>[!WARNING] Caution
> **Manual Steps Required**: The script does not automate screenshot capture—users must use browser automation tools to ensure consistency. Inconsistent naming may invalidate verification.
