**Tags:** #UXTesting, #BugReport, #FrontendDevelopment, #TimelineUI, #CriticalFailure
**Created:** 2026-01-13
**Type:** documentation

# 20251121-timeline-comprehensive-test

## Summary

```
Comprehensive UI/UX test report detailing critical bugs in the timeline page’s event creation and settings save functionality, alongside layout and visual improvements.
```

## Details

> This report documents a UI/UX testing session for the timeline page, identifying critical bugs that block core functionality. The test highlights successful layout improvements (e.g., three-column distribution) and working top timeline visualization, while pinpointing failures in event creation (`createEvent` API mismatch) and settings persistence (fetch error). Visual issues like truncated headers are noted but not critical. The map viewer is expected to be incomplete. The report emphasizes immediate fixes for P0 issues before deployment.

## Key Functions

### `Event Creation`

Broken due to incorrect API operation name (`createEvent` vs `create`).

### `Timeline Settings Save`

Fails with "Failed to fetch" error, likely due to backend/API issues.

### `Top Timeline Visualization`

Passes with correct year markers and scroll functionality.

### `Layout Assessment`

Successfully improved three-column distribution (1.2:1.5:1.3 ratio).

### `Navigation Elements`

All workflow stages (Generate, Link, Card, Timeline, Story) are functional.

## Usage

To reproduce:
1. Access `http://localhost:5174/#timeline` in an automated browser (e.g., Browsermatic).
2. Test event creation by clicking "Add Event" and verify the error message.
3. Attempt saving timeline settings via the "Save Timeline Settings" button.
4. Check column headers for truncation (e.g., "Timel Events" vs "Timeline Events").

## Dependencies

> ``boxOrchestrator``
> ``Timeline API``
> ``Backend Timeline Service``
> ``Docker Map Viewer Service``
> ``CORS Configuration``
> ``Network Tab (DevTools)`.`

## Related

- [[20251121-timeline-frontend-code-review]]
- [[20251121-backend-timeline-api-log]]
- [[20251121-mapviewer-deployment-checklist.]]

>[!INFO] Critical Priority
> The `createEvent` API operation must be corrected to `'create'` immediately to restore event creation functionality. This is a P0 blocker.

>[!WARNING] Backend Dependency
> The "Failed to fetch" error in settings save suggests a backend/API issue. Verify the `Timeline` service is running and CORS is properly configured to avoid network failures.
