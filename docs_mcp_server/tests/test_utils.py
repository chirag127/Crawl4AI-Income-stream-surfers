"""
Tests for the Documentation MCP Server utility functions.
"""

import os
import tempfile
from pathlib import Path

import pytest

from docs_mcp_server.utils import (
    scan_documentation,
    get_file_metadata,
    read_file_content,
    html_to_markdown,
    looks_like_code,
    extract_snippet,
)


def test_scan_documentation():
    """Test scanning documentation directory."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create test files
        base_dir = Path(temp_dir)
        
        # Create markdown file
        md_file = base_dir / "test.md"
        with open(md_file, "w") as f:
            f.write("# Test Document\n\nThis is a test document.")
        
        # Create text file
        txt_file = base_dir / "test.txt"
        with open(txt_file, "w") as f:
            f.write("This is a test text file.")
        
        # Create subdirectory with file
        subdir = base_dir / "subdir"
        subdir.mkdir()
        subdir_file = subdir / "subdir_test.md"
        with open(subdir_file, "w") as f:
            f.write("# Subdirectory Test\n\nThis is a test in a subdirectory.")
        
        # Test with recursive=True
        docs_index = scan_documentation(base_dir, [".md", ".txt"], recursive=True)
        assert len(docs_index) == 3
        assert "test.md" in docs_index
        assert "test.txt" in docs_index
        assert "subdir/subdir_test.md" in docs_index
        
        # Test with recursive=False
        docs_index = scan_documentation(base_dir, [".md", ".txt"], recursive=False)
        assert len(docs_index) == 2
        assert "test.md" in docs_index
        assert "test.txt" in docs_index
        assert "subdir/subdir_test.md" not in docs_index
        
        # Test with specific extensions
        docs_index = scan_documentation(base_dir, [".md"], recursive=True)
        assert len(docs_index) == 2
        assert "test.md" in docs_index
        assert "test.txt" not in docs_index
        assert "subdir/subdir_test.md" in docs_index


def test_get_file_metadata():
    """Test extracting metadata from a file."""
    with tempfile.NamedTemporaryFile(suffix=".md", mode="w+") as temp_file:
        # Write test content
        temp_file.write("# Test Title\n\nThis is a test description.\n\nMore content here.")
        temp_file.flush()
        
        # Get metadata
        metadata = get_file_metadata(Path(temp_file.name))
        
        # Check metadata
        assert metadata["title"] == "Test Title"
        assert metadata["description"] == "This is a test description."
        assert "size" in metadata
        assert "modified" in metadata


def test_read_file_content():
    """Test reading file content."""
    with tempfile.NamedTemporaryFile(suffix=".md", mode="w+") as temp_file:
        # Write test content
        test_content = "# Test Document\n\nThis is a test document."
        temp_file.write(test_content)
        temp_file.flush()
        
        # Read content
        content = read_file_content(Path(temp_file.name))
        
        # Check content
        assert content == test_content
        
        # Test with max_lines
        content = read_file_content(Path(temp_file.name), max_lines=1)
        assert content == "# Test Document\n"


def test_html_to_markdown():
    """Test converting HTML to markdown."""
    html = "<h1>Test Title</h1><p>This is a <strong>test</strong> paragraph.</p>"
    markdown = html_to_markdown(html)
    
    # Check conversion (simplified)
    assert "Test Title" in markdown
    assert "This is a test paragraph." in markdown


def test_looks_like_code():
    """Test detecting code content."""
    # Code-like content
    code = """
    def test_function():
        return "Hello, world!"
        
    if __name__ == "__main__":
        print(test_function())
    """
    assert looks_like_code(code)
    
    # Non-code content
    text = """
This is a regular text paragraph.
It doesn't have any code-like features.
Just plain text content.
    """
    assert not looks_like_code(text)


def test_extract_snippet():
    """Test extracting a relevant snippet."""
    content = """
# First Section

This is the first paragraph.

# Second Section

This is a paragraph about testing and examples.

# Third Section

This is the final paragraph.
"""
    
    # Test with matching terms
    snippet = extract_snippet(content, ["testing", "examples"])
    assert "testing" in snippet
    assert "examples" in snippet
    
    # Test with non-matching terms
    snippet = extract_snippet(content, ["nonexistent"])
    assert snippet  # Should return something even if no match
    
    # Test with max_length
    long_content = "A" * 300
    snippet = extract_snippet(long_content, ["A"], max_length=100)
    assert len(snippet) <= 103  # 100 + "..."
