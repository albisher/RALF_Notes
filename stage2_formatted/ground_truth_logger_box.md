**Tags:** #logging, #data_structures, #pybullet, #ground_truth, #simulation
**Created:** 2026-01-13
**Type:** code-notes

# ground_truth_logger_box

## Summary

```
Handles logging and exporting ground truth object data (shape, position, size) for simulation scenarios.
```

## Details

> This module implements a `GroundTruthLoggerBox` class designed to log objects that are visible in visualization but hidden from command & control (C&C) systems. It maintains a list of logged objects, processes input data (shape, position, size, and optional body_id), and supports exporting logs to JSON format. The logger tracks timestamps and forwards logs to configured output channels (e.g., frontend LoggingBox).

## Key Functions

### ``__init__(self, output_channels`

Optional[List] = None)`**: Initializes the logger with an optional list of output channels and records the start time.

### ``log_object(self, shape`

str, position: List[float], size: Any, body_id: Optional[int] = None)`**: Creates a log entry dictionary for an object and appends it to the internal list. Optionally forwards the log to configured channels.

### ``get_log_entries(self) -> List[Dict[str, Any]]``

Returns a copy of all logged entries for retrieval.

### ``export_to_file(self, filepath`

str) -> str`**: Saves the logged data (including start time and object metadata) to a JSON file in the specified path, ensuring directory creation if needed.

## Usage

1. Instantiate the `GroundTruthLoggerBox` with optional output channels (e.g., `logger = GroundTruthLoggerBox(["logging_box"])`).
2. Log objects using `logger.log_object(shape, position, size, body_id)`.
3. Retrieve logs via `logger.get_log_entries()` or export to JSON with `logger.export_to_file("path/to/output.json")`.

## Dependencies

> `json`
> `os`
> `datetime`

## Related

- [[none]]

>[!INFO] Important Note
> The `size` parameter is normalized into a 3D list (e.g., `[size, size, size]`) if not already a list/tuple to ensure consistency across shapes.

>[!WARNING] Caution
> Directly modifying `self.objects` externally may corrupt the logger’s internal state. Always use `get_log_entries()` to retrieve copies of entries.
