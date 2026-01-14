**Tags:** #world-generation, #hash-based, #robotic-systems, #procedural-content, #ai-assisted
**Created:** 2026-01-13
**Type:** documentation-research

# generate_w23_world

## Summary

```
Generates a procedural world (W23) with deterministic hash-based characters, robotic bodies, and plant-integrated buildings using a backend API.
```

## Details

> This script creates a deterministic world by generating consistent hashes for characters, robotic bodies, buildings, and plants using MD5 hashing. It uses a `HashGenerator` class to derive seeds for random traits (e.g., intelligence, specialization) and robotic enhancements. The script interacts with a local backend (`localhost:8443`) to authenticate and submit generated elements, while disabling SSL verification for testing. It supports modular generation of characters with roles, robotic bodies, and buildings with surrounding plants, using time-based offsets for uniqueness.

## Key Functions

### `HashGenerator`

Generates consistent hashes for world elements (characters, robots, buildings, plants) and converts them to seeds for deterministic trait generation.

### `create_test_user`

Authenticates with a test user (`test/passtest`) to access the backend API.

### `generate_character_with_robot`

Creates a character and its robotic body using hash-derived seeds for traits (e.g., intelligence, specialization, enhancement type).

### `generate_building_with_plants`

Generates a building with plant specifications (e.g., size, style, height) and surrounding vegetation, also using hash-based randomness.

## Usage

1. Run the script with Python 3 (`python3 generate_w23_world.py`).
2. Ensure the backend (`localhost:8443`) is running and accessible.
3. Call `create_test_user()` to authenticate, then use `HashGenerator` to generate elements (e.g., `hash_gen.generate_character_hash("Alice")`).
4. Submit generated data via the backend API using the returned token.

## Dependencies

> `requests`
> `urllib3`
> `hashlib`
> `datetime`
> `pathlib`

## Related

- [[None]]

>[!INFO] **Deterministic Hashing**
> Hashes ensure reproducibility—same input produces identical traits. Useful for debugging or regenerating worlds with identical seeds.

>[!WARNING] **SSL Verification Disabled**
> `session.verify = False` bypasses SSL checks. Only use in trusted environments; risk of MITM attacks in production.

>[!WARNING] **Backend Dependency**
> The script relies on `localhost:8443`. Replace `BACKEND_URL` if deploying elsewhere. Test with a local server first.
