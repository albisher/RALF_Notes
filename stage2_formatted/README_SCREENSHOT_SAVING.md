**Tags:** #screenshot-saving, #automation, #path-management, #browser-tools, #verification
**Created:** 2026-01-13
**Type:** documentation

# README_SCREENSHOT_SAVING

## Summary

```
Document outlines methods to ensure screenshots are saved to a standardized directory structure for UI testing verification.
```

## Details

> This document describes the process for saving screenshots to a predefined directory (`screenshots/map_generation_ui_tests/YYYYMMDD/HHMM/`) to maintain consistency across tests. The current session directory is set to `20251209/0801/`, but the workflow must enforce this path regardless of browser tool defaults. The solution includes automated (Python script), manual (post-processing), and tool-specific approaches to guarantee correct placement. Screenshots must follow specific naming conventions for verification of deterministic yet varied map outputs across different world types (Planet, Galaxy, Cloud).

## Key Functions

### ``scripts/take_map_verification_screenshots.py``

Automates browser navigation, screenshot capture, and saves files to the correct path.

### ``playwright install chromium``

Installs Playwright browser automation tools.

### ``ls -lh screenshots/map_generation_ui_tests/YYYYMMDD/HHMM/``

Lists files in the target directory for verification.

### ``find ... | wc -l``

Counts PNG files in the directory to confirm completeness.

## Usage

1. **Automated Method**: Run `python3 scripts/take_map_verification_screenshots.py` after installing dependencies.
2. **Manual Method**: Take screenshots, locate them, and move them to the correct path using `mv`.
3. **Tool-Specific**: Configure browser tools to include filenames with the target directory structure.

## Dependencies

> ``pip``
> ``playwright``
> ``python3``
> `browser automation libraries (Chromium).`

## Related

- [[README_Browser_Automation_Setup]]
- [[Test_Plan_Map_Generation_UI]]
- [[Screenshots_Standardization_Policy]]

>[!INFO] Important Note
> The directory structure (`YYYYMMDD/HHMM/`) must be created manually or via script before saving screenshots. Tools like `date +%Y%m%d` ensure consistency but require execution in the correct environment.

>[!WARNING] Caution
> Manual file moves risk errors if paths are misconfigured. Always verify filenames match expected patterns (e.g., `planet-initial-state.png`). Incomplete screenshots may invalidate test results.
