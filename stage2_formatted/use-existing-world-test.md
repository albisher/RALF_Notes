**Tags:** #testing, #api-integration, #world-building, #character-generation, #element-creation
**Created:** 2026-01-13
**Type:** code-test-reference

# use-existing-world-test

## Summary

```
Tests integration with an existing virtual world API to authenticate, generate content, and verify operations.
```

## Details

> This script performs a comprehensive test of an API for an existing virtual world system. It authenticates via login, retrieves the world list, locates a predefined world ("Space Peral"), and executes a series of operations:
> 1. **Character generation** (with error handling)
> 2. **Element creation** (plants, animals, buildings)
> 3. **Story creation** (with embedded narrative data)
> 4. **Verification** of all created elements in the world.
> 
> The test follows a structured sequence of steps, each logged for debugging, and includes nested error handling for API failures.

## Key Functions

### ``axios.post`/`axios.get``

Handles HTTP requests with authentication headers.

### ``useExistingWorldTest``

Orchestrates the full test workflow.

### `World retrieval`

Fetches and validates the target world (`Space Peral`).

### `Element creation`

Dynamically posts structured data for plants, animals, buildings, and stories.

### `Story embedding`

Includes raw narrative content (Markdown-formatted) as part of the API payload.

## Usage

1. Run the script in a Node.js environment with the API server (`http://localhost:5173/api`) accessible.
2. Ensure credentials (`test`/`passtest`) match the API’s authentication requirements.
3. Replace `Space Peral` with a valid world name if needed (though the script checks for existence).
4. Monitor console logs for success/error messages during execution.

## Dependencies

> ``axios``
> ``node_modules` (for HTTP requests and error handling).`

## Related

- [[World API Documentation]]
- [[Character Generation Guide]]
- [[Element Creation Specifications]]

>[!INFO] Important Note
> The script uses a hardcoded seed (`test_x1_seed`) for character generation. Changing this may produce different results, but the test remains valid.

>[!WARNING] Caution
> If the API endpoint (`/worlds`) or `/characters/generate/hash` does not exist, the script will fail. Verify the API’s route structure before execution.

>[!INFO] Debugging Tip
> Add `console.log(error.stack)` to error handlers to inspect full error traces in Node.js environments.
