**Tags:** #ROS2, #DDS, #MAVLink, #communication_protocol, #addon, #simulation, #networking, #queue, #threading, #signal_strength
**Created:** 2026-01-13
**Type:** code-notes

# communication_addon

## Summary

```
Handles simulation and management of communication protocols (ROS2, DDS, MAVLink) with signal strength tracking and message queuing.
```

## Details

> This file defines a `CommunicationAddon` class inheriting from `BaseAddon`, designed to simulate communication behaviors for drones or IoT devices. It initializes parameters for communication protocols (e.g., bandwidth, latency, power) and implements a signal strength simulation model using path loss and receiver sensitivity. The class manages message queues (`outgoing_messages`, `incoming_messages`) for asynchronous communication, tracks subscribers/publishers via dictionaries, and logs message history and failures. Threading and queue-based design ensure non-blocking message handling.

## Key Functions

### ``__init__``

Initializes communication attributes (bandwidth, latency, protocol) and simulation parameters (transmit/receiver power, frequency, path loss).

### ``signal_strength_cache``

Stores RSSI/SNR metrics for each target (keyed by `target_name`).

### ``subscribers`/`publishers``

Maps topics to callback queues for ROS2/DDS-style communication.

### ``sent_messages`/`received_messages``

Logs message history for debugging/analysis.

### ``failed_messages``

Tracks dropped messages due to poor signal.

## Usage

1. Subclass `CommunicationAddon` and override `__init__` to set custom protocol-specific parameters.
2. Use `self.outgoing_messages.put()` to send messages, `self.incoming_messages.get()` to receive.
3. Register subscribers via `self.subscribers[topic] = callback` and publishers via `self.publishers[topic] = queue`.
4. Simulate signal degradation by adjusting `path_loss_exponent` or `receiver_sensitivity_dbm`.

## Dependencies

> `numpy`
> `typing`
> `threading`
> `queue`
> `json (built-in)`
> ``.base_addon` (local module).`

## Related

- [[ROS2 Communication Patterns]]
- [[DDS Message Queues]]
- [[MAVLink Protocol Guide]]

>[!INFO] Signal Strength Simulation
> Uses a path loss model (`path_loss_exponent`) to estimate communication range based on distance from the receiver. Adjust `reference_distance_m` and `frequency_mhz` for accuracy.

>[!WARNING] Thread Safety
> Message queues (`Queue`) are thread-safe, but concurrent modifications to `subscribers`/`publishers` dictionaries require synchronization (e.g., `threading.Lock`). Avoid race conditions.
