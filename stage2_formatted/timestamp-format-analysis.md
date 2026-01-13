**Tags:** #timestamp, #precision, #datetime, #unix-epoch, #microseconds, #simulation-time, #log-analysis, #iso-format, #data-formats, #precision-comparison
**Created:** 2026-01-13
**Type:** documentation

# timestamp-format-analysis

## Summary

```
Analyzes existing timestamp formats in a system, comparing real-time and simulation-based precision for logs and exports.
```

## Details

> This document evaluates three timestamp formats: `time.time()` (Unix float), `datetime.now().isoformat()` (ISO string), and `sim_time` (high-precision simulation seconds). It details their precision, use cases (logs, exports), and conversion methods. The analysis highlights microsecond precision for real timestamps and high precision for simulation events, with recommendations for display (e.g., `HH:MM:SS.microseconds`) and storage (e.g., Unix timestamp or ISO string).

## Key Functions

### ``time.time()``

Returns Unix timestamp (float) with microsecond precision.

### ``datetime.fromtimestamp()``

Converts Unix timestamp to `datetime` object.

### ``strftime("%H`

%M:%S")`**: Formats timestamp as seconds-only (e.g., `10:00:34`).

### ``strftime("%H`

%M:%S.%f")`**: Formats timestamp with microseconds (e.g., `10:00:34.567890`).

### ``datetime.now().isoformat()``

Generates ISO 8601 string (e.g., `2023-12-19T10:00:34.567890`).

### ``sim_time``

High-precision simulation timestamp (e.g., `83.51666666667288`).

## Usage

1. **For logs/messages**: Use `time.time()` (float) for machine-readable precision.
2. **For exports**: Use `datetime.now().isoformat()` (ISO string) for compatibility.
3. **For simulation events**: Preserve `sim_time` (high-precision float).
4. **For display**: Convert to readable formats (e.g., `strftime` or `isoformat`).

## Dependencies

> `Python standard library (`time``
> ``datetime`)`
> `JSON for log examples.`

## Related

- [[Timestamp Conversion Guide]]
- [[Precision Standards]]
- [[Simulation Data Handling]]

>[!INFO] Important Note
> Simulation time (`sim_time`) is **not real time**—it tracks internal simulation progress, not calendar time. Misuse could lead to incorrect event ordering in logs.

>[!WARNING] Caution
> Storing raw `time.time()` as a string (e.g., `"1703001234.567890"`) risks precision loss during parsing. Always convert to float or ISO format for storage.
