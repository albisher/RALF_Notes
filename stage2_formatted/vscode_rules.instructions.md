**Tags:** #documentation, #VSCode, #rules, #consistency, #markdown
**Created:** 2026-01-13
**Type:** documentation

# vscode_rules.instructions

## Summary

```
Guidelines for structuring VS Code rule documentation to enforce codebase consistency and effectiveness.
```

## Details

> This file outlines best practices for creating and maintaining VS Code rule documentation in Markdown format. It specifies required rule structure, file referencing conventions, and examples of correct/incorrect implementations. The document emphasizes practicality by referencing real codebase patterns and maintaining DRY principles.

## Key Functions

### `Required Rule Structure`

Defines mandatory Markdown fields (`description`, `globs`, `alwaysApply`) and formatting for rule content.

### `File References`

Explains syntax for linking files (`[filename](mdc:path)`) to improve navigation.

### `Code Examples`

Provides template for showing good/bad practices with language-specific syntax highlighting.

### `Rule Maintenance`

Lists practices for updating rules based on codebase evolution.

## Usage

1. Create `.instructions.md` files in `.github/instructions/` following the template.
2. Use `[filename](mdc:path)` for cross-referencing.
3. Include both `DO`/`✅` and `DON’T`/`❌` examples.
4. Reference existing code snippets when possible.

## Dependencies

> ``markdown``
> `VS Code extension APIs (for rule enforcement)`
> `Obsidian/MDC link syntax (for file references)`

## Related

- [[VSCode Extension Documentation]]
- [[Codebase Style Guide]]
- [[Markdown Syntax Guide]]

>[!INFO] Required Fields
> Mandatory sections (`description`, `globs`, `alwaysApply`) must be included in every rule file. Omitting them will break rule application.

>[!WARNING] DRY Compliance
> Avoid duplicating examples across rules. Reference existing rules (e.g., `prisma.instructions.md`) instead of repeating patterns.
