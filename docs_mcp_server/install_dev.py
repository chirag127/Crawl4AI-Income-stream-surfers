"""
Install the package in development mode.
"""

import subprocess
import sys
import os
from pathlib import Path

# Get the directory of this script
script_dir = Path(__file__).parent.absolute()

# Run pip install -e .
subprocess.check_call([sys.executable, "-m", "pip", "install", "-e", str(script_dir)])

print("Package installed in development mode.")
