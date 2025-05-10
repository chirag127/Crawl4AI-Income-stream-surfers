---
url: https://modelcontextprotocol.io/docs/concepts/roots
title: https://modelcontextprotocol.io/docs/concepts/roots
date: 2025-04-30T17:22:01.216295
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
Concepts
Roots
[User Guide](https://modelcontextprotocol.io/introduction)[SDKs](https://modelcontextprotocol.io/sdk/java/mcp-overview)[Specification](https://modelcontextprotocol.io/specification/2025-03-26)
[User Guide](https://modelcontextprotocol.io/introduction)[SDKs](https://modelcontextprotocol.io/sdk/java/mcp-overview)[Specification](https://modelcontextprotocol.io/specification/2025-03-26)
Roots are a concept in MCP that define the boundaries where servers can operate. They provide a way for clients to inform servers about relevant resources and their locations.
## What are Roots?
A root is a URI that a client suggests a server should focus on. When a client connects to a server, it declares which roots the server should work with. While primarily used for filesystem paths, roots can be any valid URI including HTTP URLs.
For example, roots could be:
Copy
```
file:///home/user/projects/myapp
https://api.example.com/v1

```

## Why Use Roots?
Roots serve several important purposes:
  1. **Guidance** : They inform servers about relevant resources and locations
  2. **Clarity** : Roots make it clear which resources are part of your workspace
  3. **Organization** : Multiple roots let you work with different resources simultaneously


## How Roots Work
When a client supports roots, it:
  1. Declares the `roots` capability during connection
  2. Provides a list of suggested roots to the server
  3. Notifies the server when roots change (if supported)


While roots are informational and not strictly enforcing, servers should:
  1. Respect the provided roots
  2. Use root URIs to locate and access resources
  3. Prioritize operations within root boundaries


## Common Use Cases
Roots are commonly used to define:
  * Project directories
  * Repository locations
  * API endpoints
  * Configuration locations
  * Resource boundaries


## Best Practices
When working with roots:
  1. Only suggest necessary resources
  2. Use clear, descriptive names for roots
  3. Monitor root accessibility
  4. Handle root changes gracefully


## Example
Here’s how a typical MCP client might expose roots:
Copy
```

 "roots": [

   "uri": "file:///home/user/projects/frontend",
   "name": "Frontend Repository"


   "uri": "https://api.example.com/v1",
   "name": "API Endpoint"




```

This configuration suggests the server focus on both a local repository and an API endpoint while keeping them logically separated.
Was this page helpful?
YesNo
On this page
  * [What are Roots?](https://modelcontextprotocol.io/docs/concepts/roots#what-are-roots%3F)
  * [Why Use Roots?](https://modelcontextprotocol.io/docs/concepts/roots#why-use-roots%3F)
  * [How Roots Work](https://modelcontextprotocol.io/docs/concepts/roots#how-roots-work)
  * [Common Use Cases](https://modelcontextprotocol.io/docs/concepts/roots#common-use-cases)
  * [Best Practices](https://modelcontextprotocol.io/docs/concepts/roots#best-practices)



