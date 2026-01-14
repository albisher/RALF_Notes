**Tags:** #test-automation, #api-integration, #character-generation, #unit-testing
**Created:** 2026-01-13
**Type:** code-notes

# character-api-test

## Summary

```
Automated test suite for a character API, validating login, generation, and structure of generated elements.
```

## Details

> This script performs an end-to-end test of a character API by:
> 1. Authenticating via login to obtain an access token
> 2. Generating a character with a predefined seed and verifying its structure (identity, attributes, history, skills, status, visuals)
> 3. Comparing character formatting with robot generator output
> 4. Validating all supported generators (plant, building, robot, character) produce consistent responses
> 
> The test uses Axios for HTTP requests and a helper class to log structured test results with pass/fail statuses.

## Key Functions

### ``runCharacterAPITest()``

Orchestrates the entire test workflow.

### ``CheckHelper.addResult()``

Records test outcomes with metadata (status, message, details).

### ``axios.post()``

Handles all API calls with token-based authentication and SSL verification bypass.

## Usage

1. Install dependencies (`npm install axios chalk`)
2. Run script (`node character-api-test.js`)
3. Verify console output shows pass/fail results for each test phase

## Dependencies

> `axios`
> `chalk`
> `config (local)`
> `utils/check-helper`
> `https (node built-in)`

## Related

- [[Character API Documentation]]
- [[Worlds API Reference]]
- [[Test Framework Setup]]

>[!INFO] Important Note
> The script uses a hardcoded email/password for login and bypasses SSL certificate validation (`rejectUnauthorized: false`). In production, use proper authentication and validate certificates.
>

>[!WARNING] Caution
> Test seeds (`test-character-api-123`) are predictable and may produce identical results across runs. Consider using random seeds for more reliable testing.
