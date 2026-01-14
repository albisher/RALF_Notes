**Tags:** #world-generation, #robot-simulation, #api-integration, #data-structures
**Created:** 2026-01-13
**Type:** documentation-research

# create_space_peral_world

## Summary

```
Script automates creation of a fictional sci-fi world ("Space Peral") with predefined characters, robots, and elements via API calls.
```

## Details

> This script interacts with a backend API to:
> 1. Authenticate and retrieve an existing world or create a new "Space Peral" colony world
> 2. Populate it with predefined elements (characters, robots, buildings) based on provided documentation
> 3. Uses a token-based authentication system and handles both existing and new world scenarios
> 
> The world is designed as a self-sustaining colony with a central library created by Mc. Liberian Taba, featuring robotic characters and exploration drones.

## Key Functions

### `login()`

Authenticates with the API using test credentials.

### `get_existing_world(token)`

Finds the most populated existing Space Peral world by name.

### `create_world(token)`

Creates a new world if none exists, with detailed colony specifications.

### `generate_element(token, world_id, element_type, name, description, additional_data)`

Creates individual elements (characters/robots) with configurable metadata.

### `create_space_peral_elements(token, world_id)`

Orchestrates the population of all predefined Space Peral elements.

## Usage

1. Run script to authenticate and determine world state
2. Call `create_space_peral_elements()` to populate the world with predefined characters/robots
3. Elements are created with standardized metadata including personality traits and roles

## Dependencies

> `requests`
> `json`
> `datetime`

## Related

- [[Space Peral Documentation]]
- [[X-Series Robot Specifications]]

>[!INFO] Authentication Note
> Uses hardcoded test credentials ("test"/"passtest") for demonstration purposes only. In production, replace with secure credentials management.

>[!WARNING] World Conflict Warning
> If multiple runs occur, the script may overwrite existing elements. Consider adding version control or conflict resolution logic for production use.
