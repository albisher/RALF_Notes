**Tags:** #UI/UX, #BrowserAutomation, #AgencyWorkflow, #DevelopmentGuidelines, #TestingProcess
**Created:** 2026-01-13
**Type:** documentation

# clarification-uiux-vs-general-dev

## Summary

```
Clarifies the distinction between UI/UX Agent mode (browser automation enabled) and General Development mode (browser automation restricted) for a project toolset.
```

## Details

> This document addresses a miscommunication regarding browser automation tool usage, distinguishing between two operational modes: **UI/UX Agent Mode**, designed for automated UI/UX testing, and **General Development Mode**, intended for code editing and manual testing. The original rule incorrectly banned browser automation entirely, but the fix introduces exceptions for UI/UX Agent Mode while maintaining restrictions for General Development. Updated documentation includes rules, decision trees, and examples to guide when each mode should be used, emphasizing the need for explicit user requests to switch modes.

## Key Functions

### ``.cursor/rules/browser-testing.mdc``

Defines browser automation exceptions for UI/UX Agent Mode.

### ``.cursor/rules/project_ui_check.mdc``

Differentiates tool usage between UI/UX Agent and General Dev modes.

### ``docs/when-to-use-uiux-agent.md``

Provides a comprehensive guide on when to activate each mode, including decision trees and examples.

### `UI/UX Agent Role`

Automated UI/UX testing with tools like `browsermcp` and `browser-tools`.

### `General Development Role`

Code editing, static analysis, and manual testing instructions.

## Usage

1. **For Development Tasks**: Use General Development Mode to edit code, provide manual test instructions, and avoid browser automation unless explicitly requested.
2. **For UI/UX Testing**: Switch to UI/UX Agent Mode when users request automated UI/UX testing, navigation, audits, or reports.
3. **Hybrid Workflows**: Alternate between modes—e.g., fix code in General Dev, then switch to UI/UX Agent for automated verification.

## Dependencies

> ``.cursor``
> ``browsermcp``
> ``browser-tools``
> `Obsidian/Markdown for documentation.`

## Related

- [[browser-testing]]
- [[project_ui_check]]
- [[UI_UX_AGENT]]
- [[when-to-use-uiux-agent]]

>[!INFO] Critical Clarification
> UI/UX Agent Mode is explicitly designed for **automated UI/UX testing**—browsermcp and browser-tools are its primary tools. General Development Mode should **never** use these tools unless explicitly requested by the user.


>[!WARNING] Common Mistake
> Automatically assuming a user wants automated testing without asking can lead to incorrect tool usage. Always prompt the user to clarify their intent before switching modes.
