**Tags:** #archiving, #ui-components, #mockup, #data-conversion, #unused-components
**Created:** 2026-01-13
**Type:** documentation

# ARCHIVING_SUMMARY

## Summary

```
Archiving summary for unused UI components and next steps for converting mock cards to real cards.
```

## Details

> This document outlines the archiving of unused UI components from `ui-beta` based on iteration-10 mockup, including moving unused component files to an archived directory and updating `index.html` to remove redundant script tags. It also details the current status of mock cards and the necessary steps to convert them into real cards, requiring a world to be created first. The archived components are stored in `ui-beta/archived/components/` and can be restored later if needed.

## Key Functions

### ``convert_mock_cards_to_real.py``

Converts mock cards to real cards after a world is created.

### ``check_and_convert_cards.py``

Verifies and converts cards post-conversion.

### ``ui-beta/archived/components/``

Directory for storing unused UI components for future reference.

## Usage

1. **Archiving**:
   - Move unused components from `ui-beta/components/` to `ui-beta/archived/components/`.
   - Update `index.html` to remove unused script tags and add comments explaining archiving.

2. **Card Conversion**:
   - Create a world via UI (accessible at `http://localhost:8888/ui-beta/`).
   - Run `convert_mock_cards_to_real.py` with the world ID or default world.
   - Verify conversion with `check_and_convert_cards.py`.

## Dependencies

> `- `ui-beta/data/cards-data.js` (mock cards data)
- `scripts/convert_mock_cards_to_real.py` (conversion script)
- `scripts/check_and_convert_cards.py` (verification script)
- `js/api-client.js` (API client for UI)`

## Related

- [[ARCHIVING_NOTES]]
- [[UI_COMPONENT_DOCS]]

>[!INFO] Important Note
> The archived components (`ui-beta/archived/components/`) are stored for future reference but are not actively used. Ensure any restored components are tested before reintegrating into the UI.


>[!WARNING] Caution
> Converting mock cards requires a world to exist. If no world is created, the conversion script will fail. Always verify the world ID before running the conversion script.
