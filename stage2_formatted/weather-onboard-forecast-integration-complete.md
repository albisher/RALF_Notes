**Tags:** #weather_integration, #onboard_sensors, #api_integration, #gps_coordinates, #priority_system
**Created:** 2026-01-12
**Type:** code-notes

# weather_onboard_forecast_integration_complete

## Summary

```
Integrates on-board weather sensors with internet forecasts for real-time drone weather data.
```

## Details

> This system merges real-time drone sensor data with external weather forecasts, prioritizing onboard measurements over API-based predictions. It dynamically updates weather conditions every 10 minutes, falling back to simulated data if neither sensors nor forecasts are available. The architecture supports base GPS coordinates for API requests and automatically detects onboard weather stations.

## Key Functions

### ``set_base_gps()`** (in `weather_system.py`)`

Configures GPS coordinates for API-based forecasts.

### ``update_from_onboard_sensors()`** (in `weather_system.py`)`

Processes drone sensor data (wind, temp, humidity, etc.).

### ``update()`** (in `weather_system.py`)`

Periodically fetches forecasts from OpenWeatherMap API.

### ``WeatherAPIIntegration`** (in `weather_system.py`)`

Handles API calls for forecast data.

### ``base_latitude`/`base_longitude`** (in `simulation/hmrs_simulation_live.py`)`

Stores GPS coordinates for API requests.

## Usage

1. Set base GPS coordinates via `sim.set_base_gps(latitude, longitude)`.
2. Ensure drones have `WeatherStationAddon` for sensor data.
3. Call `weather_system.update()` to refresh forecasts (or let it auto-update every 10 minutes).
4. Drone weather data prioritizes onboard sensors over forecasts.

## Dependencies

> ``WeatherStationAddon``
> `OpenWeatherMap API`
> ``simulation/swarm/base_drone.py``
> ``simulation/swarm/weather_system.py`.`

## Related

- [[base_drone]]
- [[weather_system]]
- [[WeatherStationAddon documentation]]

>[!INFO] Priority Logic
> Onboard sensors take precedence over API forecasts. If sensors fail, the system defaults to simulated weather.

>[!WARNING] API Dependency
> Requires OpenWeatherMap API access. Latitude/longitude must be valid for forecasts to work.
