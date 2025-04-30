# Documentation MCP Server

A Model Context Protocol (MCP) server for accessing documentation across projects without duplicating files.

## Overview

Documentation MCP Server allows AI assistants to access documentation stored in a central repository. It exposes documentation files as MCP resources and provides tools for searching and navigating the documentation.

## Features

- **Documentation Resources**: Access documentation files through MCP resources
- **Search Functionality**: Search through documentation content
- **Navigation Tools**: Browse documentation structure
- **Markdown Conversion**: Convert various formats to markdown for LLM consumption
- **Cross-Project Access**: Reference documentation from any project without duplication

## Installation

### Using pip

```bash
pip install docs-mcp-server
```

### Using uv

```bash
uv add docs-mcp-server
```

## Usage

### Command Line Interface

Start the server with default settings:

```bash
docs-mcp-server
```

Specify a documentation directory:

```bash
docs-mcp-server --docs-dir /path/to/docs
```

Configure file extensions:

```bash
docs-mcp-server --extensions .md,.rst,.txt
```

Use SSE transport instead of stdio:

```bash
docs-mcp-server --transport sse --port 8000
```

### MCP Client Configuration

Add the server to your MCP client configuration:

#### Claude Desktop (`~/.claude/claude_desktop_config.json`)

```json
{
  "mcpServers": {
    "docs-mcp-server": {
      "command": "docs-mcp-server",
      "args": ["--docs-dir", "/path/to/docs"],
      "env": {
        "DOCS_MCP_LOG_LEVEL": "INFO"
      }
    }
  }
}
```

#### Cursor (`.cursor/mcp.json`)

```json
{
  "mcpServers": {
    "docs-mcp-server": {
      "command": "docs-mcp-server",
      "args": ["--docs-dir", "/path/to/docs"],
      "env": {
        "DOCS_MCP_LOG_LEVEL": "INFO"
      }
    }
  }
}
```

#### Using uvx

```json
{
  "mcpServers": {
    "docs-mcp-server": {
      "command": "uvx",
      "args": ["docs-mcp-server@latest", "--docs-dir", "/path/to/docs"],
      "env": {
        "DOCS_MCP_LOG_LEVEL": "INFO"
      }
    }
  }
}
```

## Available Resources

- `docs://list` - List all available documentation files
- `docs://toc` - Get a table of contents for all documentation
- `docs://{path}` - Get the content of a specific documentation file

## Available Tools

- `search_docs(query, max_results)` - Search documentation for the given query
- `get_doc_structure(path)` - Get the structure of documentation in the specified path
- `get_doc_info(path)` - Get metadata information about a specific documentation file

## Environment Variables

- `DOCS_MCP_BASE_DIR` - Base directory for documentation files (default: current directory)
- `DOCS_MCP_FILE_EXTENSIONS` - Comma-separated list of file extensions to include (default: .md,.txt,.html)
- `DOCS_MCP_RECURSIVE` - Whether to scan subdirectories recursively (default: true)
- `DOCS_MCP_LOG_LEVEL` - Logging level (default: INFO)
- `FASTMCP_TRANSPORT` - Transport protocol to use (default: stdio)
- `FASTMCP_PORT` - Port for SSE transport (default: 8000)

## Examples

### Searching Documentation

```
Using the docs-mcp-server, search for information about "installation"
```

### Accessing Specific Documentation

```
Using the docs-mcp-server, show me the documentation for the API reference
```

### Browsing Documentation Structure

```
Using the docs-mcp-server, show me the structure of the documentation
```

## License

MIT
