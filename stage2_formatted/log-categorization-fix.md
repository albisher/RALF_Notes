**Tags:** #log-management, #frontend-logging, #view-operations, #system-monitoring, #javascript, #ui-categorization
**Created:** 2026-01-13
**Type:** code-notes

# log-categorization-fix

## Summary

```
Fixes misplaced log categorization for plot-related operations to ensure they appear in the correct "View(s) logs" panel.
```

## Details

> This fix addresses incorrect log placement where `Plot3DBox` and `Plot2DBox` logs were incorrectly routed to "System Logs" instead of "View(s) logs." The solution involves updating log types in `plot-3d-box.js` and `plot-2d-box.js` to use `view_operation` instead of `plotly_command`, adding action metadata for clarity, and modifying the `system-monitoring-page-component.js` to filter logs by `view_operation` type and source (`plot3dbox`, `plot2dbox`). This ensures proper separation between view-related and system logs, improving log panel organization.

## Key Functions

### ``simulation/frontend/boxes/plot-3d-box.js``

Modified log type from `plotly_command` to `view_operation` with action metadata.

### ``simulation/frontend/boxes/plot-2d-box.js``

Updated log type similarly to ensure consistency.

### ``simulation/frontend/pages/system-monitoring-page-component.js``

Added filters for `view_operation` logs and excluded `plotly_command` variants from system logs.

## Usage

To apply this fix:
1. Update `plot-3d-box.js` and `plot-2d-box.js` to use `view_operation` log types with action metadata.
2. Modify `system-monitoring-page-component.js` to include the new filter logic for `view_operation` logs and exclude old `plotly_command` variants.
3. Test log panel categorization to confirm logs appear in the correct panel.

## Dependencies

> ``simulation/frontend/boxes/plot-3d-box.js``
> ``simulation/frontend/boxes/plot-2d-box.js``
> ``simulation/frontend/pages/system-monitoring-page-component.js``

## Related

- [[logging-system]]
- [[frontend-ui-components]]

>[!INFO] Important Note
> The updated `view_operation` logs will now appear in the "View(s) logs" panel, improving usability by separating them from system logs.
>

>[!WARNING] Caution
> Ensure backward compatibility if other components rely on `plotly_command` logs. The exclusion of these logs from view operations may require additional checks in dependent systems.
