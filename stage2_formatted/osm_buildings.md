**Tags:** #OpenStreetMap, #3D-building-integration, #API-query, #Geospatial-data
**Created:** 2026-01-13
**Type:** code-library

# osm_buildings

## Summary

```
Fetches and processes OpenStreetMap building data for simulation use via Overpass API.
```

## Details

> This module integrates with OpenStreetMap to retrieve building geometries and metadata within a specified radius of given coordinates. It uses the Overpass API to construct and execute queries, then parses the results into structured dictionaries. Rate limiting prevents excessive API calls, and error handling manages network/API failures gracefully.
> 
> The `OSMBuildingsIntegration` class encapsulates the logic: `get_buildings_in_radius()` constructs an Overpass query, sends it to the API, and returns parsed building data. The `_parse_osm_data()` helper processes raw OSM JSON responses into usable formats.

## Key Functions

### ``get_buildings_in_radius``

Queries OSM for buildings within a radius of given coordinates, enforces rate limiting, and returns parsed results.

### ``_parse_osm_data``

Internal method to convert raw OSM JSON into structured dictionaries (not exposed publicly).

### ``__init__``

Initializes rate-limiting tracking and API constants.

## Usage

```python
# Initialize the integrator
osm = OSMBuildingsIntegration()

# Fetch buildings near a point (e.g., 40.7128° N, 74.0060° W, radius=500m)
buildings = osm.get_buildings_in_radius(latitude=40.7128, longitude=-74.0060)
```

## Dependencies

> `requests`
> `time`

## Related

- [[osm_api_guide]]
- [[rate_limiting_notes]]

>[!INFO] Rate Limiting
> The `min_query_interval` (1 second) prevents API abuse. Exceeding this will pause execution until the interval resets.

>[!WARNING] API Dependency
> Requires `requests`; missing it will log a warning and return empty results. Install with `pip install requests`.
