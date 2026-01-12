**Tags:** #docker, #api-key, #perplexity, #cursor-mcp, #issue-resolution, #mcp-server, #ai-integration, #research-tools, #configuration
**Created:** 2026-01-12
**Type:** documentation

# perplexity-mcp-setup

## Summary

```
Documentation outlining the setup and troubleshooting for integrating the Perplexity MCP server into Cursor, focusing on resolving missing server availability and API key configuration.
```

## Details

> This document details the steps to resolve the Perplexity MCP server unavailability despite the Docker image existing. The root cause was the server not being added to Cursor’s MCP registry and the absence of an API key. The solution involved adding the MCP server via `mcp-find` and `mcp-add`, followed by configuring the API key via environment variables or Cursor settings. Three tools (`perplexity_ask`, `perplexity_reason`, `perplexity_research`) became available post-configuration, enabling research and reasoning functionalities.

## Key Functions

### ``mcp-find``

Locates the Perplexity Docker image in the MCP catalog.

### ``mcp-add``

Adds the Perplexity MCP server to Cursor with activation enabled.

### ``mcp-config-set``

Configures the Perplexity API key in Cursor settings.

### ``export PERPLEXITY_API_KEY``

Sets the API key via environment variables.

## Usage

1. **Verify Docker Image**: Ensure `mcp/perplexity-ask:latest` exists (`docker images`).
2. **Add MCP Server**: Use `mcp-find` and `mcp-add` to register the server in Cursor.
3. **Configure API Key**:
   - Generate a key at [Perplexity API Settings](https://www.perplexity.ai/).
   - Set via `mcp-config-set` or environment variable (`export PERPLEXITY_API_KEY="key"`).
4. **Test Integration**: Use tools like `perplexity_ask` to search/research (e.g., `perplexity_ask(messages=[...])`).

## Dependencies

> `- Perplexity API (API key required for functionality)
- Cursor MCP registry (for server management)
- Docker (for image existence verification)`

## Related

- [[00-research-methodology]]
- [[01-simulation-videos]]
- [[10-simulator-videos-reviews]]

>[!INFO] Important Note
> The Perplexity MCP server tools (`perplexity_ask`, `perplexity_reason`, `perplexity_research`) require a valid API key for full functionality. Without it, they will return errors or limited responses.


>[!WARNING] Caution
> Do not expose the `PERPLEXITY_API_KEY` in plaintext in scripts or environment files. Use secure methods (e.g., Cursor’s built-in key management) to avoid unauthorized access.
