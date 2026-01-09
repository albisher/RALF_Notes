# 0021-kuwait-test-locations

> [!WARNING] JSON parsing failed

**Raw model output:**
```text
```json
{
  "filename": "0021-kuwait-test-locations",
  "tags": ["#kuwait", "#test-locations", "#osm", "#simulation", "#geospatial"],
  "type": "test-reference",
  "summary": "Kuwait test locations for validating OSM and Cesium building coverage",
  "details": "This document provides coordinates, expected coverage, and verification steps for two key test sites in Kuwait: a residential home and the PAAET campus. It includes Python and JavaScript test scripts to query OSM data and visualize results in Cesium, alongside OpenStreetMap and Overpass Turbo links for manual verification.",
  "key_functions": [
    {
      "name": "OSMBuildingsIntegration.get_buildings_in_radius",
      "purpose": "Retrieves buildings within a specified radius using latitude/longitude coordinates from OSM data"
    },
    {
      "name": "Cesium.createOsmBuildingsAsync",
      "purpose": "Loads OpenStreetMap building data for visualization in Cesium 3D environment"
    }
  ],
  "dependencies": ["OpenStreetMap API", "Cesium.js library", "Python/CesiumJS runtime"],
  "usage": "1. Use Python script to validate building counts at specified coordinates. 2. Load CesiumJS with coordinates to visualize 3D buildings. 3. Cross-check results with OpenStreetMap links and Overpass queries.",
  "related": [
    "[[0021-real-world-street-maps-from-gps.md]]"
  ],
  "callouts": [
    "> [!INFO]- **Key OSM Coverage Metrics**: Home location expects 10-50 buildings in 500m radius, while PAAET should yield 50-200+ in 1km.",
    "> [!TIP]- **Coordinate Precision**: Lat/long values are formatted to 15 decimal places for high-resolution testing."
  ],
  "code_summary": "
```python
# Core logic: Query OSM buildings by radius
def test_kuwait_locations():
    osm = OSMBuildingsIntegration()
    home_buildings = osm.get_buildings_in_radius(latitude=29.234431, longitude=48.054988, radius_meters=500)
    paaet_buildings = osm.get_buildings_in_radius(latitude=29.332763, longitude=47.915568, radius_meters=1000)
    return 
