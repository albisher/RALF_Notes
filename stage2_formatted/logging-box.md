**Tags:** #frontend-logging, #centralized-logging, #unified-logging, #console-log-replacement, #iso-8601
**Created:** 2026-01-13
**Type:** code-notes

# logging-box

## Summary

```
Centralized frontend logging system standardizing log generation, filtering, and routing.
```

## Details

> `LoggingBox` is a singleton utility that replaces inconsistent `console.log()` calls with a unified logging interface. It maintains a history of logs, enforces configurable log levels, and routes logs to specified channels (UI, console, API). The system filters logs based on severity thresholds, adds metadata (source, timestamp, type), and supports structured logging with optional data fields.

## Key Functions

### ``init()``

Makes `LoggingBox` globally accessible and logs initialization.

### ``setLogLevel(level)``

Configures the minimum log level (DEBUG, INFO, WARNING, ERROR).

### ``setOutputChannels(channels)``

Defines where logs should be output (e.g., UI, console).

### ``log(level, message, options)``

Core method to generate standardized log entries. Returns `null` if the log level is below the configured threshold.

## Usage

1. Initialize via `LoggingBox.init()`.
2. Call `LoggingBox.log(level, message, { source, target, data })` to log messages.
3. Configure thresholds/channels with `setLogLevel()`/`setOutputChannels()`.

## Dependencies

> ``window` (for global scope)`
> ``Date` (for timestamp generation).`

## Related

- [[logging-system-overview]]
- [[frontend-monitoring-guidelines]]

>[!INFO] Global Scope
> `window.loggingBox` exposes the singleton instance globally for easy access.

>[!WARNING] Level Filtering
> Logs below the configured threshold (e.g., `setLogLevel('INFO')`) are silently discarded. Ensure critical messages are explicitly logged at higher levels.
