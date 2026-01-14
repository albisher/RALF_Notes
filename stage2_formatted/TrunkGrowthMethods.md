**Tags:** #growth-patterns, #biological-modelling, #plant-simulation, #trunk-growth-algorithms
**Created:** 2026-01-13
**Type:** code-notes

# TrunkGrowthMethods

## Summary

```
Describes potential growth methods for a trunk or plant model in a simulation.
```

## Details

> This file outlines various growth behaviors for a trunk or plant structure, including directional, angular, and patterned growth modes. The listed methods represent possible configurations for simulating how a plant trunk or similar structure expands, such as branching angles, linear growth, or rotational patterns.

## Key Functions

### `BranchAngleMethods`

Handles angular growth (e.g., 90°, 45° branching).

### `SpiralGrowth`

Implements a helical or rotational expansion pattern.

### `LinearGrowth`

Simulates straight, horizontal or vertical growth without branching.

### `ZigzagGrowth`

Models alternating directional shifts in growth.

## Usage

This file serves as a conceptual reference for defining growth rules in a plant/trunk simulation framework. Developers would integrate these patterns into a growth algorithm by selecting or combining applicable methods based on desired behavior.

>[!INFO] Important Note
> These patterns are **theoretical** and may require additional physics or environmental constraints (e.g., soil resistance) for realistic results. Adjustments may be needed for dynamic simulations.

>[!WARNING] Caution
> Overly rigid patterns (e.g., pure vertical growth) may not reflect natural variability. Hybrid approaches (e.g., combining spiral + branching) are often more biologically plausible.
