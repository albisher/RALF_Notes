**Tags:** #UI/UX, #Automation, #Testing, #BrowserAutomation, #AgencyRoles, #DevelopmentWorkflow
**Created:** 2026-01-13
**Type:** documentation

# when-to-use-uiux-agent

## Summary

```
Explains when to use a specialized UI/UX agent versus general development mode for testing and code changes.
```

## Details

> This document outlines two distinct operational modes for handling UI/UX and development tasks. The **UI/UX Agent Mode** focuses on comprehensive browser automation for testing UI/UX elements, including navigation, accessibility, performance, and visual consistency, while **General Development Mode** handles code editing, manual testing, and iterative improvements. The document provides a decision tree for selecting the appropriate mode based on user requests, examples of workflows, and key differences between the two approaches.

## Key Functions

### `UI/UX Agent Mode`

Performs automated UI/UX testing using browser automation tools like `browsermcp` and `browser-tools`, generating detailed reports and screenshots.

### `General Development Mode`

Enables code editing, manual testing instructions, and iterative development with tools like file editing, terminal commands, and code analysis.

### `Decision Tree`

Guides users in choosing between modes based on specific user requests (e.g., "Run UI/UX tests" vs. "Fix the layout").

### `Hybrid Approach`

Proposes a workflow combining both modes for development, verification, and final checks.

## Usage

1. **Identify User Request**: Determine if the task involves UI/UX testing (e.g., "Accessibility audit") or development (e.g., "Fix the layout").
2. **Select Mode**: Use **UI/UX Agent Mode** for automated testing and audits; use **General Development Mode** for code changes and manual testing.
3. **Follow Workflow**: Implement a hybrid approach—develop in General Mode, verify with UI/UX Agent, and iterate as needed.

## Dependencies

> ``browsermcp``
> ``browser-tools``
> `Vue/CSS/JS files`
> `Obsidian wikilinks for related documentation (e.g.`
> ``UI_UX_AGENT.md`).`

## Related

- [[UI_UX_AGENT]]
- [[[Documentation on Browser Automation Tools]]]

>[!INFO] **Critical Distinction**
> UI/UX Agent Mode **cannot** edit code or execute terminal commands—it strictly automates browser interactions for testing. Always use General Development Mode for code changes.


>[!WARNING] **Avoid Overlap**
> Mixing modes incorrectly (e.g., using UI/UX Agent for code fixes) leads to inefficiency. Stick to the designated tools for each phase to maintain accuracy and reliability.
