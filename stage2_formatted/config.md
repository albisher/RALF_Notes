**Tags:** #configuration-management, #api-integration, #environment-variables, #json-config, #external-services
**Created:** 2026-01-13
**Type:** code-notes

# config

## Summary

```
Manages external API integrations by loading and validating config from files or environment variables.
```

## Details

> This module (`IntegrationConfig`) centralizes configuration for external API services (e.g., OpenWeatherMap, Google Maps) and drone SDKs (DJI/Parrot). It prioritizes environment variables over a JSON file, ensuring dynamic updates without code changes. The class handles fallback logic for missing keys, validates SDK enablement flags, and provides utility methods to check API key availability.

## Key Functions

### ``__init__(self, config_file`

Optional[str] = None)`**: Initializes config path (defaults to `integration_config.json` in a parent directory) and loads merged config from file + environment variables.

### ``_load_config(self) -> Dict``

Core logic: reads JSON file (if exists) and merges with environment variables for all supported keys (e.g., `OPENWEATHERMAP_API_KEY`).

### ``get(self, key`

str, default: any = None) -> any`**: Retrieves a config value by key, falling back to `default` if missing.

### ``has_api_key(self, service`

str) -> bool`**: Validates if an API key exists for a given service (e.g., `openweathermap` → checks `openweathermap_api_key`).

## Usage

```python
config = IntegrationConfig()  # Auto-detects config.json path
print(config.get("openweathermap_api_key"))  # Fallback to env var if file exists
if config.has_api_key("google_maps"):       # Check availability
    api_key = config.get("google_maps_api_key")
```

## Dependencies

> ``os``
> ``json``
> ``pathlib` (Python standard libraries).`

## Related

- [[`env_vars]]
- [[`api_keys]]

>[!INFO] Priority Order
> Environment variables take precedence over JSON file values. If both fail, defaults (empty strings) are used.

>[!WARNING] Case-Sensitive Flags
> SDK enablement flags (`DJI_SDK_ENABLED`, `PARROT_SDK_ENABLED`) must be lowercase (`true`/`false`) to match internal logic. Uppercase values (e.g., `TRUE`) will default to `False`.
