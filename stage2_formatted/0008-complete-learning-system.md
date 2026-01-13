**Tags:** #machine-learning, #neural-network, #drone-autonomy, #supervised-learning, #swarm-intelligence
**Created:** 2026-01-13
**Type:** code-notes

# 0008-complete-learning-system

## Summary

```
A 2-layer neural network controller for drones that learns flight patterns via supervised learning from successful scenarios.
```

## Details

> The `ml_controller.py` implements a lightweight neural network (2 hidden layers) to process drone state inputs (position, velocity, orientation, target, wind) and output motor thrust commands. It relies on an experience buffer storing successful flight data, enabling batch learning. Key features include model persistence (save/load), performance metrics tracking, and adaptation to weather conditions.

## Key Functions

### ``__init__()``

Initializes the 2-layer neural network with 12 input features and 4 output motor thrusts.

### ``learn_from_experience()``

Stores successful flight data in an experience buffer for later batch training.

### ``predict_motor_thrusts()``

Uses current state to generate motor commands based on trained weights.

### ``save_model()``

Persists the trained neural network weights to disk.

### ``load_model()``

Restores weights from a saved model file.

### ``track_performance()``

Logs metrics like success rate, error rates, and learning progress.

## Usage

1. Initialize the controller with a trained model or empty buffer.
2. Feed drone state data (e.g., position, wind) to `predict_motor_thrusts()`.
3. Store successful outcomes in `learn_from_experience()`.
4. Periodically call `save_model()` to persist progress.

## Dependencies

> ``numpy``
> ``tensorflow`/`keras` (for neural network implementation)`
> `custom `ExperienceBuffer` class (for storing flight data).`

## Related

- [[learning_drone]]
- [[learning_simulator]]
- [[scenario_generator]]

>[!INFO] **Experience Buffer Criticality**
> The `ExperienceBuffer` must be populated with successful flight data before training. Without data, the model defaults to random weights, reducing reliability.

>[!WARNING] **Weather Sensitivity**
> Wind inputs (e.g., `wind` feature) must be normalized to [0,1] or [-1,1] to avoid numerical instability in gradient updates. Unchecked scaling can degrade learning performance.
