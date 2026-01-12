**Tags:** #audit, #configuration, #hardcoded-values, #simulation, #environment-variables, #gps, #network-config, #dependency-management
**Created:** 2026-01-12
**Type:** documentation

# hardcoded-values-audit

## Summary

```
Document outlining hardcoded values in a simulation codebase requiring refactoring to environment variables or config files.
```

## Details

> This document serves as a comprehensive audit of hardcoded values across multiple files in a simulation system, identifying critical network settings, positional data, and city coordinates. The audit categorizes values into intentional defaults (e.g., base position at origin) and those requiring refactoring (e.g., port numbers, API URLs). Recommendations focus on moving static data to external configuration files or environment variables to improve maintainability and flexibility.

## Key Functions

### ``hmrs_simulation_live.py``

Core simulation logic with hardcoded network, positional, and city data.

### ``simulation/frontend/app-data.js``

Frontend configuration with hardcoded base position/orientation and OSM settings.

### ``docker/docker-compose.yml``

Containerized deployment with hardcoded port mappings.

## Usage

To apply this audit:
1. Replace hardcoded values in `hmrs_simulation_live.py` and frontend scripts with environment variables or config files.
2. Update `docker/docker-compose.yml` to dynamically set `FLASK_PORT` via an environment variable.
3. Document intentional defaults (e.g., base position/orientation) to avoid confusion.

## Dependencies

> `- Environment variables (`FLASK_PORT``
> ``API_BASE_URL`)
- External config files (`config/cities.json``
> ``config/gps_presets.json`)
- Network libraries (e.g.`
> `for OSM data integration)`

## Related

- [[configuration-guide]]
- [[`environment-variables]]

>[!INFO] Important Note
> Hardcoded values like `[0.0, 0.0, 0.0]` for base position are intentional in simulation coordinates and should not be refactored unless altering the simulation logic. Document these clearly to avoid breaking changes.


>[!WARNING] Caution
> Hardcoded `http://localhost:5007` URLs in test scripts may fail in non-local environments. Replace with environment variables like `API_BASE_URL` to ensure portability across deployments.
