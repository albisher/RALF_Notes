**Tags:** #Flask, #API, #Location Services, #Geospatial, #Proximity Search, #Biome Detection
**Created:** 2026-01-13
**Type:** documentation

# location_bp

## Summary

```
API Blueprint for generating, parsing, and analyzing location data with biome detection and clustering capabilities.
```

## Details

> This Flask-based API Blueprint (`location_bp`) integrates with a `location_service` to provide endpoints for coordinate generation, biome detection, and proximity searches. It handles JWT authentication and validates input ranges (e.g., latitude between -90 to 90, longitude between -180 to 180). The service supports generating locations from hash seeds, parsing coordinate strings, querying biome data, and clustering nearby locations within a specified radius.
> 
> The code dynamically imports time-related generators if available, though this feature is conditionally enabled. Error handling is centralized via Flask’s `logger` for debugging.

## Key Functions

### ``health_check()``

Returns service status, including availability of generators and proximity search.

### ``generate_location()``

Generates coordinates from a seed (with optional zone hint) and returns formatted data (latitude, longitude, biome, etc.).

### ``parse_coordinates()``

Converts a string input (e.g., `"c=40.7128,-74.0060 z=10"`) into parsed coordinates and biome.

### ``get_biome()``

Retrieves biome information for given latitude/longitude after validation.

### ``generate_location_cluster()``

Creates a cluster of locations around a seed, with adjustable size and radius.

## Usage

1. **Install Dependencies**: Ensure Flask, Flask-JWT-Extended, and `location_service` are installed.
2. **Register Blueprint**: Attach `location_bp` to a Flask app with `url_prefix='/api/location'`.
3. **Call Endpoints**:
   - `/health`: Check service status.
   - `/generate`: POST with `seed` and optional `zone_hint`.
   - `/parse`: POST with `coordinate_string`.
   - `/biome`: POST with `latitude` and `longitude`.
   - `/cluster`: POST with `center_seed`, `cluster_size`, and `radius_km`.

## Dependencies

> ``flask``
> ``flask-jwt-extended``
> ``location_service``
> ``models` (WorldElement`
> `User`
> `World`
> `db)`
> ``logging``
> ``sys``
> ``os``
> ``json` (implicitly).`

## Related

- [[Flask API Documentation]]
- [[Location Service Module]]
- [[WorldElement Model]]

>[!INFO] **JWT Authentication**
> All endpoints except `/health` require a valid JWT token via `@jwt_required()`. Missing auth returns a 401 error.

>[!WARNING] **Input Validation**
> Validate coordinates (latitude/longitude ranges) and cluster parameters (e.g., `cluster_size` must be 1–20). Invalid inputs return 400 errors.

>[!WARNING] **Error Handling**
> Logs errors to `logger` under `__name__`; returns generic 500 errors for unhandled exceptions.
