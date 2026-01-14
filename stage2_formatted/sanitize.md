**Tags:** #Security, #DOM-Manipulation, #XSS-Protection, #Sanitization, #Frontend-Utilities
**Created:** 2026-01-13
**Type:** code-library

# sanitize

## Summary

```
A production-ready sanitization utility class for XSS protection in DOM manipulation, SVG handling, and input validation.
```

## Details

> This library provides static methods to sanitize HTML, SVG, user input, and URLs to prevent cross-site scripting (XSS) attacks. It uses DOM parsing and attribute whitelisting to ensure only safe elements and attributes are retained. The `sanitizeHTML` method leverages browser textContent escaping, while `sanitizeSVG` enforces strict element/attribute whitelisting. Additional methods handle DOM manipulation (e.g., `clearElement`, `appendSafe`) and input validation (e.g., `sanitizeInput`, `sanitizeURL`).

## Key Functions

### `sanitizeHTML(html)`

Escapes HTML content by parsing it into a temporary DOM container and returning sanitized innerHTML.

### `sanitizeSVG(svgString)`

Parses SVG strings into a DocumentFragment, recursively sanitizing elements/attributes against a whitelist of allowed tags/attributes.

### `clearElement(element)`

Removes all child nodes from an HTMLElement safely.

### `setTextContent(element, text)`

Sets text content on an element while escaping HTML.

### `appendSafe(container, content)`

Appends sanitized content (HTMLElement, DocumentFragment, or string) to a container.

### `sanitizeInput(input)`

Removes dangerous characters (e.g., `<>`, `javascript:`, event handlers) from user input.

### `sanitizeURL(url, allowedProtocols)`

Validates URLs against allowed protocols (defaults to `http:`/`https:`).

## Usage

```javascript
import { Sanitizer } from './sanitize.js';

// Sanitize HTML
const safeHtml = Sanitizer.sanitizeHTML('<script>alert("XSS")</script>');

// Sanitize SVG
const safeSvgFragment = Sanitizer.sanitizeSVG('<svg><script>alert()</script></svg>');

// Clear an element
Sanitizer.clearElement(document.getElementById('target'));

// Append sanitized content
Sanitizer.appendSafe(document.body, safeHtml);

// Sanitize user input
const safeInput = Sanitizer.sanitizeInput('<script>alert("XSS")</script>');

// Validate URL
const safeUrl = Sanitizer.sanitizeURL('http://example.com');
```

## Dependencies

> ``./logger.js` (custom logger utility for error logging)`

## Related

- [[Security Best Practices for Frontend Development]]
- [[DOM-Security-Guide]]

>[!INFO] Important Note
> **`sanitizeHTML` relies on browser textContent escaping**, which may not handle all edge cases (e.g., malformed HTML). For complex cases, consider a dedicated library like DOMPurify.


>[!WARNING] Caution
> **`sanitizeSVG` does not validate SVG structure**—malformed input may still cause errors. Always validate input before sanitizing.
