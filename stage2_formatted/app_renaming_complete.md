**Tags:** #branding, #localization, #arabic-language, #user-experience, #storytelling, #docker, #internationalization, #app-renaming
**Created:** 2026-01-13
**Type:** documentation

# app_renaming_complete

## Summary

```
Renames a creative writing application from a complex Arabic title to a concise, culturally resonant name ("ملاحم") with bilingual support.
```

## Details

> This document details the successful renaming of a web application from **"منشئ عالم اللؤلؤ الفضائي"** (Space Pearl World Builder) to **"ملاحم"** (Malahim), emphasizing simplicity, cultural relevance, and storytelling focus. The name change involved updating localization files, HTML titles, UI elements, and testing across Arabic and English modes. The new name leverages Arabic tradition for epic storytelling while ensuring technical compatibility and user accessibility.

## Key Functions

### ``frontend/src/locales/ar.json``

Stores Arabic translations for app title and subtitle.

### ``frontend/src/locales/en.json``

Stores English translations for the same elements.

### ``frontend/index.html``

Updated `<title>` tag to reflect the new name.

### ``docker-compose build frontend``

Rebuilds the frontend container post-renaming.

### ``docker-compose up -d frontend``

Restarts the frontend service for changes to take effect.

### ``App.vue``

Dynamically renders the app title using `{{ $t('app.title') }}` for localization.

## Usage

1. **Update Localization Files**: Modify `ar.json` and `en.json` with new translations.
2. **Rebuild Frontend**: Run `docker-compose build frontend` to apply changes.
3. **Restart Container**: Execute `docker-compose up -d frontend` to deploy updates.
4. **Test UI**: Verify UI updates (app bar, browser tab title) in both Arabic and English modes.

## Dependencies

> `Docker Compose`
> `frontend build tools (likely Vue.js or similar)`
> `Arabic/English localization libraries.`

## Related

- [[App Localization Strategy]]
- [[Arabic UI Design Guidelines]]
- [[Docker Deployment Best Practices]]

>[!INFO] Cultural Significance
> "ملاحم" (Malahim) is rooted in Arabic literary tradition, symbolizing epic storytelling—directly aligning with the app’s core function of world-building and creativity.

>[!WARNING] RTL Considerations
> Ensure RTL (right-to-left) support is maintained in UI components (e.g., text direction, dropdown menus) to avoid visual misalignment in Arabic mode.
