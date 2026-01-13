**Tags:** #time-restrictions, #drone-operations, #timezone-handling, #datetime-enforcement
**Created:** 2026-01-13
**Type:** code-notes

# time_restrictions

## Summary

```
Enforces time-of-day restrictions for drone operations by validating current time against configured operating hours.
```

## Details

> This module implements a `TimeRestrictionEnforcer` class that checks whether a drone operation is allowed based on predefined start/end times. It supports timezone-aware enforcement when `pytz` is available, falling back to UTC otherwise. The enforcer dynamically adjusts checks for both standard (e.g., 08:00–18:00) and overnight (e.g., 18:00–08:00) operating windows.

## Key Functions

### ``__init__()``

Initializes default restrictions (enabled=False, UTC timezone, 08:00–18:00 window).

### ``set_restrictions(restrictions`

Dict)`**: Updates configurable parameters via a dictionary.

### ``is_operation_allowed(current_time`

Optional[datetime] = None) -> tuple[bool, str]`**:

## Usage

```python
enforcer = TimeRestrictionEnforcer()
enforcer.set_restrictions({'enabled': True, 'startTime': '09:00', 'endTime': '22:00', 'timezone': 'America/New_York'})
is_allowed, reason = enforcer.is_operation_allowed()
```

## Dependencies

> ``datetime``
> ``pytz` (optional`
> `for timezone support)`
> ``typing` (for type hints).`

## Related

- [[timezone_aware_drone_systems]]
- [[drone_operational_rules]]

>[!INFO] Timezone Handling
> If `pytz` is unavailable, timezone conversions are disabled, and all checks default to UTC. This may cause incorrect results for non-UTC regions.

>[!WARNING] Edge Case Handling
> For start/end times like `23:00`–`07:00`, the code assumes `start_time <= end_time` is false (e.g., `23:00` > `07:00`), triggering an overnight check. Ensure logic aligns with intended behavior.
