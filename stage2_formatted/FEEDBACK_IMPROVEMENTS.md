**Tags:** #UI/UX, #data-structure, #map-visualization, #card-system, #local-storage, #aspect-ratio, #feedback-implementation
**Created:** 2026-01-13
**Type:** documentation

# FEEDBACK_IMPROVEMENTS

## Summary

```
Tracks feedback and technical improvements for a card-based system, focusing on location mapping, image handling, and interactive page/book creation.
```

## Details

> This document details feedback received and implemented changes for a **card viewer system**, particularly addressing location display on 2D maps, image aspect ratio preservation, and modular history book creation. The system now supports dynamic card selection, page building, and history book exports while maintaining data integrity and visual consistency. Key improvements include enhanced map rendering, structured location data extraction, and UI refinements for responsive image handling.

## Key Functions

### ``extract_location()``

Parses and returns structured location data (coordinates, display string) for map integration.

### ``generate_cards_data.py``

Regenerates card data with coordinates, fixes HistoryBook parsing, and updates data structures.

### ``cardview.html``

Implements interactive UI for map rendering, card selection, page/book creation, and localStorage persistence.

### ``cards-data.js``

Stores 77 refined cards (13 Robot, 19 Event, 28 World, 11 History, 6 Convention) with coordinates and individual year/event content.

### `Map Rendering`

SVG-based 2D map with coordinate projection, markers, and fallbacks for missing data.

### `Page/Book Builder`

Checkbox selection + "Create Page"/"Create History Book" workflows with localStorage export.

## Usage

1. **For Developers**:
   - Update `generate_cards_data.py` to regenerate card data with coordinates.
   - Modify `cardview.html` for UI adjustments (e.g., map controls).
   - Ensure `processed_map.json` exists for map rendering.

2. **For Users**:
   - Select cards via checkboxes to create pages.
   - Build history books by selecting pages and exporting as JSON.
   - View locations on maps (character images overlay when applicable).

## Dependencies

> ``processed_map.json``
> ``localStorage``
> `SVG libraries (for map rendering)`
> `CSS (for aspect ratio and UI styling).`

## Related

- [[Card System Architecture]]
- [[Data Processing Pipeline]]
- [[Local Storage API Guide]]

>[!INFO] **Map Data Dependency**
> The system relies on `processed_map.json` for location-based cards. Missing data triggers a fallback placeholder.

>[!WARNING] **LocalStorage Limits**
> History books/pages persist in browser storage. Excessive data may cause memory issues or export failures.
