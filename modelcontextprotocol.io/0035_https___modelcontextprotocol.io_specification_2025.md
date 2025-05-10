---
url: https://modelcontextprotocol.io/specification/2025-03-26/changelog
title: https://modelcontextprotocol.io/specification/2025-03-26/changelog
date: 2025-04-30T17:22:29.703526
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
2025-03-26 (Latest)
Key Changes
[User Guide](https://modelcontextprotocol.io/introduction)[SDKs](https://modelcontextprotocol.io/sdk/java/mcp-overview)[Specification](https://modelcontextprotocol.io/specification/2025-03-26)
[User Guide](https://modelcontextprotocol.io/introduction)[SDKs](https://modelcontextprotocol.io/sdk/java/mcp-overview)[Specification](https://modelcontextprotocol.io/specification/2025-03-26)
This document lists changes made to the Model Context Protocol (MCP) specification since the previous revision, [2024-11-05](https://modelcontextprotocol.io/specification/2024-11-05).
## Major changes
  1. Added a comprehensive **[authorization framework](https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization)** based on OAuth 2.1 (PR [#133](https://github.com/modelcontextprotocol/specification/pull/133))
  2. Replaced the previous HTTP+SSE transport with a more flexible **[Streamable HTTP transport](https://modelcontextprotocol.io/specification/2025-03-26/basic/transports#streamable-http)** (PR [#206](https://github.com/modelcontextprotocol/specification/pull/206))
  3. Added support for JSON-RPC (PR [#228](https://github.com/modelcontextprotocol/specification/pull/228))
  4. Added comprehensive **tool annotations** for better describing tool behavior, like whether it is read-only or destructive (PR [#185](https://github.com/modelcontextprotocol/specification/pull/185))


## Other schema changes
  * Added `message` field to `ProgressNotification` to provide descriptive status updates
  * Added support for audio data, joining the existing text and image content types
  * Added `completions` capability to explicitly indicate support for argument autocompletion suggestions


See [the updated schema](http://github.com/modelcontextprotocol/specification/tree/main/schema/2025-03-26/schema.ts) for more details.
## Full changelog
For a complete list of all changes that have been made since the last protocol revision, [see GitHub](https://github.com/modelcontextprotocol/specification/compare/2024-11-05...2025-03-26).
Was this page helpful?
YesNo
[Specification](https://modelcontextprotocol.io/specification/2025-03-26)[Architecture](https://modelcontextprotocol.io/specification/2025-03-26/architecture)
On this page
  * [Major changes](https://modelcontextprotocol.io/specification/2025-03-26/changelog#major-changes)
  * [Other schema changes](https://modelcontextprotocol.io/specification/2025-03-26/changelog#other-schema-changes)
  * [Full changelog](https://modelcontextprotocol.io/specification/2025-03-26/changelog#full-changelog)



