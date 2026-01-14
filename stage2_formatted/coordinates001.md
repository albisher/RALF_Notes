**Tags:** #Geographic Coordinate Systems, #Spherical Coordinates, #Cartesian Conversion, #Geodesy
**Created:** 2026-01-13
**Type:** research

# coordinates001

## Summary

```
Explains a centered-globe coordinate system for mapping latitude and longitude, detailing conversion formulas for spherical-to-Cartesian coordinates.
```

## Details

> This system centers the globe at (0,0) with latitude ranging from **–90° (South Pole)** to **+90° (North Pole)** and longitude spanning **–180° to +180° (W180 to E180)**. Latitude measures angular distance from the equator, while longitude measures angular distance from the prime meridian (Greenwich). The formulas convert spherical coordinates (latitude *φ*, longitude *λ*, radius *r*) to Cartesian coordinates (x, y, z) using trigonometric functions. Deviations occur if Earth is modeled as an ellipsoid instead of a perfect sphere, requiring adjusted formulas for varying radii.

## Key Functions

### `Spherical-to-Cartesian Conversion`

Converts geographic coordinates (φ, λ) to Cartesian (x, y, z) using trigonometric identities.

### `Ellipsoidal Adjustment`

Accounts for Earth’s oblate spheroid shape, modifying formulas for non-spherical reference surfaces.

## Usage

1. Define latitude (*φ*) and longitude (*λ*) in radians.
2. Use the formulas:
   - `x = r * cos(φ) * cos(λ)`
   - `y = r * cos(φ) * sin(λ)`
   - `z = r * sin(φ)`
   For ellipsoids, substitute the ellipsoidal radius formula (e.g., WGS84).

## Dependencies

> `None (mathematical definitions only; relies on basic trigonometry).`

## Related

- [[Geographic Coordinate Systems]]
- [[Spherical Earth Models]]

>[!INFO] **Key Assumption**
> This system assumes a **perfect sphere** of radius *r*. For Earth’s actual shape (ellipsoid), use geodetic formulas (e.g., WGS84) to account for flattening at poles.

>[!WARNING] **Longitude Range**
> Longitude spans **–180° to +180°** (not 0°–360°), ensuring a single global center at (0,0).
