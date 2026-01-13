**Tags:** #logging, #centralized, #simulation, #monolithic, #enum, #callbacks, #routing, #ui, #console, #file, #api, #history
**Created:** 2026-01-13
**Type:** code-notes

# logging_box

## Summary

```
Standardized logging system for simulation components, replacing inconsistent logging methods.
```

## Details

> The `LoggingBox` class implements a centralized logging mechanism for the HMRS simulation system. It enforces a unified logging format, replacing legacy `print()` and `console.log()` calls. The system supports configurable log levels (DEBUG, INFO, WARNING, ERROR), multi-channel output (UI, console, file, API), and dynamic routing via callbacks. Logs are stored in a history buffer with configurable size limits.

## Key Functions

### ``LogLevel``

Enum defining log severity levels (DEBUG=1, INFO=2, WARNING=3, ERROR=4).

### ``__init__``

Initializes the logger with source identifier, log level, output channels, and history buffer.

### ``set_ui_callback``

Assigns a callback for UI log display.

### ``set_socketio_handler``

Configures Socket.IO for real-time log broadcasting.

### ``set_api_handler``

Sets up API endpoint for log retrieval.

### ``log``

Core method to generate and route standardized log entries with metadata (level, message, optional data, simulation time, log type).

## Usage

1. Instantiate `LoggingBox` with a source identifier and desired log level/output channels.
2. Configure routing via `set_ui_callback`, `set_socketio_handler`, or `set_api_handler`.
3. Call `log()` with a severity level and message to generate logs.
4. Logs are automatically filtered by `log_level` and routed to configured channels.

## Dependencies

> ``time``
> ``typing.Dict``
> ``typing.List``
> ``typing.Optional``
> ``typing.Callable``
> ``inspect``
> ``enum.Enum``

## Related

- [[logging_system_overview]]
- [[simulation_component_architecture]]

>[!INFO] Important Note
> Logs are only emitted if the provided `level` matches or exceeds the logger’s configured `log_level` threshold (e.g., logging `INFO` when `log_level=WARNING` will be ignored).
>

>[!WARNING] Caution
> Directly modifying `output_channels` or `max_history` after initialization may cause inconsistent log routing or history truncation. Prefer immutable configurations via callbacks.
