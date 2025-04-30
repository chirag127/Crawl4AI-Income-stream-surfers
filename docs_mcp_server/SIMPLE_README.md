# Simple Documentation MCP Server

This is a simplified version of the Documentation MCP Server that doesn't rely on complex package structure. It's designed to be easy to run and test.

## Features

- Access documentation files through MCP resources
- Search documentation content
- Get metadata about documentation files

## Usage

### Running the Server

```bash
# Set the documentation directory
export DOCS_MCP_BASE_DIR=/path/to/your/docs

# Run the server
python simple_server.py
```

Or use the provided script:

```bash
python run_simple_server.py
```

### MCP Client Configuration

#### Claude Desktop

Copy the `claude_desktop_config.json` file to your Claude Desktop configuration directory:

- Windows: `%APPDATA%\Claude\claude_desktop_config.json`
- macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`

Make sure to update the paths in the configuration file to match your system.

#### Cursor

Create a `.cursor/mcp.json` file in your project directory with the following content:

```json
{
  "mcpServers": {
    "docs-mcp-server": {
      "command": "python",
      "args": ["/path/to/simple_server.py"],
      "env": {
        "DOCS_MCP_BASE_DIR": "/path/to/your/docs"
      }
    }
  }
}
```

### Available Resources

- `docs://list` - List all available documentation files
- `docs://{path}` - Get the content of a specific documentation file

### Available Tools

- `search_documentation(query, max_results)` - Search documentation for the given query
- `get_doc_info(path)` - Get metadata information about a specific documentation file

## Examples

### Searching Documentation

```
Using the docs-mcp-server, search for information about "installation"
```

### Accessing Specific Documentation

```
Using the docs-mcp-server, show me the documentation for the API reference
```

## Troubleshooting

If you encounter issues:

1. Check that the documentation directory exists and contains markdown files
2. Verify that the paths in your configuration file are correct
3. Check the server logs for error messages
