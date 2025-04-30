"""
Run the Documentation MCP Server with test documentation.
"""

import os
import sys
from pathlib import Path

# Add the package directory to the Python path
sys.path.insert(0, str(Path(__file__).parent))

# Set environment variables for the server
os.environ["DOCS_MCP_BASE_DIR"] = str(Path(__file__).parent / "test_docs")
os.environ["DOCS_MCP_FILE_EXTENSIONS"] = ".md,.txt,.html"
os.environ["DOCS_MCP_RECURSIVE"] = "true"
os.environ["DOCS_MCP_LOG_LEVEL"] = "INFO"

# Import and run the server
from docs_mcp_server.server import run_server

if __name__ == "__main__":
    run_server()
