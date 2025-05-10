---
url: https://modelcontextprotocol.io/docs/tools/inspector
title: https://modelcontextprotocol.io/docs/tools/inspector
date: 2025-04-30T17:22:06.024841
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
Tutorials
Inspector
[User Guide](https://modelcontextprotocol.io/introduction)[SDKs](https://modelcontextprotocol.io/sdk/java/mcp-overview)[Specification](https://modelcontextprotocol.io/specification/2025-03-26)
[User Guide](https://modelcontextprotocol.io/introduction)[SDKs](https://modelcontextprotocol.io/sdk/java/mcp-overview)[Specification](https://modelcontextprotocol.io/specification/2025-03-26)
The [MCP Inspector](https://github.com/modelcontextprotocol/inspector) is an interactive developer tool for testing and debugging MCP servers. While the [Debugging Guide](https://modelcontextprotocol.io/docs/tools/debugging) covers the Inspector as part of the overall debugging toolkit, this document provides a detailed exploration of the Inspector’s features and capabilities.
## Getting started
### Installation and basic usage
The Inspector runs directly through `npx` without requiring installation:
Copy
```
npx @modelcontextprotocol/inspector <command>

```

Copy
```
npx @modelcontextprotocol/inspector <command> <arg1> <arg2>

```

#### Inspecting servers from NPM or PyPi
A common way to start server packages from [NPM](https://npmjs.com) or [PyPi](https://pypi.com).
  * NPM package
  * PyPi package


Copy
```
npx -y @modelcontextprotocol/inspector npx <package-name> <args>
# For example
npx -y @modelcontextprotocol/inspector npx server-postgres postgres://127.0.0.1/testdb

```

Copy
```
npx -y @modelcontextprotocol/inspector npx <package-name> <args>
# For example
npx -y @modelcontextprotocol/inspector npx server-postgres postgres://127.0.0.1/testdb

```

Copy
```
npx @modelcontextprotocol/inspector uvx <package-name> <args>
# For example
npx @modelcontextprotocol/inspector uvx mcp-server-git --repository ~/code/mcp/servers.git

```

#### Inspecting locally developed servers
To inspect servers locally developed or downloaded as a repository, the most common way is:
  * TypeScript
  * Python


Copy
```
npx @modelcontextprotocol/inspector node path/to/server/index.js args...

```

Copy
```
npx @modelcontextprotocol/inspector node path/to/server/index.js args...

```

Copy
```
npx @modelcontextprotocol/inspector \
 uv \
 --directory path/to/server \
 run \
 package-name \
 args...

```

Please carefully read any attached README for the most accurate instructions.
## Feature overview
The MCP Inspector interface
The Inspector provides several features for interacting with your MCP server:
### Server connection pane
  * Allows selecting the [transport](https://modelcontextprotocol.io/docs/concepts/transports) for connecting to the server
  * For local servers, supports customizing the command-line arguments and environment


### Resources tab
  * Lists all available resources
  * Shows resource metadata (MIME types, descriptions)
  * Allows resource content inspection
  * Supports subscription testing


### Prompts tab
  * Displays available prompt templates
  * Shows prompt arguments and descriptions
  * Enables prompt testing with custom arguments
  * Previews generated messages


### Tools tab
  * Lists available tools
  * Shows tool schemas and descriptions
  * Enables tool testing with custom inputs
  * Displays tool execution results


### Notifications pane
  * Presents all logs recorded from the server
  * Shows notifications received from the server


## Best practices
### Development workflow
  1. Start Development
     * Launch Inspector with your server
     * Verify basic connectivity
     * Check capability negotiation
  2. Iterative testing
     * Make server changes
     * Rebuild the server
     * Reconnect the Inspector
     * Test affected features
     * Monitor messages
  3. Test edge cases
     * Invalid inputs
     * Missing prompt arguments
     * Concurrent operations
     * Verify error handling and error responses


## Next steps
## [Inspector RepositoryCheck out the MCP Inspector source code](https://github.com/modelcontextprotocol/inspector)## [Debugging GuideLearn about broader debugging strategies](https://modelcontextprotocol.io/docs/tools/debugging)
Was this page helpful?
YesNo
[Debugging](https://modelcontextprotocol.io/docs/tools/debugging)[Core architecture](https://modelcontextprotocol.io/docs/concepts/architecture)
On this page
  * [Getting started](https://modelcontextprotocol.io/docs/tools/inspector#getting-started)
  * [Installation and basic usage](https://modelcontextprotocol.io/docs/tools/inspector#installation-and-basic-usage)
  * [Inspecting servers from NPM or PyPi](https://modelcontextprotocol.io/docs/tools/inspector#inspecting-servers-from-npm-or-pypi)
  * [Inspecting locally developed servers](https://modelcontextprotocol.io/docs/tools/inspector#inspecting-locally-developed-servers)
  * [Feature overview](https://modelcontextprotocol.io/docs/tools/inspector#feature-overview)
  * [Server connection pane](https://modelcontextprotocol.io/docs/tools/inspector#server-connection-pane)
  * [Resources tab](https://modelcontextprotocol.io/docs/tools/inspector#resources-tab)
  * [Notifications pane](https://modelcontextprotocol.io/docs/tools/inspector#notifications-pane)
  * [Best practices](https://modelcontextprotocol.io/docs/tools/inspector#best-practices)
  * [Development workflow](https://modelcontextprotocol.io/docs/tools/inspector#development-workflow)



