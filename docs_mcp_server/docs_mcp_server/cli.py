"""
Command-line interface for the Documentation MCP Server.
"""

import os
import sys
import argparse
from pathlib import Path

from .server import run_server


def main():
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(
        description="Documentation MCP Server - A Model Context Protocol server for accessing documentation."
    )
    
    parser.add_argument(
        "--docs-dir",
        type=str,
        help="Base directory for documentation files (default: current directory)",
        default="."
    )
    
    parser.add_argument(
        "--extensions",
        type=str,
        help="Comma-separated list of file extensions to include (default: .md,.txt,.html)",
        default=".md,.txt,.html"
    )
    
    parser.add_argument(
        "--recursive",
        action="store_true",
        help="Scan subdirectories recursively (default: true)",
        default=True
    )
    
    parser.add_argument(
        "--no-recursive",
        action="store_false",
        dest="recursive",
        help="Don't scan subdirectories recursively"
    )
    
    parser.add_argument(
        "--log-level",
        type=str,
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        help="Logging level (default: INFO)",
        default="INFO"
    )
    
    parser.add_argument(
        "--transport",
        type=str,
        choices=["stdio", "sse"],
        help="Transport protocol to use (default: stdio)",
        default="stdio"
    )
    
    parser.add_argument(
        "--port",
        type=int,
        help="Port for SSE transport (default: 8000)",
        default=8000
    )
    
    args = parser.parse_args()
    
    # Set environment variables based on arguments
    os.environ["DOCS_MCP_BASE_DIR"] = args.docs_dir
    os.environ["DOCS_MCP_FILE_EXTENSIONS"] = args.extensions
    os.environ["DOCS_MCP_RECURSIVE"] = str(args.recursive).lower()
    os.environ["DOCS_MCP_LOG_LEVEL"] = args.log_level
    
    # Set FastMCP transport options
    if args.transport == "sse":
        os.environ["FASTMCP_TRANSPORT"] = "sse"
        os.environ["FASTMCP_PORT"] = str(args.port)
    else:
        os.environ["FASTMCP_TRANSPORT"] = "stdio"
    
    # Run the server
    run_server()


if __name__ == "__main__":
    main()
