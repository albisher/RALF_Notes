**Tags:** #API-Testing, #Database-Management, #World-Building, #Cyberpunk-Simulation
**Created:** 2026-01-13
**Type:** code-test

# api-database-test

## Summary

```
Automated API/database test suite for creating and managing a cyberpunk-themed virtual world, characters, and locations.
```

## Details

> This script performs automated testing of an API endpoint suite for a fictional cyberpunk universe. It handles authentication, world creation, character development, and location elements within a single world. The code uses Axios for HTTP requests, bypassing SSL certificate validation for testing self-signed certificates. It includes error handling for duplicate entries and gracefully falls back to retrieving existing resources when duplicates are detected.
> 
> The test suite sequentially:
> 1. Authenticates with a test API
> 2. Creates a cyberpunk-themed world
> 3. Attempts to create a character within that world
> 4. Creates a location element (temple)
> 5. Retrieves all worlds, characters, and elements
> 6. Attempts to save a fictional story to the database

## Key Functions

### `login()`

Authenticates with the API using test credentials.

### `createWorld()`

Creates a new cyberpunk world with specified details, handling duplicates by retrieving existing world data.

### `createCharacter(worldId)`

Creates a character within a specified world.

### `createElement(worldId)`

Creates a location element (like a temple) within a specified world.

### `getWorlds()`

Retrieves all worlds from the database.

### `getCharacters(worldId)`

Retrieves all characters belonging to a specific world.

### `getElements(worldId)`

Retrieves all elements (locations) within a specific world.

### `saveStoryToDatabase(worldId)`

Attempts to save a fictional story to the database (incomplete implementation shown in snippet).

## Usage

1. Run the script to execute the full test sequence
2. The script automatically handles authentication and error cases
3. For testing purposes, it uses hardcoded credentials ('test', 'passtest')
4. The script logs each operation's status with emoji indicators

## Dependencies

> `axios`
> `fs`
> `path`
> `https`

## Related

- [[API-Endpoint-Reference-for-Cyberpunk-Simulation]]
- [[Self-Signed-Certificate-Testing-Guide]]

>[!INFO] Important Note
> This script is designed for testing purposes only. The credentials ('test', 'passtest') may not work in production environments. The story saving functionality appears incomplete in the provided snippet.


>[!WARNING] Caution
> The script disables SSL certificate verification (`rejectUnauthorized: false`), which is unsafe for production use. Only use this in trusted local development environments with self-signed certificates.
