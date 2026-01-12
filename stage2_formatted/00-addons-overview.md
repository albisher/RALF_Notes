**Tags:** #hardware, #robotics, #drone, #sensor, #communication, #gps, #lidar, #camera, #flight-control, #addon, #system-overview
**Created:** 2026-01-12
**Type:** documentation

# 00-addons-overview

## Summary

```
Provides an organized overview of hardware addons for a multi-robot drone system, detailing categories, components, and documentation structure.
```

## Details

> This file serves as a central repository for all hardware addons required for the **HMRS (Heterogeneous Multi-Robot System)** drone project. It categorizes components into **GPS/RTK, LiDAR, Camera, Communication, Sensor, and Flight Controller** addons, each with dedicated subdirectories containing detailed specifications, integration guides, and documentation. The structure ensures modularity, allowing easy access to technical details, datasheets, and integration examples for each addon type.

## Key Functions

### ``00-[category]-overview.md``

Provides a high-level summary of each addon category (e.g., GPS/RTK, LiDAR).

### ``00-complete-addons-list.md``

Compiles a comprehensive list of all addons with download links and status updates.

### `Subdirectory-specific files (e.g., `01-[addon-name]-specifications.md`)`

Contains detailed technical specs for individual hardware components.

## Usage

1. Navigate to the `00-addons-overview` file to explore categories and subdirectories.
2. Use the linked overview files (e.g., `gps-rtk/00-gps-rtk-overview.md`) for deeper insights into specific addon types.
3. Refer to `00-complete-addons-list.md` for a consolidated list of all addons and their status.

## Dependencies

> `None (primarily documentation and reference files).`

## Related

- [[00-gps-rtk-overview]]
- [[00-lidar-overview]]
- [[00-camera-overview]]
- [[00-communication-overview]]
- [[00-sensors-overview]]
- [[00-flight-controller-overview]]
- [[00-complete-addons-list]]

>[!INFO] Key Integration Insight
> Each subdirectory follows a standardized structure (`00-overview.md`, `01-specs.md`, `02-integration.md`), ensuring consistency across addon types. This modular approach simplifies maintenance and updates.

>[!WARNING] Documentation Priority
> Prioritize updating `00-[category]-overview.md` and `01-[addon-name]-specifications.md` files to reflect hardware compatibility and performance metrics for real-time project adjustments.
