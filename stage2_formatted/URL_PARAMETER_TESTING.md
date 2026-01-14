**Tags:** #url-parameter-testing, #map-generator, #web-development, #testing-automation, #deterministic-generation
**Created:** 2026-01-13
**Type:** documentation

# URL_PARAMETER_TESTING

## Summary

```
A guide for testing the Map Generator via URL parameters to enable automated and reproducible map generation.
```

## Details

> This documentation outlines how to use URL parameters to test the Map Generator application. Users can navigate directly to predefined URLs containing parameters like `hash`, `worldType`, and `mapType`, triggering auto-generation of maps without manual input. The system supports URL encoding for special characters and allows optional parameters to control generation behavior (e.g., `generate=true/false`).

## Key Functions

### `URL Parameter Parsing`

Extracts and decodes parameters on component mount.

### `Auto-Populate Form`

Fills form fields dynamically from URL parameters.

### `Deterministic Generation`

Generates consistent maps based on provided `hash` and `worldType`.

### `Hash Change Listening`

Updates map generation when the `hash` parameter changes.

### `Conditional Generation Trigger`

Starts map generation only if `generate=true` (default) and a valid `hash` is provided.

## Usage

1. **Access URLs**: Open any provided URL in a browser to auto-generate a map.
2. **Encode Special Characters**: Replace spaces, symbols, or plus signs with URL-encoded equivalents (e.g., `%20`, `%2B`).
3. **Test Scenarios**: Use predefined URLs for quick verification of different `worldType` and `mapType` combinations.
4. **Automate Testing**: Script browser automation by iterating over test URLs (e.g., using Bash or Python).

## Dependencies

> `React (frontend framework)`
> `URL encoding/decoding libraries (e.g.`
> ``url-parse` or browser-native `URLSearchParams`)`
> `Map Generator component logic.`

## Related

- [[Map Generator Component Code]]
- [[URL Encoding Cheat Sheet]]
- [[Automated Testing Script Template]]

>[!INFO] **Deterministic Behavior**
> Providing the same `hash` and `worldType` will always produce the same map output, ensuring reproducibility across sessions.
>

>[!WARNING] **URL Encoding Pitfalls**
> Manually constructing URLs requires careful encoding of spaces and special characters. Use the provided examples or tools like [URL Encoder](https://www.urlencoder.org/) to avoid broken links.
