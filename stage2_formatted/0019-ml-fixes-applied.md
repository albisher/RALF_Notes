**Tags:** #machine-learning, #strategy-adaptation, #decision-making, #optimization, #ai-improvements
**Created:** 2026-01-13
**Type:** code-notes

# 0019-ml-fixes-applied

## Summary

```
Applies machine learning fixes to improve mission strategy selection via feature-based learning and adaptive decision-making.
```

## Details

> This document outlines four key fixes for a machine learning system that previously relied on random selection. The system now dynamically learns optimal strategies from mission outcomes, incorporating features like building height and distance. The `DecisionLearningBox` component records sessions, adjusts strategy weights based on success/failure, and prioritizes successful approaches. Features are tracked in `building_height`, `distance_to_target`, and others, enabling data-driven decision-making. The implementation uses weighted random selection to balance exploration and exploitation.

## Key Functions

### ``DecisionLearningBox``

Core class that learns from mission outcomes, tracks sessions, and updates strategy weights.

### ``record_session()``

Logs features, decisions, and outcomes for each mission.

### ``_learn_from_success()` / `_learn_from_failure()``

Dynamically adjusts strategy weights based on outcomes.

### ``select_target()``

Uses building features (e.g., distance, height) to refine target selection.

### ``allocate_scouts()``

Allocates scouts based on distance matching and learned weights.

### ``simulation/swarm/boxes/decision_learning_box.py``

New file implementing learning logic.

### ``simulation/hmrs_simulation_live.py``

Updated to integrate learned strategies.

## Usage

1. Initialize `DecisionLearningBox` with mission data.
2. Call `record_session()` after each mission to log outcomes.
3. The system automatically updates strategy weights and selects the next approach based on learned probabilities.
4. Features (e.g., `building_height`, `distance_to_target`) are dynamically used to refine decisions.

## Dependencies

> ``json` (for saving learned weights)`
> ``numpy` (for normalization)`
> ``simulation` module (core simulation logic).`

## Related

- [[`0018-ml-baseline-implementation`]]
- [[`0020-ml-evaluation-results`]]

>[!INFO] Feature Tracking
> Features like `building_height` and `distance_to_target` are now critical for decision-making. Ensure these are consistently logged in `session_memory` to maintain accuracy.

>[!WARNING] Weight Normalization
> Manual intervention may be needed if weights drift outside expected bounds (e.g., extreme success/failure rates). The system normalizes weights, but edge cases require validation.
