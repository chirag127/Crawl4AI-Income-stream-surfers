"""
Run the simple Documentation MCP Server with test documentation.
"""

import os
import sys
from pathlib import Path

# Set environment variables for the server
os.environ["DOCS_MCP_BASE_DIR"] = str(Path(__file__).parent / "test_docs")

# Import and run the server
from simple_server import mcp

if __name__ == "__main__":
    mcp.run()
