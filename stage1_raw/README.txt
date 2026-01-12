### FILENAME
README

### TAGS
#integration, #api, #drone, #simulation, #open-source, #geospatial, #weather, #3d, #configuration

### TYPE
documentation

### SUMMARY
Directory documentation for HMRS simulation system integration modules, detailing external service APIs and drone SDK adapters.

### DETAILS
This `README` describes a directory of integration modules for the HMRS simulation system, providing access to external services like OpenStreetMap, Google Maps 3D tiles, and weather APIs. Modules include building data extraction, photorealistic 3D mesh access, weather data fetching, drone SDK unification, time-of-day restrictions, and configuration management. Modules are designed to be modular, extensible, and compatible with global coverage requirements.

### KEY_FUNCTIONS
- **OSMBuildingsIntegration**: Fetches building data from OpenStreetMap via Overpass API.
- **GoogleMaps3DIntegration**: Retrieves high-quality 3D building meshes from Google Maps Platform.
- **WeatherAPIIntegration**: Provides real-time weather data (wind speed, temperature, etc.) via OpenWeatherMap API.
- **create_adapter**: Unified interface for drone SDKs (DJI, Parrot).
- **TimeRestrictionEnforcer**: Enforces time-based drone operation restrictions.
- **get_config**: Manages API key storage and configuration settings.

### DEPENDENCIES
- Python libraries (e.g., `requests`, `geopy` for geospatial operations)
- External APIs (OpenStreetMap, Google Maps Platform, OpenWeatherMap)
- Environment variables for API keys

### USAGE
1. Import modules via `swarm.integrations`.
2. Initialize integrations (e.g., `OSMBuildingsIntegration()`).
3. Configure API keys in environment variables or `config.py`.
4. Use provided functions (e.g., `get_buildings_in_radius()`).

### RELATED
[[swarm.integrations.osm_buildings.py]], [[swarm.integrations.google_maps_3d.py]], [[swarm.integrations.drone_brand_adapters.py]]

### CALLOUTS
>[!INFO]- Important Note
> Modules require API keys (e.g., OpenWeatherMap, Google Maps Platform) for functionality. Keys must be securely stored in environment variables or config files.
>[!WARNING]- Caution
> Time restrictions (`TimeRestrictionEnforcer`) must be configured before use to avoid runtime errors. Unauthorized API key usage may invalidate service access.