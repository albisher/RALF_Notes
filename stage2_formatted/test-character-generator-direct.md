**Tags:** #testing, #character-generator, #direct-execution, #seed-based-generation, #python-script
**Created:** 2026-01-13
**Type:** code-test

# test-character-generator-direct

## Summary

```
Tests a Python-based character generator using direct command-line execution with different seeds to verify deterministic output.
```

## Details

> This script verifies the functionality of a Python character generator (`characters.py`) by running it via `execSync` with two distinct input seeds (`test_character_seed` and `another_test_seed`). It checks:
> 1. **Hash-based generation** (output consistency for identical seeds).
> 2. **Deterministic behavior** (same seed produces identical character).
> 3. **Seed variability** (different seeds yield distinct outputs).
> 4. **Physical linking** (implicitly assumes the generator produces valid character data).
> 
> The script uses `child_process.execSync` to execute the Python script in a controlled directory, capturing and logging results. Errors are caught and logged for debugging.

## Key Functions

### `execSync`

Executes the Python script with input seeds via shell command.

### `path.join`

Constructs the absolute path to `characters.py` for execution.

### `console.log/error`

Outputs test results and errors in structured format.

## Usage

1. Run the script directly in a Node.js environment.
2. Verify logs show deterministic output for identical seeds and varied results for different seeds.
3. Check for errors in `❌ Error testing character generator:` if execution fails.

## Dependencies

> ``child_process``
> ``path` (Node.js built-ins)`
> `Python (`characters.py` script).`

## Related

- [[none]]

>[!INFO] Important Note
> The script assumes `characters.py` is in `Generators/Characters/` relative to the test file. Adjust paths if the structure differs.

>[!WARNING] Caution
> `execSync` blocks the Node.js process. Use `exec` (async) for non-blocking tests in production.
