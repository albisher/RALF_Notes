**Tags:** #data-processing, #timeline-construction, #year-extraction, #card-analysis, #regex-patterns
**Created:** 2026-01-13
**Type:** code-module

# year_extraction_box

## Summary

```
Extracts unique years from card data for timeline visualization.
```

## Details

> This module processes an array of cards to identify and extract years from various fields (e.g., `time`, `timestamp`, `date`, or `content.year`). It validates input, handles edge cases (empty arrays, invalid operations), and returns structured metadata (sorted years, min/max years, and range). The core logic uses regex and date parsing to detect years in diverse formats (e.g., "Year 20485" or "20485-01-01").

## Key Functions

### ``_extractYearsFromCards(cards)``

Extracts unique years from an array of cards by iterating through each card and calling `_extractYearFromCard()`.

### ``_extractYearFromCard(card)``

Attempts to parse a single card for a year using multiple strategies (date strings, content fields, regex, and Date object parsing).

### ``_executeInternal(inputData)``

Orchestrates the extraction process, validates input, and formats the output as `{ years: [...], minYear: number, maxYear: number, yearRange: number }`.

## Usage

1. Instantiate `YearExtractionBox` and call its `extractYears` operation with an input object containing a `cards` array.
2. Example input:
   ```json
   { "operation": "extractYears", "cards": [...] }
   ```
3. Output includes:
   - Sorted array of unique years.
   - Minimum and maximum years.
   - Computed range (`maxYear - minYear`).

## Dependencies

> ``../core/box_interface.js` (Box framework for input/output handling)`
> ``BoxOutput``
> ``BoxErrorCode``
> ``BoxErrorCategory`.`

## Related

- [[Card Processing Pipeline]]
- [[Timeline Construction Module]]

>[!INFO] Year Extraction Logic
> The module prioritizes `content.year` over date strings (e.g., `card.content.year = 2023`) due to its directness. Regex (`/Year\s+(\d+)|(\d{3,5})/`) handles formats like "Year 20485" or "0624-01-01" (historical dates).

>[!WARNING] Edge Case Handling
> Returns `null` for invalid years (e.g., non-numeric strings) and skips empty date fields. Empty input arrays yield `{ years: [], ... }` with `null` min/max values.
