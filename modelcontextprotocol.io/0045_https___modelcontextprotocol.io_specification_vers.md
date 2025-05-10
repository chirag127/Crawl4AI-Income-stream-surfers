---
url: https://modelcontextprotocol.io/specification/versioning
title: https://modelcontextprotocol.io/specification/versioning
date: 2025-04-30T17:22:33.598569
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
Resources
Versioning
[User Guide](https://modelcontextprotocol.io/introduction)[SDKs](https://modelcontextprotocol.io/sdk/java/mcp-overview)[Specification](https://modelcontextprotocol.io/specification/2025-03-26)
[User Guide](https://modelcontextprotocol.io/introduction)[SDKs](https://modelcontextprotocol.io/sdk/java/mcp-overview)[Specification](https://modelcontextprotocol.io/specification/2025-03-26)
The Model Context Protocol uses string-based version identifiers following the format `YYYY-MM-DD`, to indicate the last date backwards incompatible changes were made.
The protocol version will _not_ be incremented when the protocol is updated, as long as the changes maintain backwards compatibility. This allows for incremental improvements while preserving interoperability.
## Revisions
Revisions may be marked as:
  * **Draft** : in-progress specifications, not yet ready for consumption.
  * **Current** : the current protocol version, which is ready for use and may continue to receive backwards compatible changes.
  * **Final** : past, complete specifications that will not be changed.


The **current** protocol version is [**2025-03-26**](https://modelcontextprotocol.io/specification/2025-03-26).
## Negotiation
Version negotiation happens during [initialization](https://modelcontextprotocol.io/specification/2025-03-26/basic/lifecycle#initialization). Clients and servers **MAY** support multiple protocol versions simultaneously, but they **MUST** agree on a single version to use for the session.
The protocol provides appropriate error handling if version negotiation fails, allowing clients to gracefully terminate connections when they cannot find a version compatible with the server.
Was this page helpful?
YesNo
On this page



