**Tags:** #API-Validation, #Health-Check, #Database-Verification, #Dependency-Testing
**Created:** 2026-01-13
**Type:** code-notes

# api-check

## Summary

```
Validates API endpoints for health, users, worlds, generators, and performs element generation tests.
```

## Details

> This script performs automated API checks using `axios` and `chalk` for logging. It validates:
> 1. **Health Check** – Ensures the API responds with expected status fields (`status`, `database`, `generators_available`, `version`).
> 2. **Users/Worlds API** – Verifies successful responses and checks if data arrays (`users`, `worlds`) exist and contain elements.
> 3. **Generators API** – Confirms available generator types (`plant`, `building`, `robot`, `character`) against expected list.
> 4. **Element Generation** – Tests a POST endpoint to generate a test element (e.g., a desert biome element) and validates its structure (e.g., `id`, `name`, `element_type`).
> 
> The script uses a helper (`CheckHelper`) to log results with statuses (`pass`, `fail`, `warning`) and structured data.

## Key Functions

### ``runAPIChecks()``

Orchestrates all API validation steps.

### ``CheckHelper.addResult()``

Logs check outcomes (e.g., `Health Endpoint`, `Users Data Structure`).

### ``helper.checkApiEndpoint()``

Executes HTTP requests and returns success/error statuses.

### ``https.Agent` (inlined)`

Bypasses SSL verification for testing (critical for insecure endpoints).

## Usage

1. Require dependencies and initialize `CheckHelper`.
2. Call `runAPIChecks()` to execute all checks.
3. Review `helper.addResult()` logs for pass/fail warnings.
4. Modify `config.urls` and `config.testData` for custom endpoints/seed values.

## Dependencies

> ``axios``
> ``chalk``
> ``config` (local)`
> ``check-helper` (local)`
> ``https` (Node.js built-in).`

## Related

- [[API-Configuration-File]]
- [[Test-Data-Schema]]

>[!INFO] Critical Dependency
> The script uses `https.Agent({ rejectUnauthorized: false })`, which disables SSL validation. Use only in trusted environments or with explicit caution.

>[!WARNING] Race Condition Risk
> Element generation depends on `worldsCheck.success`, which may fail if earlier checks (e.g., health) fail. Add retry logic for transient failures.
