**Tags:** #error-handling, #centralized-logic, #box-component, #asynchronous-processing
**Created:** 2026-01-13
**Type:** code-notes

# error_handling_box

## Summary

```
Centralized error handling module for processing and categorizing errors with retry logic and user-friendly messaging.
```

## Details

> This `ErrorHandlingBox` class extends a base `Box` component to provide structured error handling. It processes incoming error data (e.g., raw errors, error codes, or user messages), extracts detailed error metadata (e.g., message, stack trace, timestamp), and generates standardized outputs. The box uses predefined logic to categorize errors (e.g., network, authentication) and determines whether to retry operations based on error type. It integrates with a logger for centralized error tracking and supports parallel execution with configurable timeouts.

## Key Functions

### ``_executeInternal(inputData)``

Core async method that processes input error data, logs errors, and returns structured output (error info, user-friendly message, retry flag, and delay).

### ``_getFriendlyMessage(error, errorCode, errorCategory)``

Generates human-readable messages based on error details, error codes, or predefined patterns (e.g., "Network error").

### ``_shouldRetry(error, errorCode)``

Decides if an error warrants retry by checking error codes or error message keywords (e.g., "network", "timeout").

### ``_getRetryDelay(error, errorCode)``

Sets retry delay (e.g., 2s for timeouts, 1s default).

## Usage

1. Instantiate `ErrorHandlingBox` and pass it to a workflow.
2. Feed it input data containing `operation`, `error`, `errorCode`, `errorCategory`, etc.
3. Retrieve processed output with `errorInfo`, `userMessage`, `shouldRetry`, and `retryDelay`.
4. Use the output to handle errors (e.g., retry logic, user notifications).

## Dependencies

> ``../core/box_interface.js` (Box class and related interfaces)`
> ``../../utils/logger.js` (logger utility).`

## Related

- [[Error Handling Workflow]]
- [[Box Component Architecture]]

>[!INFO] Standardized Logging
> Errors are logged with a timestamp and structured metadata (e.g., `errorInfo.message`, `errorInfo.stack`) for debugging.

>[!WARNING] Retry Logic Overhead
> Retries are only attempted for specific error codes (`NETWORK_ERROR`, `TIMEOUT`) or keywords. Avoid over-retrying transient errors to prevent cascading failures.
