**Tags:** #automation, #file-management, #bash-scripting, #screenshot-organization
**Created:** 2026-01-13
**Type:** code-notes

# move_screenshots_to_path

## Summary

```
Automates moving recent PNG screenshots to a structured timestamped directory.
```

## Details

> This script locates recently modified PNG files (within the last 5 minutes) across specified directories (`/tmp`, `~/Downloads`, current directory, and `screenshots`), then moves them into a dynamically generated path (`YYYYMMDD/HHMM/`) under `screenshots/map_generation_ui_tests/`. It skips files already in the target directory and logs results.

## Key Functions

### ``SCREENSHOT_DIR``

Constructs the target path using `date` for timestamp formatting.

### ``SOURCE_DIRS``

Defines directories to search for screenshots.

### ``find` loop`

Recursively scans directories for PNG files modified in the last 5 minutes.

### ``mv` command`

Moves valid files to the target directory with error suppression.

## Usage

1. Run the script directly (`./move_screenshots_to_path`).
2. If no files are found, manually move screenshots to the target directory using `mv`.
3. Verify contents with `ls -lh "$SCREENSHOT_DIR"/*.png`.

## Dependencies

> ``bash``
> ``date``
> ``find` (standard Unix utilities)`

## Related

- [[none]]

>[!INFO] Important Note
> The script skips files already in the target directory (`"$SCREENSHOT_DIR"/*`) to avoid overwrites.

>[!WARNING] Caution
> Ensure `screenshots/map_generation_ui_tests/` exists before running—missing parent directories will fail silently.
