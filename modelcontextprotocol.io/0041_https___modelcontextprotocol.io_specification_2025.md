---
url: https://modelcontextprotocol.io/specification/2025-03-26/contributing
title: https://modelcontextprotocol.io/specification/2025-03-26/contributing
date: 2025-04-30T17:22:32.228102
depth: 2
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
Introduction
[User Guide](https://modelcontextprotocol.io/introduction)[SDKs](https://modelcontextprotocol.io/sdk/java/mcp-overview)[Specification](https://modelcontextprotocol.io/specification/2025-03-26)
[User Guide](https://modelcontextprotocol.io/introduction)[SDKs](https://modelcontextprotocol.io/sdk/java/mcp-overview)[Specification](https://modelcontextprotocol.io/specification/2025-03-26)
C# SDK released! Check out [what else is new.](https://modelcontextprotocol.io/development/updates)
MCP is an open protocol that standardizes how applications provide context to LLMs. Think of MCP like a USB-C port for AI applications. Just as USB-C provides a standardized way to connect your devices to various peripherals and accessories, MCP provides a standardized way to connect AI models to different data sources and tools.
## Why MCP?
MCP helps you build agents and complex workflows on top of LLMs. LLMs frequently need to integrate with data and tools, and MCP provides:
  * A growing list of pre-built integrations that your LLM can directly plug into
  * The flexibility to switch between LLM providers and vendors
  * Best practices for securing your data within your infrastructure


### General architecture
At its core, MCP follows a client-server architecture where a host application can connect to multiple servers:
Internet
Your Computer
MCP Protocol
MCP Protocol
MCP Protocol
Web APIs
Host with MCP Client(Claude, IDEs, Tools)
MCP Server A
MCP Server B
MCP Server C
LocalData Source A
LocalData Source B
RemoteService C
  * **MCP Hosts** : Programs like Claude Desktop, IDEs, or AI tools that want to access data through MCP
  * **MCP Clients** : Protocol clients that maintain 1:1 connections with servers
  * **MCP Servers** : Lightweight programs that each expose specific capabilities through the standardized Model Context Protocol
  * **Local Data Sources** : Your computer’s files, databases, and services that MCP servers can securely access
  * **Remote Services** : External systems available over the internet (e.g., through APIs) that MCP servers can connect to


## Get started
Choose the path that best fits your needs:
#### Quick Starts
## [For Server DevelopersGet started building your own server to use in Claude for Desktop and other clients](https://modelcontextprotocol.io/quickstart/server)## [For Client DevelopersGet started building your own client that can integrate with all MCP servers](https://modelcontextprotocol.io/quickstart/client)## [For Claude Desktop UsersGet started using pre-built servers in Claude for Desktop](https://modelcontextprotocol.io/quickstart/user)
#### Examples
## [Example ServersCheck out our gallery of official MCP servers and implementations](https://modelcontextprotocol.io/examples)## [Example ClientsView the list of clients that support MCP integrations](https://modelcontextprotocol.io/clients)
## Tutorials
## [Building MCP with LLMsLearn how to use LLMs like Claude to speed up your MCP development](https://modelcontextprotocol.io/tutorials/building-mcp-with-llms)## [Debugging GuideLearn how to effectively debug MCP servers and integrations](https://modelcontextprotocol.io/docs/tools/debugging)## [MCP InspectorTest and inspect your MCP servers with our interactive debugging tool](https://modelcontextprotocol.io/docs/tools/inspector)## [MCP Workshop (Video, 2hr)](https://www.youtube.com/watch?v=kQmXtrmQ5Zg)
## Explore MCP
Dive deeper into MCP’s core concepts and capabilities:
## [Core architectureUnderstand how MCP connects clients, servers, and LLMs](https://modelcontextprotocol.io/docs/concepts/architecture)## [ResourcesExpose data and content from your servers to LLMs](https://modelcontextprotocol.io/docs/concepts/resources)## [PromptsCreate reusable prompt templates and workflows](https://modelcontextprotocol.io/docs/concepts/prompts)## [ToolsEnable LLMs to perform actions through your server](https://modelcontextprotocol.io/docs/concepts/tools)## [SamplingLet your servers request completions from LLMs](https://modelcontextprotocol.io/docs/concepts/sampling)## [TransportsLearn about MCP’s communication mechanism](https://modelcontextprotocol.io/docs/concepts/transports)
## Contributing
Want to contribute? Check out our [Contributing Guide](https://modelcontextprotocol.io/development/contributing) to learn how you can help improve MCP.
## Support and Feedback
Here’s how to get help or provide feedback:
  * For bug reports and feature requests related to the MCP specification, SDKs, or documentation (open source), please [create a GitHub issue](https://github.com/modelcontextprotocol)
  * For discussions or Q&A about the MCP specification, use the [specification discussions](https://github.com/modelcontextprotocol/specification/discussions)
  * For discussions or Q&A about other MCP open source components, use the [organization discussions](https://github.com/orgs/modelcontextprotocol/discussions)
  * For bug reports, feature requests, and questions related to Claude.app and claude.ai’s MCP integration, please see Anthropic’s guide on [How to Get Support](https://support.anthropic.com/en/articles/9015913-how-to-get-support)


Was this page helpful?
YesNo
[For Server Developers](https://modelcontextprotocol.io/quickstart/server)
On this page
  * [General architecture](https://modelcontextprotocol.io/introduction#general-architecture)
  * [Support and Feedback](https://modelcontextprotocol.io/introduction#support-and-feedback)



