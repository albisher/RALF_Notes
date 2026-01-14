**Tags:** #i18n-check, #puppeteer, #web-testing, #localization-test, #frontend-validation
**Created:** 2026-01-13
**Type:** code-test

# simple-i18n-check

## Summary

```
Automated i18n (internationalization) validation tool for web applications using Puppeteer.
```

## Details

> This script performs an automated check of an application's i18n implementation by:
> 1. Launching a browser instance to inspect the login page for visible text content
> 2. Extracting all text elements (headings, paragraphs, labels, etc.) and validating their presence
> 3. Verifying the existence of translation files (English and Arabic)
> 4. Checking the structure and completeness of translation keys in both files
> 5. Capturing screenshots of both successful and failed states for debugging
> 
> The tool specifically looks for common i18n elements like app names, login buttons, and username fields while validating the translation file structure.

## Key Functions

### `SimpleI18nCheck.runTest()`

Orchestrates the complete i18n verification process by:

### `SimpleI18nCheck constructor()`

Initializes the base URL and screenshot directory path

## Usage

1. Install dependencies: `npm install puppeteer fs path`
2. Configure the base URL in the constructor (currently set to localhost:8443)
3. Run the test: `const test = new SimpleI18nCheck(); test.runTest()`
4. Review screenshots in the `./screenshots/ui-checks` directory for visual verification
5. Check console logs for detailed validation results

## Dependencies

> `puppeteer`
> `fs`
> `path`

## Related

- [[i18n-translation-guidelines]]
- [[frontend-localization-standards]]

>[!INFO] Important Note
> This script specifically targets the login page for i18n validation. For comprehensive testing, you would need to extend it to check multiple pages and possibly implement more sophisticated text extraction logic.
>

>[!WARNING] Caution
> The script uses Chrome with disabled security features (`--ignore-web-security`). In production, you should:
> - Use a proper browser instance with security enabled
> - Implement proper error handling for file operations
> - Consider adding more specific validation rules beyond basic text presence checks
> - Validate against a consistent set of expected translations rather than just presence
