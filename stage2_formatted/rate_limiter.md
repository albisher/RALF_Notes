**Tags:** #rate-limiting, #api-control, #time-window, #concurrency-management
**Created:** 2026-01-13
**Type:** code-notes

# rate_limiter

## Summary

```
A lightweight rate limiter for enforcing API call constraints via timestamps.
```

## Details

> This `RateLimiterBox` class implements a sliding-window rate limiter by tracking timestamps of recent API calls. It enforces a maximum call limit (`max_calls`) within a configurable time window (`time_window`). When a call is made, the system checks if it exceeds the limit by removing outdated timestamps (older than `time_window` seconds) before evaluating eligibility. The `execute()` method supports two actions: `"check"` (validates call permission) and `"get_remaining"` (queries remaining allowed calls).

## Key Functions

### ``__init__(max_calls, time_window)``

Configures the rate limiter with call limits and time constraints.

### ``execute(input_data)``

Processes API call requests, enforces limits, and returns permission status/remaining calls.

### ``self.calls``

Internal list storing timestamps of recent calls (auto-cleans old entries).

## Usage

1. Initialize with `RateLimiterBox(max_calls=10, time_window=60)`.
2. Call `execute()` with:
   - `"check"` action + `record_call=True` to enforce limits.
   - `"get_remaining"` action to query remaining allowed calls.
3. Example input:
   ```python
   input_data = BoxInput({"action": "check", "record_call": True})
   ```

## Dependencies

> ``time``
> ``logging``
> ``..core.box_interface` (parent Box class)`
> ``BoxInput``
> ``BoxOutput`.`

## Related

- [[`Box` class in `core]]
- [[BoxOutput` documentation]]

>[!INFO] Sliding-Window Logic
> The system dynamically adjusts call eligibility by truncating timestamps older than `time_window` seconds, ensuring fairness across bursts.

>[!WARNING] Edge Case Handling
> If `max_calls` is exceeded, `record_call=True` has no effect—call timestamps are ignored until the window resets.
