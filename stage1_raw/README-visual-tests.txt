### TAGS
#visual-testing
#automated-testing
#webapp
#puppeteer
#ui-testing
#web-development

### TYPE
documentation

### SUMMARY
A comprehensive visual testing framework for verifying UI consistency and functionality in a Space Pearl web application using Puppeteer.

### DETAILS
This `README-visual-tests` file outlines a Puppeteer-based visual testing suite designed to automate UI verification across multiple webapp components. The suite captures screenshots at each step, ensuring visual consistency and functional correctness for authentication, core pages, world-building features, and responsive design. It includes configuration options for browser settings, credentials, and execution modes (interactive/headless).

The suite runs tests against a local webapp instance, recording detailed reports (JSON, console output, screenshots) to document test results and failures. It supports CI/CD integration via GitHub Actions and provides troubleshooting guidance for common issues like authentication failures or missing webapp services.

### KEY_FUNCTIONS
- **`VisualTestSuite` class**: Core test runner that orchestrates all visual checks using Puppeteer.
- **`testAuthentication()`**: Validates login functionality, protected routes, and error handling.
- **`testCorePages()`**: Verifies dashboard, map, globe, character, and element pages load correctly.
- **`testWorldBuildingFeatures()`**: Tests world creation forms, element generation, and character management.
- **`testResponsiveDesign()`**: Ensures UI renders properly across desktop, tablet, and mobile viewports.
- **`testErrorHandling()`**: Checks 404 pages, API errors, and network failures.
- **`testSystemHealth()`**: Validates API endpoints, database connectivity, and service availability.
- **`setup-visual-tests.sh`**: Script to initialize test environment (permissions, dependencies).
- **`test-report.json`**: Structured JSON output summarizing test results (pass/fail counts, timestamps).

### DEPENDENCIES
Puppeteer, npm (for package management), Docker (for webapp container), Node.js (runtime environment).

### USAGE
1. **Setup**: Run `chmod +x setup-visual-tests.sh` and execute it to install dependencies.
2. **Run Tests**: Use `npm test` (interactive) or `npm run test:headless` (CI/CD optimized).
3. **Customize**:
   - Update `baseUrl` in `visual-test-suite.js` for different environments.
   - Modify credentials in `testAuthentication()` for testing different users.
   - Add new test methods to `VisualTestSuite` for custom UI checks.
4. **Review Results**: Check `test-screenshots/` for visual evidence and `test-report.json` for structured results.

### RELATED
[[Space Pearl WebApp Documentation]], [[Puppeteer API Reference]], [[CI/CD Pipeline for Web Apps]]

### CALLOUTS
>[!INFO]- **Interactive Mode**
> Run `npm test` to see browser windows for visual inspection. Screenshots are saved automatically to `test-screenshots/`.
>
>[!WARNING]- **Authentication Dependency**
> Ensure the test user (`testuser/testpass`) exists in the database and authentication endpoints are functional. If credentials fail, verify the webapp’s login flow and database schema.
>
>[!INFO]- **Headless Mode**
> For CI/CD, use `npm run test:headless` to reduce resource usage. Screenshots still capture visual results but without browser windows.