**Tags:** #data-formatting, #utility-library, #internationalization, #OOP, #static-methods
**Created:** 2026-01-13
**Type:** code-notes

# FormatterBox

## Summary

```
A reusable utility class for formatting numbers, currency, dates, and times with locale support.
```

## Details

> `FormatterBox` is a static utility class providing formatting capabilities for numbers, currency, percentages, dates, and times using the browser's `Intl` API. It follows a single-responsibility principle, focusing solely on data formatting. The class supports locale-specific formatting and handles edge cases like ISO date strings. Methods include `number()`, `currency()`, `percentage()`, `date()`, and `time()` for versatile formatting needs across applications like e-commerce, SaaS, and blogs.

## Key Functions

### ``number(num, decimals = 0, locale = 'en-US')``

Formats a number with locale-specific separators and decimal places.

### ``currency(amount, currency = 'USD', locale = 'en-US')``

Formats monetary values with currency symbols (e.g., USD, EUR).

### ``percentage(value, decimals = 1)``

Combines number formatting with a percentage suffix (e.g., "45.2%").

### ``date(date, format = 'short', locale = 'en-US')``

Formats dates in predefined styles (short/medium/long/full) or custom options.

### ``time(time, includeSeconds = false, locale = 'en-US')``

Formats time with optional seconds and locale support.

## Usage

```javascript
// Example 1: Format a number with locale
FormatterBox.number(1000000, 2, 'de-DE'); // Output: "1.000.000,00"

// Example 2: Format currency
FormatterBox.currency(100, 'EUR', 'en-US'); // Output: "€100.00"

// Example 3: Format percentage
FormatterBox.percentage(0.75); // Output: "75.0%"

// Example 4: Format date
FormatterBox.date(new Date(), 'medium'); // Output: "May 15, 2023"

// Example 5: Format time
FormatterBox.time(new Date(), true, 'en-US'); // Output: "10:30:45 PM"
```

## Dependencies

> ``Intl` (browser API)`
> `no external libraries required.`

## Related

- [[None]]

>[!INFO] Locale Support
> Use locale strings like `'en-US'`, `'de-DE'`, or `'fr-FR'` for culturally appropriate formatting. Defaults to `'en-US'` if unspecified.


>[!WARNING] Date Parsing
> Pass a `Date` object, string, or timestamp (e.g., `new Date()` or `"2023-01-01"`). Invalid inputs may default to the current date.
