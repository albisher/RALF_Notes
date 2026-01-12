**Tags:** #logging, #initialization-order, #attribute-error, #safe-access, #debugging
**Created:** 2026-01-12
**Type:** code-fix

# simulation/hmrs_simulation_live.py

## Summary

```
Fixes logger initialization order issue in `set_base_gps()` to prevent AttributeError during backend startup.
```

## Details

> The fix addresses a race condition where `set_base_gps()` attempted to access `self.logger` before it was initialized in the `__init__` method. The original code relied on `if self.logger:` which fails if the attribute hasn’t been set yet. The solution replaces this with `hasattr(self, 'logger')` to safely check for attribute existence, ensuring graceful fallback to `print()` output when the logger isn’t available during initialization.

## Key Functions

### ``set_base_gps()``

Sets GPS coordinates with conditional logging fallback.

### ``LoggingBox``

Logger class initialized after `set_base_gps()` in `__init__`.

## Usage

The fix is applied during backend initialization by modifying `simulation/hmrs_simulation_live.py`. The method now safely handles cases where the logger isn’t ready, maintaining compatibility with existing code.

## Dependencies

> ``logging` module (implicitly used in `LoggingBox` class)`
> ``simulation` package components.`

## Related

- [[backend-logger-initialization-order]]
- [[simulation-package-documentation]]

>[!INFO] Safe Fallback
> The method now uses `hasattr()` to check for `self.logger` existence before accessing it, preventing crashes during initialization.

>[!WARNING] Debugging Note
> Ensure `LoggingBox` is initialized *after* `set_base_gps()` in `__init__` to avoid redundant checks. The fix is defensive but doesn’t alter initialization order.
