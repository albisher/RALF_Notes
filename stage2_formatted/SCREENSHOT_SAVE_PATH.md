**Tags:** #screenshot, #automation, #file-path, #playwright, #ui-testing, #directory-structure, #verification
**Created:** 2026-01-13
**Type:** documentation

# SCREENSHOT_SAVE_PATH

## Summary

```
Configures and verifies screenshot save paths and naming conventions for UI test automation using Playwright.
```

## Details

> This document outlines the structured directory for saving screenshots of map generation UI tests, ensuring reproducibility via timestamped folder organization (`YYYYMMDD/HHMM/`) while avoiding timestamps in filenames. The system uses a Python script (`take_map_verification_screenshots.py`) to automate browser screenshot capture and relocation to the correct path. Manual methods are also documented for browser-based tools. Screenshots follow a descriptive naming convention (e.g., `planet-map-generated-1.png`) to distinguish test cases, with verification steps to confirm directory integrity and file counts.

## Key Functions

### ``take_map_verification_screenshots.py``

Automates Playwright-driven screenshot capture and directory management.

### ``ls -la screenshots/map_generation_ui_tests/YYYYMMDD/HHMM/``

Verifies directory existence and writability.

### ``find ... -name "*.png" | wc -l``

Counts saved screenshots for validation.

## Usage

1. **Automated Method**: Run `python3 scripts/take_map_verification_screenshots.py` to capture screenshots directly to the configured path.
2. **Manual Method**: Use browser tools to save screenshots, then move them to the target directory (e.g., `mv /temp/screenshot.png /path/to/screenshots/YYYYMMDD/HHMM/`).
3. **Verification**: Execute verification commands (`ls`, `find`, `wc`) to confirm screenshots are saved correctly.

## Dependencies

> `Playwright`
> `Python 3`
> `Bash shell commands.`

## Related

- [[SCREENSHOT_NAME_CONVENTIONS]]
- [[MAP_GENERATION_TEST_FLOW]]
- [[AUTOMATION_SCRIPT_DOCS]]

>[!INFO] Important Note
> **Folder Structure Rule**: Timestamps are embedded in the folder path (`YYYYMMDD/HHMM/`) but **not** in filenames to avoid conflicts across runs. Always use descriptive names (e.g., `planet-map-generated-1.png`) to link screenshots to specific test cases.


>[!WARNING] Caution
> **Manual Overwrite Risk**: If manually moving files, ensure filenames match existing ones in the target directory to avoid accidental overwrites. Use `ls` to check for duplicates before moving.
