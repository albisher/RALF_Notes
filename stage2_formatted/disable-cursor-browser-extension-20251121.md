**Tags:** #browser-automation, #mcp-configuration, #cursor-ide, #tool-restrictions, #browser-extensions
**Created:** 2026-01-13
**Type:** documentation

# disable-cursor-browser-extension-20251121

## Summary

```
Configures Cursor IDE to disable cursor-browser-extension tools while enabling browsermcp and browser-tools via MCP server configurations.
```

## Details

> This file outlines modifications to restrict Cursor IDE’s browser automation tools to only allow `browsermcp` and `browser-tools` packages, explicitly blocking the `cursor-browser-extension` tools. Changes include updating JSON configuration files (`.mcp.json`, `.cursor/mcp.json`, `.cursor/settings.json`) and documentation (`.cursor/rules/browser-testing.mdc`) to enforce this restriction. The logic involves defining allowed and blocked MCP server tool namespaces in the settings file, ensuring only permitted tools are accessible in the Cursor IDE environment.

## Key Functions

### ``.mcp.json` (root)`

Configures MCP server for `browser-tools` and retains `browsermcp`.

### ``.cursor/mcp.json``

Enables `browsermcp` and `browser-tools` MCP servers in Cursor IDE context.

### ``.cursor/settings.json``

Defines `allowedTools` (e.g., `mcp_browsermcp_*` and `mcp_browser-tools_*`) and `blockedTools` (e.g., `mcp_cursor-browser-extension_*`).

### ``.cursor/rules/browser-testing.mdc``

Documents disabled tools and clarifies UI/UX agent restrictions.

## Usage

1. Apply changes to `.mcp.json`, `.cursor/mcp.json`, and `.cursor/settings.json`.
2. Restart Cursor IDE to apply MCP server updates.
3. Verify tool restrictions via documentation and IDE logs.

## Dependencies

> ``@modelcontextprotocol/server-browser-tools``
> `Cursor IDE core libraries`
> ``.cursor` directory structure.`

## Related

- [[Cursor IDE Configuration Guide]]
- [[Model Context Protocol (MCP) Docs]]

>[!INFO] Important Note
> Ensure `@modelcontextprotocol/server-browser-tools` matches the actual package name in Cursor’s environment. Adjust if needed.

>[!WARNING] Restart Requirement
> MCP server changes may require a Cursor IDE restart for full effect. Test after restarting.
