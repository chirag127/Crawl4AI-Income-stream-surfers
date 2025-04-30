"""
Simple example of using the Documentation MCP Server.
"""

import asyncio
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client


async def main():
    # Create server parameters for stdio connection
    server_params = StdioServerParameters(
        command="docs-mcp-server",
        args=["--docs-dir", "../docs"],
        env={"DOCS_MCP_LOG_LEVEL": "INFO"},
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the connection
            await session.initialize()

            # List available resources
            resources = await session.list_resources()
            print("Available resources:")
            for resource in resources:
                print(f"- {resource.name}: {resource.description}")
            print()

            # List available tools
            tools = await session.list_tools()
            print("Available tools:")
            for tool in tools:
                print(f"- {tool.name}: {tool.description}")
            print()

            # Search for documentation
            print("Searching for 'installation'...")
            search_result = await session.call_tool("search_docs", {"query": "installation", "max_results": 3})
            print(f"Found {len(search_result)} results:")
            for result in search_result:
                print(f"- {result['title']} (score: {result['score']})")
                print(f"  Path: {result['path']}")
                print(f"  Snippet: {result['snippet'][:100]}...")
                print()

            # Get documentation structure
            print("Getting documentation structure...")
            structure = await session.call_tool("get_doc_structure", {})
            print(f"Found {len(structure['directories'])} directories and {len(structure['files'])} files")
            print("Directories:")
            for directory in structure["directories"]:
                print(f"- {directory['name']} ({directory['count']} files)")
            print("Files:")
            for file in structure["files"][:3]:  # Show only first 3 files
                print(f"- {file['title']}")
            print()

            # Read a documentation file
            if structure["files"]:
                file_path = structure["files"][0]["path"]
                print(f"Reading documentation file: {file_path}")
                content, mime_type = await session.read_resource(f"docs://{file_path}")
                print(f"Content type: {mime_type}")
                print("Content preview:")
                print(content[:500] + "...")


if __name__ == "__main__":
    asyncio.run(main())
