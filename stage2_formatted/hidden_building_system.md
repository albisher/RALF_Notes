**Tags:** #simulation, #autonomous_exploration, #pybullet, #hidden_buildings, #testing, #building_generation, #ground_truth
**Created:** 2026-01-13
**Type:** code-notes

# hidden_building_system

## Summary

```
A PyBullet-based system for generating hidden buildings to test autonomous exploration and mapping.
```

## Details

> The `HiddenBuildingSystem` class manages static buildings in a PyBullet physics simulator, ensuring they are invisible to command & control (C&C) while accessible to drones via sensor ray casting. It implements a "separation of knowledge" principle: the simulator holds ground truth data, while C&C must discover buildings through sensor inputs alone. The system generates simple rectangular towers with configurable positions, sizes, and IDs, storing their geometry in a structured format for later retrieval.

## Key Functions

### ``__init__(physics_client`

int, storage_path: str)`**: Initializes the system with a PyBullet client and directory for ground truth storage.

### ``generate_simple_tower(position`

Tuple[float, float, float], size: Tuple[float, float, float], building_id: str)`**: Creates a static rectangular tower with collision and visual shapes, returning its ID for reference.

## Usage

1. Instantiate `HiddenBuildingSystem` with a PyBullet client ID and storage path.
2. Call `generate_simple_tower()` to create buildings with customizable dimensions and positions.
3. Retrieve ground truth data from `self.ground_truth_buildings` or saved JSON files in `storage_path`.

## Dependencies

> `numpy`
> `pybullet`
> `json`
> `os`

## Related

- [[simulation_environment_setup]]
- [[autonomous_mapping_algorithms]]

>[!INFO] Ground Truth Storage
> Buildings are stored in `self.ground_truth_buildings` as a dictionary mapping IDs to bounding box coordinates (min/max). The system also creates JSON files in `storage_path` for persistence.

>[!WARNING] Static Physics
> Buildings are static (mass=0) to avoid simulation instability. Ensure drones use collision detection to avoid collisions with these structures.
