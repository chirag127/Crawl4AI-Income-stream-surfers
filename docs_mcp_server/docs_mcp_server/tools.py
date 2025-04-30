"""
Tools for the Documentation MCP Server.
"""

from typing import List, Dict, Any
import os
from pathlib import Path

from mcp.server.fastmcp import FastMCP, Context

from .utils import search_documentation


def register_tools(server: FastMCP) -> None:
    """
    Register documentation tools with the MCP server.

    Args:
        server: The FastMCP server instance
    """

    @server.tool()
    def search_docs(query: str, ctx: Context, max_results: int = 5) -> List[Dict[str, Any]]:
        """
        Search documentation for the given query.

        Args:
            query: Search query string
            max_results: Maximum number of results to return (default: 5)
            ctx: MCP context

        Returns:
            List[Dict[str, Any]]: List of search results with path, title, snippet, and score
        """
        docs_index = ctx.request_context.lifespan_context.docs_index
        base_dir = ctx.request_context.lifespan_context.docs_base_dir

        results = search_documentation(
            query=query,
            docs_index=docs_index,
            base_dir=base_dir,
            max_results=max_results
        )

        # Format results for better readability
        formatted_results = []
        for result in results:
            formatted_results.append({
                "path": result["path"],
                "title": result["title"],
                "snippet": result["snippet"],
                "score": result["score"],
                "resource_uri": f"docs://{result['path']}"
            })

        return formatted_results

    @server.tool()
    def get_doc_structure(ctx: Context, path: str = "") -> Dict[str, Any]:
        """
        Get the structure of documentation in the specified path.

        Args:
            path: Path to get structure for (default: root)
            ctx: MCP context

        Returns:
            Dict[str, Any]: Structure of documentation with directories and files
        """
        docs_index = ctx.request_context.lifespan_context.docs_index

        # Build structure for the specified path
        structure = {"directories": {}, "files": []}

        for doc_path, info in docs_index.items():
            # Check if this document is in the requested path
            if not path or doc_path.startswith(path + "/") or doc_path == path:
                # Get relative path from the requested path
                rel_path = doc_path
                if path and doc_path.startswith(path + "/"):
                    rel_path = doc_path[len(path) + 1:]

                # If this is a direct file in the requested path
                if path and doc_path == path:
                    structure["files"].append({
                        "path": doc_path,
                        "title": info.get("title", os.path.basename(doc_path)),
                        "description": info.get("description", "")
                    })
                    continue

                # Handle nested paths
                if "/" in rel_path:
                    dir_name = rel_path.split("/")[0]
                    if dir_name not in structure["directories"]:
                        structure["directories"][dir_name] = {
                            "path": os.path.join(path, dir_name) if path else dir_name,
                            "count": 0
                        }
                    structure["directories"][dir_name]["count"] += 1
                else:
                    structure["files"].append({
                        "path": doc_path,
                        "title": info.get("title", os.path.basename(doc_path)),
                        "description": info.get("description", "")
                    })

        # Convert directories dict to list for easier consumption
        structure["directories"] = [
            {"name": name, **info}
            for name, info in structure["directories"].items()
        ]

        # Sort directories and files
        structure["directories"].sort(key=lambda x: x["name"])
        structure["files"].sort(key=lambda x: x["path"])

        return structure

    @server.tool()
    def get_doc_info(path: str, ctx: Context) -> Dict[str, Any]:
        """
        Get metadata information about a specific documentation file.

        Args:
            path: Path to the documentation file
            ctx: MCP context

        Returns:
            Dict[str, Any]: Metadata about the documentation file

        Raises:
            ValueError: If the file does not exist
        """
        docs_index = ctx.request_context.lifespan_context.docs_index

        if path not in docs_index:
            raise ValueError(f"Documentation file not found: {path}")

        info = docs_index[path].copy()
        info["path"] = path
        info["resource_uri"] = f"docs://{path}"

        return info
