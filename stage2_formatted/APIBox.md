**Tags:** #HTTP, #API, #OOP, #Reusable, #Generic, #RequestHandler, #Async/Await, #ErrorHandling
**Created:** 2026-01-13
**Type:** code-notes

# APIBox

## Summary

```
A lightweight, reusable HTTP API communication utility for handling all HTTP requests with configurable defaults.
```

## Details

> `APIBox` is a class-based utility designed to abstract HTTP request logic, supporting GET, POST, and other HTTP methods. It enforces a single responsibility by managing all request lifecycle—including URL construction, request configuration, response parsing, and error handling—while maintaining flexibility via configurable defaults (e.g., base URL, timeout, headers). The class tracks request/error statistics (`requestCount`, `errorCount`) and delegates callbacks (`onSuccess`, `onError`) to external logic. It avoids local assumptions (e.g., works in Docker) and adheres to OOP principles.

## Key Functions

### `constructor(config)`

Initializes the APIBox with defaults (e.g., `baseURL`, `timeout`) and merges custom headers.

### `request(method, endpoint, options)`

Core method that orchestrates HTTP requests via `executeRequest` and `parseResponse`, with error handling and callback invocation.

### `get(endpoint, options)`

Convenience method for GET requests (delegates to `request`).

### `post(endpoint, data, options)`

Convenience method for POST requests (delegates to `request`).

### `buildURL(endpoint)`

Constructs the full API URL from `baseURL` + `endpoint`.

### `buildRequestConfig(method, options)`

Sets up request config (headers, timeout, signal) from defaults and overrides.

### `executeRequest(url, config)`

Abstracted HTTP request logic (likely uses `fetch` under the hood).

### `parseResponse(response)`

Extracts data from HTTP responses (e.g., JSON parsing).

### `createError(response, data)`

Formats error objects for non-2xx responses.

## Usage

```javascript
const apiBox = new APIBox({
    baseURL: 'https://api.example.com',
    timeout: 5000,
    headers: { 'Authorization': 'Bearer token' },
    onError: (err) => console.error('API Error:', err),
    onSuccess: (data) => console.log('Success:', data),
});

// Example GET request
apiBox.get('/users').then(data => console.log(data));

// Example POST request
apiBox.post('/users', { name: 'Alice' }).then(data => console.log(data));
```

## Dependencies

> ``fetch` (built-in browser API)`
> ``AbortSignal` (for request cancellation).`

## Related

- [[APIBox Usage Guide]]
- [[Fetch API Reference]]

>[!INFO] Default Timeout
> The default timeout (`30000ms`) can be overridden via `options.timeout` in `request()` or `post()`.

>[!WARNING] Error Handling
> Unhandled errors are rethrown after invoking `onError`. Ensure callbacks handle them gracefully to avoid silent failures.
