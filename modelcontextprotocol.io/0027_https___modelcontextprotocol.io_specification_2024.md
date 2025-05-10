---
url: https://modelcontextprotocol.io/specification/2024-11-05/basic/lifecycle
title: https://modelcontextprotocol.io/specification/2024-11-05/basic/lifecycle
date: 2025-04-30T17:22:26.067057
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
    * Utilities
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
Base Protocol
Lifecycle
[User Guide](https://modelcontextprotocol.io/introduction)[SDKs](https://modelcontextprotocol.io/sdk/java/mcp-overview)[Specification](https://modelcontextprotocol.io/specification/2025-03-26)
[User Guide](https://modelcontextprotocol.io/introduction)[SDKs](https://modelcontextprotocol.io/sdk/java/mcp-overview)[Specification](https://modelcontextprotocol.io/specification/2025-03-26)
**Protocol Revision** : 2024-11-05
The Model Context Protocol (MCP) defines a rigorous lifecycle for client-server connections that ensures proper capability negotiation and state management.
  1. **Initialization** : Capability negotiation and protocol version agreement
  2. **Operation** : Normal protocol communication
  3. **Shutdown** : Graceful termination of the connection


ServerClientServerClientInitialization PhaseOperation PhaseNormal protocol operationsShutdownConnection closedinitialize requestinitialize responseinitialized notificationDisconnect
## Lifecycle Phases
### Initialization
The initialization phase **MUST** be the first interaction between client and server. During this phase, the client and server:
  * Establish protocol version compatibility
  * Exchange and negotiate capabilities
  * Share implementation details


The client **MUST** initiate this phase by sending an `initialize` request containing:
  * Protocol version supported
  * Client capabilities
  * Client implementation information


Copy
```

 "jsonrpc": "2.0",
 "id": 1,
 "method": "initialize",
 "params": {
  "protocolVersion": "2024-11-05",
  "capabilities": {
   "roots": {
    "listChanged": true

   "sampling": {}

  "clientInfo": {
   "name": "ExampleClient",
   "version": "1.0.0"




```

The server **MUST** respond with its own capabilities and information:
Copy
```

 "jsonrpc": "2.0",
 "id": 1,
 "result": {
  "protocolVersion": "2024-11-05",
  "capabilities": {
   "logging": {},
   "prompts": {
    "listChanged": true

   "resources": {
    "subscribe": true,
    "listChanged": true

   "tools": {
    "listChanged": true


  "serverInfo": {
   "name": "ExampleServer",
   "version": "1.0.0"




```

After successful initialization, the client **MUST** send an `initialized` notification to indicate it is ready to begin normal operations:
Copy
```

 "jsonrpc": "2.0",
 "method": "notifications/initialized"


```

  * The client **SHOULD NOT** send requests other than [pings](https://modelcontextprotocol.io/specification/2024-11-05/basic/utilities/ping) before the server has responded to the `initialize` request.
  * The server **SHOULD NOT** send requests other than [pings](https://modelcontextprotocol.io/specification/2024-11-05/basic/utilities/ping) and [logging](https://modelcontextprotocol.io/specification/2024-11-05/server/utilities/logging) before receiving the `initialized` notification.


#### Version Negotiation
In the `initialize` request, the client **MUST** send a protocol version it supports. This **SHOULD** be the _latest_ version supported by the client.
If the server supports the requested protocol version, it **MUST** respond with the same version. Otherwise, the server **MUST** respond with another protocol version it supports. This **SHOULD** be the _latest_ version supported by the server.
If the client does not support the version in the server’s response, it **SHOULD** disconnect.
#### Capability Negotiation
Client and server capabilities establish which optional protocol features will be available during the session.
Key capabilities include:
Category| Capability| Description  
---|---|---  
Client| `roots`| Ability to provide filesystem [roots](https://modelcontextprotocol.io/specification/2024-11-05/client/roots)  
Client| `sampling`| Support for LLM [sampling](https://modelcontextprotocol.io/specification/2024-11-05/client/sampling) requests  
Client| `experimental`| Describes support for non-standard experimental features  
Server| `prompts`| Offers [prompt templates](https://modelcontextprotocol.io/specification/2024-11-05/server/prompts)  
Server| `resources`| Provides readable [resources](https://modelcontextprotocol.io/specification/2024-11-05/server/resources)  
Server| `tools`| Exposes callable [tools](https://modelcontextprotocol.io/specification/2024-11-05/server/tools)  
Server| `logging`| Emits structured [log messages](https://modelcontextprotocol.io/specification/2024-11-05/server/utilities/logging)  
Server| `experimental`| Describes support for non-standard experimental features  
Capability objects can describe sub-capabilities like:
  * `listChanged`: Support for list change notifications (for prompts, resources, and tools)
  * `subscribe`: Support for subscribing to individual items’ changes (resources only)


### Operation
During the operation phase, the client and server exchange messages according to the negotiated capabilities.
Both parties **SHOULD** :
  * Respect the negotiated protocol version
  * Only use capabilities that were successfully negotiated


### Shutdown
During the shutdown phase, one side (usually the client) cleanly terminates the protocol connection. No specific shutdown messages are defined—instead, the underlying transport mechanism should be used to signal connection termination:
#### stdio
For the stdio [transport](https://modelcontextprotocol.io/specification/2024-11-05/basic/transports), the client **SHOULD** initiate shutdown by:
  1. First, closing the input stream to the child process (the server)
  2. Waiting for the server to exit, or sending `SIGTERM` if the server does not exit within a reasonable time
  3. Sending `SIGKILL` if the server does not exit within a reasonable time after `SIGTERM`


The server **MAY** initiate shutdown by closing its output stream to the client and exiting.
#### HTTP
For HTTP [transports](https://modelcontextprotocol.io/specification/2024-11-05/basic/transports), shutdown is indicated by closing the associated HTTP connection(s).
## Error Handling
Implementations **SHOULD** be prepared to handle these error cases:
  * Protocol version mismatch
  * Failure to negotiate required capabilities
  * Initialize request timeout
  * Shutdown timeout


Implementations **SHOULD** implement appropriate timeouts for all requests, to prevent hung connections and resource exhaustion.
Example initialization error:
Copy
```

 "jsonrpc": "2.0",
 "id": 1,
 "error": {
  "code": -32602,
  "message": "Unsupported protocol version",
  "data": {
   "supported": ["2024-11-05"],
   "requested": "1.0.0"




```

Was this page helpful?
YesNo
On this page
  * [Lifecycle Phases](https://modelcontextprotocol.io/specification/2024-11-05/basic/lifecycle#lifecycle-phases)
  * [Initialization](https://modelcontextprotocol.io/specification/2024-11-05/basic/lifecycle#initialization)
  * [Version Negotiation](https://modelcontextprotocol.io/specification/2024-11-05/basic/lifecycle#version-negotiation)
  * [Capability Negotiation](https://modelcontextprotocol.io/specification/2024-11-05/basic/lifecycle#capability-negotiation)
  * [Error Handling](https://modelcontextprotocol.io/specification/2024-11-05/basic/lifecycle#error-handling)



