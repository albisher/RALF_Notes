**Tags:** #communication, #ros2, #dds, #drones, #real-time, #inter-drone, #ground-station
**Created:** 2026-01-12
**Type:** documentation

# communication-overview

## Summary

```
Provides an overview of the communication architecture for HMRS drones using ROS2 and DDS middleware.
```

## Details

> This document outlines the communication system for HMRS drones, which includes inter-drone coordination, ground station communication, and data transmission. The system leverages ROS2 for its robust topic-based publish-subscribe and service-based communication, alongside DDS middleware (Fast DDS or Cyclone DDS) for reliable, real-time data exchange. The **Micro XRCE-DDS Agent** bridges PX4 flight controllers to the ROS2/DDS ecosystem, enabling seamless integration between drone hardware and software.

## Key Functions

### `ROS2`

Manages distributed communication via topics, services, and actions.

### `Fast DDS (eProsima)`

Provides configurable, scalable DDS implementation for ROS2.

### `Cyclone DDS (Eclipse)`

Alternative high-performance DDS middleware for ROS2.

### `Micro XRCE-DDS Agent`

Translates uORB messages from PX4 to DDS-compatible data for ROS2.

## Usage

1. Install ROS2 and select a DDS middleware (Fast DDS or Cyclone DDS).
2. Deploy Micro XRCE-DDS Agent (standalone, Snap, or ROS2 workspace) to bridge PX4 to ROS2.
3. Configure drone nodes to publish/subscribe via ROS2 topics/services using DDS.

## Dependencies

> `ROS2`
> `Fast DDS`
> `Cyclone DDS`
> `Micro XRCE-DDS-Agent (eProsima)`
> `PX4 flight controller software.`

## Related

- [[01-ros2-specifications]]
- [[02-ros2-integration]]
- [[04-dds-middleware-specifications]]
- [[05-dds-middleware-integration]]

>[!INFO] Key Integration Point
> The **Micro XRCE-DDS Agent** is critical for translating PX4’s uORB messages into ROS2/DDS topics, ensuring compatibility between flight controllers and ROS2-based ground stations.

>[!WARNING] Network Dependency
> DDS communication relies on a stable network; latency or packet loss may disrupt real-time drone coordination. Test with simulated network conditions before deployment.
