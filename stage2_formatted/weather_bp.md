**Tags:** #Flask, #API, #Weather, #Database, #Authentication, #JWT, #SQLAlchemy, #World Management
**Created:** 2026-01-13
**Type:** documentation

# weather_bp

## Summary

```
Manages weather-related endpoints for a Flask-based application, handling calculations, saving, and retrieval of weather data with JWT authentication.
```

## Details

> This Flask blueprint (`WeatherManagementAPIBox`) provides endpoints for weather-related operations within a world management system. It integrates with a `WeatherCalculationBox` for dynamic weather computation and interacts with SQLAlchemy models (`Weather`, `World`, `Card`) to store and retrieve weather data. The API enforces JWT authentication to ensure user ownership of worlds and locations, validating requests before processing.
> 
> The system supports three primary operations:
> 1. **POST `/api/weather/calculate`**: Computes weather conditions for a given location using provided celestial objects and world conditions.
> 2. **POST `/api/weather/save`**: Persists weather data (e.g., temperature, humidity) into the database after validation.
> 3. **GET `/api/weather/location/<location_id>`**: Retrieves the latest weather record for a specified location.

## Key Functions

### ``WeatherManagementAPIBox``

Initializes the Flask blueprint and registers weather-related routes.

### ``calculate_weather``

Validates user access, computes weather using `WeatherCalculationBox`, and returns results or errors.

### ``save_weather``

Creates a new `Weather` record in the database after validating user permissions.

### ``get_location_weather``

Fetches the most recent weather data for a given location ID.

## Usage

1. **Initialize**: Create an instance of `WeatherManagementAPIBox` and register it with your Flask app.
2. **Call Endpoints**:
   - **Calculate Weather**: Send a POST request to `/api/weather/calculate` with `world_id`, `location_id`, and optional metadata (e.g., `timestamp`, `celestial_objects`).
   - **Save Weather**: POST to `/api/weather/save` with `world_id` and weather attributes (e.g., `weather_type`, `temperature`).
   - **Retrieve Weather**: GET `/api/weather/location/<location_id>` to fetch the latest weather record for a location.

## Dependencies

> ``flask``
> ``flask-jwt-extended``
> ``flask-sqlalchemy``
> ``models` (SQLAlchemy models)`
> ``WeatherCalculationBox``
> ``BoxInput`.`

## Related

- [[models]]
- [[weather_calculation_box]]
- [[box_interface]]

>[!INFO] Authentication Requirement
> All endpoints require a valid JWT token in the `Authorization` header. The `user_id` is extracted from the JWT payload for validation against owned worlds/locations.


>[!WARNING] Database Rollback
> If an error occurs during `save_weather`, the database session is rolled back to maintain data integrity. Ensure transactions are idempotent to avoid conflicts.
