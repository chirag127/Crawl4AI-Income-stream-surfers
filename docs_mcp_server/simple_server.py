"""
Simple MCP server for documentation.
"""

import os
import sys
from pathlib import Path
from typing import Dict, Any, List
import logging

from mcp.server.fastmcp import FastMCP, Context

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger("docs-mcp-server")

# Create server
mcp = FastMCP("Documentation MCP Server")

# Documentation directory
DOCS_DIR = os.environ.get("DOCS_MCP_BASE_DIR", ".")
logger.info(f"Using documentation directory: {DOCS_DIR}")

# Simple functions to handle documentation
def list_docs(docs_dir: str = DOCS_DIR) -> List[Dict[str, Any]]:
    """List all documentation files."""
    result = []
    base_path = Path(docs_dir)
    
    if not base_path.exists():
        return result
    
    for path in base_path.glob("**/*.md"):
        if path.is_file():
            rel_path = path.relative_to(base_path)
            result.append({
                "path": str(rel_path),
                "title": path.stem,
                "size": path.stat().st_size,
                "modified": path.stat().st_mtime
            })
    
    return result

def read_doc(path: str, docs_dir: str = DOCS_DIR) -> str:
    """Read a documentation file."""
    file_path = Path(docs_dir) / path
    
    if not file_path.exists():
        return f"Documentation file not found: {path}"
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"Error reading file: {e}"

def search_docs(query: str, docs_dir: str = DOCS_DIR) -> List[Dict[str, Any]]:
    """Search documentation files."""
    results = []
    query = query.lower()
    
    for doc in list_docs(docs_dir):
        path = doc["path"]
        content = read_doc(path, docs_dir)
        
        if query in content.lower() or query in doc["title"].lower():
            # Find a snippet
            lines = content.split("\n")
            snippet = ""
            for line in lines:
                if query in line.lower():
                    snippet = line
                    break
            
            if not snippet and lines:
                snippet = lines[0]
            
            results.append({
                "path": path,
                "title": doc["title"],
                "snippet": snippet[:200] + "..." if len(snippet) > 200 else snippet
            })
    
    return results

# Register resources
@mcp.resource("docs://list")
def list_documentation() -> str:
    """
    List all available documentation files.
    
    Returns:
        str: Markdown-formatted list of documentation files
    """
    docs = list_docs()
    
    if not docs:
        return "No documentation files found."
    
    result = "# Available Documentation\n\n"
    
    for doc in docs:
        result += f"- **[{doc['title']}](docs://{doc['path']})** - {doc['path']}\n"
    
    return result

@mcp.resource("docs://{path}")
def get_documentation(path: str) -> str:
    """
    Get the content of a documentation file.
    
    Args:
        path: Path to the documentation file
        
    Returns:
        str: Content of the documentation file
    """
    content = read_doc(path)
    
    # Add metadata header
    header = f"# Documentation: {path}\n\n"
    header += f"*Source: {path}*\n\n---\n\n"
    
    return header + content

# Register tools
@mcp.tool()
def search_documentation(query: str, max_results: int = 5) -> List[Dict[str, Any]]:
    """
    Search documentation for the given query.
    
    Args:
        query: Search query string
        max_results: Maximum number of results to return (default: 5)
        
    Returns:
        List[Dict[str, Any]]: List of search results with path, title, and snippet
    """
    results = search_docs(query)
    return results[:max_results]

@mcp.tool()
def get_doc_info(path: str) -> Dict[str, Any]:
    """
    Get metadata information about a specific documentation file.
    
    Args:
        path: Path to the documentation file
        
    Returns:
        Dict[str, Any]: Metadata about the documentation file
    """
    file_path = Path(DOCS_DIR) / path
    
    if not file_path.exists():
        raise ValueError(f"Documentation file not found: {path}")
    
    return {
        "path": path,
        "title": file_path.stem,
        "size": file_path.stat().st_size,
        "modified": file_path.stat().st_mtime,
        "resource_uri": f"docs://{path}"
    }

if __name__ == "__main__":
    # Run the server
    mcp.run()
