**Tags:** #UI/UX_Design, #AI_Prompting, #Accessibility, #Usability_Testing, #Browser_Tools, #Research_Based_Prompting
**Created:** 2026-01-13
**Type:** documentation

# UI_UX_AGENT_PROMPTING_GUIDE

## Summary

```
A research-backed guide for prompting a UI/UX agent to enhance expertise in usability, accessibility, and performance evaluation using restricted browser tools.
```

## Details

> This guide outlines structured techniques for optimizing a UI/UX agent’s performance by defining expert personas, applying structured evaluation frameworks (e.g., Nielsen’s heuristics, WCAG 2.1), and providing context-rich prompts. It restricts the agent to 26 predefined browser tools while emphasizing systematic task decomposition and self-assessment to improve accuracy and thoroughness. The document emphasizes usability, accessibility compliance, and adherence to design systems.

## Key Functions

### `Expert Persona Definition`

Assigns specialized roles (e.g., senior UI/UX expert) to guide evaluation criteria.

### `Structured Evaluation Frameworks`

Applies Nielsen’s 10 Usability Heuristics and WCAG 2.1 POUR principles for systematic assessment.

### `Context-Rich Prompting`

Integrates project-specific details (user personas, design systems, constraints) to tailor evaluations.

### `Task Decomposition`

Breaks evaluations into phases (e.g., navigation, form design, accessibility) for granular analysis.

### `Self-Assessment Mechanisms`

Encourages iterative review to identify gaps in findings.

## Usage

1. **Define Expert Role**: Craft prompts with specialized experience (e.g., 10+ years in UI/UX).
2. **Apply Frameworks**: Use structured templates for heuristics or WCAG compliance checks.
3. **Provide Context**: Include project details (user personas, design systems) to guide evaluations.
4. **Decompose Tasks**: Break evaluations into phases (e.g., navigation, accessibility) for precision.
5. **Self-Assess**: Request iterative reviews to refine findings.

## Dependencies

> ``mcp_browsermcp_*` (browser navigation`
> `interaction tools)`
> ``mcp_browser-tools_*` (audit`
> `logging`
> `and debugging tools)`
> `WCAG 2.1 guidelines`
> `Nielsen’s Usability Heuristics.`

## Related

- [[UX Evaluation Best Practices]]
- [[WCAG 2]]
- [[Nielsen’s Usability Heuristics Guide]]

>[!INFO] Critical Restriction
> The agent is **only allowed** to use 26 predefined browser tools (e.g., `mcp_browsermcp_browser_navigate`, `mcp_browser-tools_getConsoleLogs`). Violations risk disabling tool access.

>[!WARNING] Context Dependency
> Without project-specific context (e.g., user personas, design systems), evaluations may lack relevance or accuracy. Always provide exhaustive details.
