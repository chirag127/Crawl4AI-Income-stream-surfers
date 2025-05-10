---
url: https://modelcontextprotocol.io/specification/2024-11-05/client/roots
title: https://modelcontextprotocol.io/specification/2024-11-05/client/roots
date: 2025-04-30T17:22:26.069021
depth: 2
---

[Model Context Protocol home page](https://modelcontextprotocol.io/)
Search...
Ctrl K
##### 2025-03-26 (Latest)
  * Base Protocol
  * Client Features
  * Server Features


##### 2024-11-05
  * Base Protocol
  * Client Features
  * Server Features


##### draft
  * Base Protocol
  * Client Features
  * Server Features


##### Resources


[Model Context Protocol home page](https://modelcontextprotocol.io/)
Search...
Ctrl K
Search...
Navigation
Client Features
Roots
[User Guide](https://modelcontextprotocol.io/introduction)[SDKs](https://modelcontextprotocol.io/sdk/java/mcp-overview)[Specification](https://modelcontextprotocol.io/specification/2025-03-26)
[User Guide](https://modelcontextprotocol.io/introduction)[SDKs](https://modelcontextprotocol.io/sdk/java/mcp-overview)[Specification](https://modelcontextprotocol.io/specification/2025-03-26)
**Protocol Revision** : 2024-11-05
The Model Context Protocol (MCP) provides a standardized way for clients to expose filesystem “roots” to servers. Roots define the boundaries of where servers can operate within the filesystem, allowing them to understand which directories and files they have access to. Servers can request the list of roots from supporting clients and receive notifications when that list changes.
## User Interaction Model
Roots in MCP are typically exposed through workspace or project configuration interfaces.
For example, implementations could offer a workspace/project picker that allows users to select directories and files the server should have access to. This can be combined with automatic workspace detection from version control systems or project files.
However, implementations are free to expose roots through any interface pattern that suits their needs—the protocol itself does not mandate any specific user interaction model.
## Capabilities
Clients that support roots **MUST** declare the `roots` capability during [initialization](https://modelcontextprotocol.io/specification/2024-11-05/basic/lifecycle#initialization):
Copy
```

 "capabilities": {
  "roots": {
   "listChanged": true




```

`listChanged` indicates whether the client will emit notifications when the list of roots changes.
## Protocol Messages
### Listing Roots
To retrieve roots, servers send a `roots/list` request:
**Request:**
Copy
```

 "jsonrpc": "2.0",
 "id": 1,
 "method": "roots/list"


```

**Response:**
Copy
```

 "jsonrpc": "2.0",
 "id": 1,
 "result": {
  "roots": [

    "uri": "file:///home/user/projects/myproject",
    "name": "My Project"





```

### Root List Changes
When roots change, clients that support `listChanged` **MUST** send a notification:
Copy
```

 "jsonrpc": "2.0",
 "method": "notifications/roots/list_changed"


```

## Message Flow
ClientServerClientServerDiscoveryChangesroots/listAvailable rootsnotifications/roots/list_changedroots/listUpdated roots
## Data Types
### Root
A root definition includes:
  * `uri`: Unique identifier for the root. This **MUST** be a `file://` URI in the current specification.
  * `name`: Optional human-readable name for display purposes.


Example roots for different use cases:
#### Project Directory
Copy
```

 "uri": "file:///home/user/projects/myproject",
 "name": "My Project"


```

#### Multiple Repositories
Copy
```


  "uri": "file:///home/user/repos/frontend",
  "name": "Frontend Repository"


  "uri": "file:///home/user/repos/backend",
  "name": "Backend Repository"



```

## Error Handling
Clients **SHOULD** return standard JSON-RPC errors for common failure cases:
  * Client does not support roots: `-32601` (Method not found)
  * Internal errors: `-32603`


Example error:
Copy
```

 "jsonrpc": "2.0",
 "id": 1,
 "error": {
  "code": -32601,
  "message": "Roots not supported",
  "data": {
   "reason": "Client does not have roots capability"




```

## Security Considerations
  1. Clients **MUST** :
     * Only expose roots with appropriate permissions
     * Validate all root URIs to prevent path traversal
     * Implement proper access controls
     * Monitor root accessibility
  2. Servers **SHOULD** :
     * Handle cases where roots become unavailable
     * Respect root boundaries during operations
     * Validate all paths against provided roots


## Implementation Guidelines
  1. Clients **SHOULD** :
     * Prompt users for consent before exposing roots to servers
     * Provide clear user interfaces for root management
     * Validate root accessibility before exposing
     * Monitor for root changes
  2. Servers **SHOULD** :
     * Check for roots capability before usage
     * Handle root list changes gracefully
     * Respect root boundaries in operations
     * Cache root information appropriately


Was this page helpful?
YesNo
On this page
  * [User Interaction Model](https://modelcontextprotocol.io/specification/2024-11-05/client/roots#user-interaction-model)
  * [Protocol Messages](https://modelcontextprotocol.io/specification/2024-11-05/client/roots#protocol-messages)
  * [Listing Roots](https://modelcontextprotocol.io/specification/2024-11-05/client/roots#listing-roots)
  * [Root List Changes](https://modelcontextprotocol.io/specification/2024-11-05/client/roots#root-list-changes)
  * [Project Directory](https://modelcontextprotocol.io/specification/2024-11-05/client/roots#project-directory)
  * [Multiple Repositories](https://modelcontextprotocol.io/specification/2024-11-05/client/roots#multiple-repositories)
  * [Error Handling](https://modelcontextprotocol.io/specification/2024-11-05/client/roots#error-handling)
  * [Security Considerations](https://modelcontextprotocol.io/specification/2024-11-05/client/roots#security-considerations)
  * [Implementation Guidelines](https://modelcontextprotocol.io/specification/2024-11-05/client/roots#implementation-guidelines)



