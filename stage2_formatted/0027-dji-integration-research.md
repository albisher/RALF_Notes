**Tags:** #DJI, #DroneSDK, #MAVLink, #ProprietaryProtocol, #OnboardSDK, #SimulatorIntegration, #UDP/TCP, #Telemetry, #AutonomousDrone, #FlightController
**Created:** 2026-01-12
**Type:** research

# 0027-dji-integration-research

## Summary

```
Researches DJI SDK integration options, protocols, and compatibility with existing HMRS simulator architecture for drone behavior emulation.
```

## Details

> This document analyzes DJI’s SDK options, emphasizing the **non-MAVLink proprietary protocols** (binary-encoded, encrypted, high-frequency telemetry) used for drone integration. The existing HMRS simulator is well-suited for DJI integration via an adapter pattern, particularly the `DJIAdapter` framework in `simulation/swarm/integrations/drone_brand_adapters.py`. The **Onboard SDK** is recommended for autonomous drones like Matrice 300/350 RTK, enabling full control via companion computers. The document details the proprietary communication stack (OcuSync/UART, TLS encryption, UDP/TCP) and binary packet structure, contrasting it with MAVLink.

## Key Functions

### ``DJIAdapter``

Framework for translating DJI proprietary commands into simulator-compatible formats.

### ``simulation/swarm/integrations/drone_brand_adapters.py``

Core adapter handling binary protocol parsing and telemetry synchronization.

### `Onboard SDK`

Enables full autonomy for industrial drones via companion hardware (e.g., Jetson Nano).

### `OcuSync/TCP/UDP`

High-bandwidth air-ground communication links for real-time telemetry.

## Usage

1. **Select SDK Tier**: Use **Onboard SDK** for autonomous drones (e.g., Matrice 350 RTK) with companion computer integration.
2. **Adapter Integration**: Implement `DJIAdapter` to bridge proprietary binary commands to simulator’s motion patterns.
3. **Telemetry Handling**: Map high-frequency telemetry (10–50 Hz) from UDP/TCP streams to simulator state.
4. **Protocol Compliance**: Ensure CRC checks, timestamp sync, and session management align with DJI’s encrypted binary protocol.

## Dependencies

> `- HMRS simulator core (motion patterns`
> `adapter pattern framework)
- DJI proprietary SDK libraries (Mobile/Onboard/Payload/Cloud APIs)
- UDP/TCP networking stack (for OcuSync communication)
- TLS/SSL encryption (for encrypted protocol packets)`

## Related

- [[HMRS Simulator Architecture]]
- [[MAVLink Integration Guide]]
- [[DJI SDK Documentation]]

>[!INFO] Important Note
> DJI’s proprietary protocols require **binary parsing** (not MAVLink), necessitating custom adapter logic for telemetry and command translation. The existing HMRS adapter pattern is ideal but must handle encrypted packets and high-frequency updates.


>[!WARNING] Caution
> Avoid direct MAVLink assumptions—DJI’s protocols include **TLS encryption**, **checksums**, and **session-based ACK/NACK**, which MAVLink lacks. Misalignment here could cause telemetry loss or command failures. Test with **UDP/TCP** first before serial/UART.
