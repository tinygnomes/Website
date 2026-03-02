# Local Figma MCP Server

This tool (`tools/figma-mcp.py`) is a standalone Model Context Protocol (MCP) server written in Python. It provides the AI assistant with direct access to the TinyGnomes Figma design file via the Figma REST API.

## Requirements Introspection

The script leverages `uv`'s inline script metadata to run without needing a managed virtual environment:
```python
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "mcp",
#     "requests"
# ]
# ///
```

## Running the Server

The server is intended to be run by the AI assistant (or an MCP-compatible editor) using the Justfile, which automatically injects the necessary environment variables (`FIGMA_FILE_ID` and `FIGMA_ACCESS_TOKEN`) from the `.env` file:
```bash
just serve-figma
```

## IDE / MCP Configuration

If you are setting this up in an AI-powered IDE (like Claude Desktop, Cursor, or similar tools that use an `mcp_config.json` file), you should configure the tool to execute the `just` command from within the TinyGnomes directory so it automatically picks up the `.env` file credentials. Here is the recommended configuration snippet:

```json
{
  "mcpServers": {
    "figma-mcp": {
      "command": "bash",
      "args": [
        "-c",
        "cd /path/to/TinyGnomes && just serve-figma"
      ]
    }
  }
}
```

## Capabilities Provided to AI

By connecting to this server, the AI assistant gains the following discrete tools:

### `list_figma_hierarchy(root_node_id=None, depth=2)`
Traverses the document and prints a clean tree of names and Node IDs. This is the critical first step for the AI to discover the ID of a specific page, frame, or component it needs to inspect.

### `get_figma_styles()`
Hits the `styles` endpoints to output a list of your local published colors, typography tokens, and effects (shadows), mapping their properties into a clean dictionary. The AI uses this to maintain `website/css/style.css`.

### `get_node_details(node_names_or_ids)`
Allows the AI to pass specific Node IDs (found via the hierarchy tool) and retrieves their core parameters: `absoluteBoundingBox`, padding, gap, background fills, and local children objects. Used heavily for extracting exact CSS positions for complex overlapping graphics.

### `export_figma_asset(node_id, format)`
Takes a specific Node ID (e.g. an icon or illustration) and a format (`svg`, `png`, `jpg`). It issues an export request to Figma, parses the returning temporary download URL, fetches the binary file, and writes it directly to the `website/images` or custom specified directory.
