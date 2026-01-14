**Tags:** #screenshot-processing, #automated-analysis, #map-generation, #playwright-integration, #file-system-operations
**Created:** 2026-01-13
**Type:** documentation-research

# capture_and_analyze_screenshots

## Summary

```
Automates screenshot capture, organization, and analysis for map generation UI tests, ensuring deterministic map rendering verification.
```

## Details

> This script handles the lifecycle of map generation screenshots by:
> 1. Creating timestamped directories for organized storage
> 2. Detecting and copying existing screenshots from a verification folder
> 3. Classifying screenshots by world type (galaxy, clouds, planet) via filename analysis
> 4. Generating a structured markdown report with metadata and verification checklists
> 
> The workflow prioritizes existing screenshots while providing fallback mechanisms for manual capture.

## Key Functions

### ``analyze_existing_screenshots()``

Scans for recent map-generated PNGs in verification directory

### ``copy_and_analyze_screenshots()``

Classifies files by world type, copies them to timestamped location

### ``generate_analysis_report()``

Creates markdown report with metadata organization and verification checklist

### ``SCREENSHOT_DIR``

Dynamic directory path combining date/time stamps for organized storage

## Usage

1. Run script to automatically process existing screenshots
2. Script creates timestamped directory structure (e.g., `screenshots/map_generation_ui_tests/YYYYMMDD/HHMM`)
3. Existing screenshots are copied with standardized naming conventions
4. Generate report at `SCREENSHOT_DIR/SCREENSHOT_ANALYSIS_REPORT.md`

## Dependencies

> `subprocess`
> `json`
> `shutil`
> `playwright.sync_api (via playwright)`
> `pathlib`
> `datetime`

## Related

- [[Map Generation Verification Documentation]]
- [[Playwright Integration Guide]]

>[!INFO] Playwright Dependency
> If Playwright is unavailable, script gracefully falls back to manual screenshot analysis. Users must install dependencies with:
> `pip install playwright && playwright install chromium`
>

>[!WARNING] File Naming Assumptions
> World type classification relies on filename patterns ("galaxy", "clouds", etc.). Custom naming conventions may require adjustments to classification logic.
