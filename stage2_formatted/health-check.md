**Tags:** #health-check, #monitoring, #api-testing, #frontend-validation, #database-check, #puppeteer, #ssl-validation
**Created:** 2026-01-13
**Type:** code-notes

# health-check

## Summary

```
Automated health checks for application components, including API, frontend, and database connectivity.
```

## Details

> This script performs a multi-stage health check for an application using Puppeteer for frontend validation and other libraries for API/database checks. It logs results with statuses (pass/fail/warning) and captures screenshots for documentation. The checks include:
> - API endpoint responsiveness (with SSL validation).
> - Database connection status.
> - Frontend accessibility, title correctness, and navigation elements.
> - Console error detection.
> - SSL certificate validation.

## Key Functions

### ``runHealthChecks()``

Orchestrates all health checks sequentially.

### ``CheckHelper` (from `./utils/check-helper`)`

Handles individual check logic (e.g., `checkServiceHealth`, `checkPageTitle`, `elementExists`).

### ``puppeteer.launch()``

Launches a browser instance for frontend checks.

### ``helper.addResult()``

Records check outcomes with statuses and metadata.

## Usage

1. Require dependencies and initialize `config` (e.g., URLs, timeouts).
2. Call `runHealthChecks()` to execute all checks.
3. Review `helper.addResult()` outputs for pass/fail/warning statuses.

## Dependencies

> `puppeteer`
> `chalk`
> `config (local)`
> `utils/check-helper (local)`
> `Node.js core modules (e.g.`
> ``https`).`

## Related

- [[health-check-config]]
- [[check-helper-module]]

>[!INFO] Important Note
> The script assumes `config` contains structured data like `urls.health`, `urls.frontend`, and `expected.elements`. Validate config before execution.

>[!WARNING] Caution
> Self-signed SSL certificates may cause API checks to fail. Ensure proper certificate validation in production.
