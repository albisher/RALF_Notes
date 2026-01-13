**Tags:** #dependencies, #package-management, #api-integration, #drone-sdk
**Created:** 2026-01-13
**Type:** documentation

# requirements

## Summary

```
Document listing Python package requirements for API integrations and optional drone SDK support.
```

## Details

> This file outlines the necessary packages for a software module requiring API integrations, specifying both mandatory and optional dependencies. The core requirement is the `requests` library (version ≥2.28.0) for HTTP interactions. Optional but recommended is `pytz` (≥2022.1) for timezone-aware time handling. A separate installation is required for real drone control via SDKs (e.g., DJI or Parrot SDKs).

## Key Functions

### ``requests>=2.28.0``

Core HTTP client for API interactions.

### ``pytz>=2022.1``

Timezone-aware datetime handling (optional but recommended).

## Usage

Install via `pip install -r requirements.txt` for API support. Drone SDKs must be installed separately if needed.

## Dependencies

> ``requests``
> ``pytz` (optional)`
> `DJI SDK (`dji-sdk`)`
> `Parrot SDK (`olympe`)`

## Related

- [[none]]

>[!INFO] Mandatory Dependency
> `requests` is essential for all API integrations; omitting it breaks core functionality.

>[!WARNING] Separate Installation
> Drone SDKs (`dji-sdk`, `olympe`) are not included here—install them manually if drone control is required.
