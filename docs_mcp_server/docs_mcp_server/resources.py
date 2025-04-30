"""
Resource handlers for the Documentation MCP Server.
"""

import os
from pathlib import Path
from typing import Dict, Any, List

from mcp.server.fastmcp import FastMCP, Context

from .utils import read_file_content, get_file_metadata


def register_resources(server: FastMCP) -> None:
    """
    Register documentation resources with the MCP server.
    
    Args:
        server: The FastMCP server instance
    """
    
    @server.resource("docs://list")
    def list_documentation(ctx: Context) -> str:
        """
        List all available documentation files.
        
        Returns:
            str: Markdown-formatted list of documentation files
        """
        docs_index = ctx.request_context.lifespan_context.docs_index
        base_dir = ctx.request_context.lifespan_context.docs_base_dir
        
        if not docs_index:
            return "No documentation files found."
        
        result = "# Available Documentation\n\n"
        
        # Group by directories
        grouped_docs: Dict[str, List[Dict[str, Any]]] = {}
        for path, info in docs_index.items():
            dir_path = os.path.dirname(path)
            if dir_path not in grouped_docs:
                grouped_docs[dir_path] = []
            grouped_docs[dir_path].append({
                "path": path,
                "title": info.get("title", path),
                "description": info.get("description", "")
            })
        
        # Generate markdown list
        for dir_path, files in sorted(grouped_docs.items()):
            if dir_path:
                result += f"## {dir_path}\n\n"
            else:
                result += "## Root Directory\n\n"
                
            for file_info in sorted(files, key=lambda x: x["path"]):
                path = file_info["path"]
                title = file_info["title"]
                description = file_info["description"]
                
                result += f"- **[{title}](docs://{path})** - {description}\n"
            
            result += "\n"
        
        return result
    
    @server.resource("docs://{path}")
    def get_documentation(path: str, ctx: Context) -> str:
        """
        Get the content of a documentation file.
        
        Args:
            path: Path to the documentation file
            ctx: MCP context
            
        Returns:
            str: Content of the documentation file
            
        Raises:
            ValueError: If the file does not exist
        """
        docs_index = ctx.request_context.lifespan_context.docs_index
        base_dir = ctx.request_context.lifespan_context.docs_base_dir
        
        if path not in docs_index:
            raise ValueError(f"Documentation file not found: {path}")
        
        file_path = base_dir / path
        content = read_file_content(file_path)
        
        # Add metadata header
        metadata = docs_index[path]
        header = f"# {metadata.get('title', path)}\n\n"
        if "description" in metadata and metadata["description"]:
            header += f"{metadata['description']}\n\n"
        header += f"*Source: {path}*\n\n---\n\n"
        
        return header + content
    
    @server.resource("docs://toc")
    def get_table_of_contents(ctx: Context) -> str:
        """
        Get a table of contents for all documentation.
        
        Returns:
            str: Markdown-formatted table of contents
        """
        docs_index = ctx.request_context.lifespan_context.docs_index
        
        if not docs_index:
            return "No documentation files found."
        
        result = "# Documentation Table of Contents\n\n"
        
        # Build directory tree
        tree: Dict[str, Any] = {"dirs": {}, "files": []}
        
        for path, info in docs_index.items():
            parts = path.split("/")
            current = tree
            
            # Navigate through directories
            for i, part in enumerate(parts[:-1]):
                if part not in current["dirs"]:
                    current["dirs"][part] = {"dirs": {}, "files": []}
                current = current["dirs"][part]
            
            # Add file
            current["files"].append({
                "name": parts[-1],
                "path": path,
                "title": info.get("title", parts[-1]),
                "description": info.get("description", "")
            })
        
        # Generate markdown from tree
        def render_tree(node: Dict[str, Any], prefix: str = "") -> str:
            output = ""
            
            # Render files
            for file_info in sorted(node["files"], key=lambda x: x["path"]):
                title = file_info["title"]
                path = file_info["path"]
                output += f"{prefix}- **[{title}](docs://{path})**\n"
            
            # Render directories
            for dir_name, dir_node in sorted(node["dirs"].items()):
                output += f"{prefix}- **{dir_name}/**\n"
                output += render_tree(dir_node, prefix + "  ")
            
            return output
        
        result += render_tree(tree)
        return result
