**Tags:** #machine-learning, #drone-control, #neural-networks, #reinforcement-learning, #autonomous-systems
**Created:** 2026-01-13
**Type:** code-notes

# ml_controller

## Summary

```
A neural-network-based drone controller that learns optimal flight control from past experiences.
```

## Details

> The `MLController` class implements a simple two-layer neural network for drone control. It initializes weights randomly and uses ReLU and sigmoid activations. The controller processes input states (position, velocity, orientation) to produce motor thrust outputs. It tracks flight performance metrics and manages exploration decay for reinforcement learning.

## Key Functions

### ``__init__``

Initializes a 2-layer neural network with configurable input/hidden/output sizes, learning parameters, and exploration settings.

### ``relu``

Implements ReLU activation function for hidden layer.

### ``sigmoid``

Implements sigmoid activation for output layer.

### ``forward``

Computes neural network predictions from input states (padded/truncated to match input_size).

### ``get_control``

(Incomplete) Placeholder for state-based control logic (missing implementation).

## Usage

Initialize with `MLController(input_size=12, hidden_size=16, output_size=4)`.
Call `forward()` with state vectors to generate motor outputs.
Track flight success/failure metrics via `total_flights`, `successful_flights`, etc.

## Dependencies

> `numpy`
> `pickle`
> `os`
> `datetime`

## Related

- [[none]]

>[!INFO] Exploration Decay
> The `exploration_rate` starts at 30% and decays toward 5% over time, balancing exploration/exploitation.

>[!WARNING] State Truncation
> Input states are padded/truncated to `input_size`; ensure input vectors match expected dimensions.
