"""
Main server implementation for the Documentation MCP Server.
"""

import os
import logging
from pathlib import Path
from typing import List, Dict, Optional, Any
from contextlib import asynccontextmanager
from collections.abc import AsyncIterator
from dataclasses import dataclass

from mcp.server.fastmcp import FastMCP, Context

from .utils import scan_documentation, read_file_content, search_documentation
from .resources import register_resources
from .tools import register_tools

# Configure logging
logging.basicConfig(
    level=os.environ.get("DOCS_MCP_LOG_LEVEL", "INFO"),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger("docs-mcp-server")


@dataclass
class ServerContext:
    """Context for the Documentation MCP Server."""
    docs_base_dir: Path
    docs_index: Dict[str, Dict[str, Any]]
    file_extensions: List[str]


@asynccontextmanager
async def server_lifespan(server: FastMCP) -> AsyncIterator[ServerContext]:
    """
    Manage server lifecycle and initialize documentation index.
    
    Args:
        server: The FastMCP server instance
        
    Yields:
        ServerContext: Context containing documentation index and configuration
    """
    # Get configuration from environment variables
    docs_base_dir = os.environ.get("DOCS_MCP_BASE_DIR", ".")
    file_extensions_str = os.environ.get("DOCS_MCP_FILE_EXTENSIONS", ".md,.txt,.html")
    recursive = os.environ.get("DOCS_MCP_RECURSIVE", "true").lower() == "true"
    
    # Parse configuration
    base_dir = Path(docs_base_dir)
    file_extensions = file_extensions_str.split(",")
    
    logger.info(f"Initializing Documentation MCP Server with base directory: {base_dir}")
    logger.info(f"File extensions: {file_extensions}")
    logger.info(f"Recursive scanning: {recursive}")
    
    # Scan documentation directory and build index
    docs_index = scan_documentation(base_dir, file_extensions, recursive)
    logger.info(f"Indexed {len(docs_index)} documentation files")
    
    # Create and yield server context
    try:
        yield ServerContext(
            docs_base_dir=base_dir,
            docs_index=docs_index,
            file_extensions=file_extensions,
        )
    finally:
        # Cleanup (if needed)
        logger.info("Shutting down Documentation MCP Server")


def create_server() -> FastMCP:
    """
    Create and configure the Documentation MCP Server.
    
    Returns:
        FastMCP: Configured server instance
    """
    # Create server with lifespan
    server = FastMCP(
        "Documentation MCP Server",
        lifespan=server_lifespan,
        dependencies=["mcp>=1.0.0"],
    )
    
    # Register resources and tools
    register_resources(server)
    register_tools(server)
    
    return server


# Create the server instance
mcp_server = create_server()


def run_server():
    """Run the Documentation MCP Server."""
    mcp_server.run()


if __name__ == "__main__":
    run_server()
