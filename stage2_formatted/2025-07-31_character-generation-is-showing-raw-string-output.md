**Tags:** #debugging, #json-formatting, #data-structures, #api-integration, #procedural-generation
**Created:** 2026-01-13
**Type:** research-notes

# 2025-07-31_character-generation-is-showing-raw-string-output

## Summary

```
Investigates why a character generator outputs raw string data instead of structured JSON, contrasting with a working robot generator.
```

## Details

> The issue arises when the character generator returns a concatenated string of key-value pairs (e.g., `'0:A', '1:v', '2:e'`) rather than a properly formatted JSON object. The robot generator, in contrast, outputs structured JSON (e.g., `{ "0": "A", "1": "v", "2": "e" }`). The root cause is likely improper serialization of internal data structures. The fix involves ensuring the generator returns a Python dictionary/list and serializes it to JSON with formatting options like `indent=4` and `sort_keys=True` to match the robot generator’s output style.

## Key Functions

### `character_generator()`

Returns raw string output instead of structured JSON.

### `json.dumps()`

Serializes structured data into formatted JSON (e.g., `json.dumps(data, indent=4)`).

### `robot_generator()`

Correctly outputs structured JSON (reference implementation).

## Usage

1. Modify the character generator to return a dictionary/list of character data (e.g., `{"0": "A", "1": "v"}`).
2. Use `json.dumps()` to format the output with `indent=4` and `sort_keys=True` for readability.
3. Ensure the frontend (e.g., Vue) parses the JSON correctly without manual string manipulation.

## Dependencies

> ``json` (Python standard library)`
> `Flask API backend (if applicable)`
> `Vue.js frontend (for JSON parsing).`

## Related

- [[Flask API Design Notes]]
- [[Procedural Content Generation Guide]]

>[!INFO] Debugging Tip
> Check if the character generator’s internal data structure is a string or a dictionary. If it’s a string, split/parse it into a dictionary before serialization.

>[!WARNING] Frontend Compatibility
> If the frontend expects raw strings, ensure the JSON output is parsed correctly (e.g., `JSON.parse()` in JavaScript). Inconsistent parsing may reintroduce raw string behavior.
