---
url: https://modelcontextprotocol.io/examples
title: https://modelcontextprotocol.io/examples
date: 2025-04-30T17:22:07.474560
depth: 1
---

[Model Context Protocol home page](https://modelcontextprotocol.io/)
Search...
Ctrl K
##### Get Started
  * Quickstart


##### Tutorials
  * [Building MCP with LLMs](https://modelcontextprotocol.io/tutorials/building-mcp-with-llms)


##### Concepts


##### Development


[Model Context Protocol home page](https://modelcontextprotocol.io/)
Search...
Ctrl K
Search...
Navigation
Get Started
Example Servers
[User Guide](https://modelcontextprotocol.io/introduction)[SDKs](https://modelcontextprotocol.io/sdk/java/mcp-overview)[Specification](https://modelcontextprotocol.io/specification/2025-03-26)
[User Guide](https://modelcontextprotocol.io/introduction)[SDKs](https://modelcontextprotocol.io/sdk/java/mcp-overview)[Specification](https://modelcontextprotocol.io/specification/2025-03-26)
This page showcases various Model Context Protocol (MCP) servers that demonstrate the protocol’s capabilities and versatility. These servers enable Large Language Models (LLMs) to securely access tools and data sources.
## Reference implementations
These official reference servers demonstrate core MCP features and SDK usage:
### Data and file systems
  * - Secure file operations with configurable access controls
  * - Read-only database access with schema inspection capabilities
  * - Database interaction and business intelligence features
  * - File access and search capabilities for Google Drive


### Development tools
  * - Tools to read, search, and manipulate Git repositories
  * - Repository management, file operations, and GitHub API integration
  * - GitLab API integration enabling project management
  * - Retrieving and analyzing issues from Sentry.io


### Web and browser automation
  * - Web and local search using Brave’s Search API
  * - Web content fetching and conversion optimized for LLM usage
  * - Browser automation and web scraping capabilities


### Productivity and communication
  * - Channel management and messaging capabilities
  * - Location services, directions, and place details
  * - Knowledge graph-based persistent memory system


### AI and specialized tools
  * - AI image generation using various models
  * - Dynamic problem-solving through thought sequences
  * - Retrieval from AWS Knowledge Base using Bedrock Agent Runtime


## Official integrations
These MCP servers are maintained by companies for their platforms:
  * - Query and analyze logs, traces, and event data using natural language
  * - Automate browser interactions in the cloud
  * - Deploy and manage resources on the Cloudflare developer platform
  * - Execute code in secure cloud sandboxes
  * - Interact with the Neon serverless Postgres platform
  * **[Obsidian Markdown Notes](https://github.com/calclavia/mcp-obsidian)** - Read and search through Markdown notes in Obsidian vaults
  * - Manage and interact with Prisma Postgres databases
  * - Implement semantic memory using the Qdrant vector search engine
  * - Access crash reporting and monitoring data
  * - Unified API for search, crawling, and sitemaps
  * - Interact with the Stripe API
  * - Interface with the Tinybird serverless ClickHouse platform
  * - Enable Agentic RAG through your Weaviate collection(s)


## Community highlights
A growing ecosystem of community-developed servers extends MCP’s capabilities:
  * - Manage containers, images, volumes, and networks
  * - Manage pods, deployments, and services
  * - Project management and issue tracking
  * - Interact with Snowflake databases
  * - Control Spotify playback and manage playlists
  * - Task management integration


> **Note:** Community servers are untested and should be used at your own risk. They are not affiliated with or endorsed by Anthropic.
For a complete list of community servers, visit the [MCP Servers Repository](https://github.com/modelcontextprotocol/servers).
## Getting started
### Using reference servers
TypeScript-based servers can be used directly with `npx`:
Copy
```
npx -y @modelcontextprotocol/server-memory

```

Python-based servers can be used with `uvx` (recommended) or `pip`:
Copy
```
# Using uvx
uvx mcp-server-git
# Using pip
pip install mcp-server-git
python -m mcp_server_git

```

### Configuring with Claude
To use an MCP server with Claude, add it to your configuration:
Copy
```

 "mcpServers": {
  "memory": {
   "command": "npx",
   "args": ["-y", "@modelcontextprotocol/server-memory"]

  "filesystem": {
   "command": "npx",
   "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/allowed/files"]

  "github": {
   "command": "npx",
   "args": ["-y", "@modelcontextprotocol/server-github"],
   "env": {
    "GITHUB_PERSONAL_ACCESS_TOKEN": "<YOUR_TOKEN>"





```

## Additional resources
  * [MCP Servers Repository](https://github.com/modelcontextprotocol/servers) - Complete collection of reference implementations and community servers
  * [Awesome MCP Servers](https://github.com/punkpeye/awesome-mcp-servers) - Curated list of MCP servers
  * [MCP CLI](https://github.com/wong2/mcp-cli) - Command-line inspector for testing MCP servers
  * [MCP Get](https://mcp-get.com) - Tool for installing and managing MCP servers
  * [Pipedream MCP](https://mcp.pipedream.com) - MCP servers with built-in auth for 3,000+ APIs and 10,000+ tools
  * [Supergateway](https://github.com/supercorp-ai/supergateway) - Run MCP stdio servers over SSE
  * [Zapier MCP](https://zapier.com/mcp) - MCP Server with over 7,000+ apps and 30,000+ actions


Visit our [GitHub Discussions](https://github.com/orgs/modelcontextprotocol/discussions) to engage with the MCP community.
Was this page helpful?
YesNo
[For Claude Desktop Users](https://modelcontextprotocol.io/quickstart/user)[Example Clients](https://modelcontextprotocol.io/clients)
On this page
  * [Reference implementations](https://modelcontextprotocol.io/examples#reference-implementations)
  * [Data and file systems](https://modelcontextprotocol.io/examples#data-and-file-systems)
  * [Development tools](https://modelcontextprotocol.io/examples#development-tools)
  * [Web and browser automation](https://modelcontextprotocol.io/examples#web-and-browser-automation)
  * [Productivity and communication](https://modelcontextprotocol.io/examples#productivity-and-communication)
  * [AI and specialized tools](https://modelcontextprotocol.io/examples#ai-and-specialized-tools)
  * [Official integrations](https://modelcontextprotocol.io/examples#official-integrations)
  * [Community highlights](https://modelcontextprotocol.io/examples#community-highlights)
  * [Getting started](https://modelcontextprotocol.io/examples#getting-started)
  * [Using reference servers](https://modelcontextprotocol.io/examples#using-reference-servers)
  * [Configuring with Claude](https://modelcontextprotocol.io/examples#configuring-with-claude)
  * [Additional resources](https://modelcontextprotocol.io/examples#additional-resources)



