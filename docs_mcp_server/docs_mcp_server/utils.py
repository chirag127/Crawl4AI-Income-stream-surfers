"""
Utility functions for the Documentation MCP Server.
"""

import os
import re
from pathlib import Path
from typing import Dict, List, Any, Tuple, Optional
import logging

logger = logging.getLogger("docs-mcp-server")


def scan_documentation(
    base_dir: Path,
    file_extensions: List[str],
    recursive: bool = True
) -> Dict[str, Dict[str, Any]]:
    """
    Scan the documentation directory and build an index.
    
    Args:
        base_dir: Base directory to scan
        file_extensions: List of file extensions to include
        recursive: Whether to scan subdirectories recursively
        
    Returns:
        Dict[str, Dict[str, Any]]: Index of documentation files
    """
    docs_index = {}
    
    if not base_dir.exists():
        logger.warning(f"Base directory does not exist: {base_dir}")
        return docs_index
    
    # Normalize file extensions
    normalized_extensions = [ext.lower() for ext in file_extensions]
    normalized_extensions = [ext if ext.startswith(".") else f".{ext}" for ext in normalized_extensions]
    
    # Walk directory
    for root, dirs, files in os.walk(base_dir):
        # Skip if not recursive and not in base directory
        if not recursive and root != str(base_dir):
            continue
        
        for file in files:
            file_path = Path(root) / file
            
            # Check file extension
            if any(file.lower().endswith(ext) for ext in normalized_extensions):
                # Get relative path from base directory
                rel_path = file_path.relative_to(base_dir)
                rel_path_str = str(rel_path).replace("\\", "/")  # Normalize path separators
                
                # Extract metadata
                metadata = get_file_metadata(file_path)
                
                # Add to index
                docs_index[rel_path_str] = metadata
    
    return docs_index


def get_file_metadata(file_path: Path) -> Dict[str, Any]:
    """
    Extract metadata from a documentation file.
    
    Args:
        file_path: Path to the file
        
    Returns:
        Dict[str, Any]: Metadata extracted from the file
    """
    metadata = {
        "title": file_path.stem,
        "description": "",
        "size": file_path.stat().st_size,
        "modified": file_path.stat().st_mtime
    }
    
    # Try to extract title and description from file content
    try:
        content = read_file_content(file_path, max_lines=20)
        
        # Look for title in first heading
        title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        if title_match:
            metadata["title"] = title_match.group(1).strip()
        
        # Look for description in first paragraph after title
        desc_match = re.search(r'^#.*?\n\n(.+?)(\n\n|$)', content, re.DOTALL)
        if desc_match:
            metadata["description"] = desc_match.group(1).strip()
    except Exception as e:
        logger.warning(f"Error extracting metadata from {file_path}: {e}")
    
    return metadata


def read_file_content(file_path: Path, max_lines: Optional[int] = None) -> str:
    """
    Read content from a file and convert to markdown if needed.
    
    Args:
        file_path: Path to the file
        max_lines: Maximum number of lines to read (None for all)
        
    Returns:
        str: File content as markdown
        
    Raises:
        FileNotFoundError: If the file does not exist
        PermissionError: If the file cannot be read
    """
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            if max_lines is not None:
                lines = [next(f) for _ in range(max_lines)]
                content = ''.join(lines)
            else:
                content = f.read()
    except UnicodeDecodeError:
        # Try with different encoding
        with open(file_path, 'r', encoding='latin-1') as f:
            if max_lines is not None:
                lines = [next(f) for _ in range(max_lines)]
                content = ''.join(lines)
            else:
                content = f.read()
    
    # Convert to markdown based on file extension
    ext = file_path.suffix.lower()
    
    if ext == '.html':
        # Simple HTML to markdown conversion
        # In a real implementation, use a proper HTML to markdown converter
        content = html_to_markdown(content)
    elif ext == '.txt':
        # Wrap plain text in markdown code blocks if it looks like code
        if looks_like_code(content):
            content = f"```\n{content}\n```"
    
    return content


def html_to_markdown(html_content: str) -> str:
    """
    Convert HTML to markdown (simplified version).
    
    Args:
        html_content: HTML content
        
    Returns:
        str: Markdown content
    """
    # This is a very simplified conversion
    # In a real implementation, use a proper HTML to markdown converter
    
    # Remove HTML tags (very basic)
    markdown = re.sub(r'<[^>]*>', '', html_content)
    
    # Unescape HTML entities
    markdown = markdown.replace('&lt;', '<').replace('&gt;', '>').replace('&amp;', '&')
    
    return markdown


def looks_like_code(content: str) -> bool:
    """
    Check if content looks like code.
    
    Args:
        content: Text content
        
    Returns:
        bool: True if content looks like code
    """
    # Simple heuristic: if more than 15% of lines start with whitespace
    # or contain special characters like {, }, (, ), it's probably code
    lines = content.split('\n')
    if not lines:
        return False
    
    code_line_count = 0
    for line in lines:
        if line.startswith('    ') or line.startswith('\t'):
            code_line_count += 1
        elif re.search(r'[{}\[\]()<>]', line):
            code_line_count += 1
    
    return code_line_count / len(lines) > 0.15


def search_documentation(
    query: str,
    docs_index: Dict[str, Dict[str, Any]],
    base_dir: Path,
    max_results: int = 5
) -> List[Dict[str, Any]]:
    """
    Search documentation for the given query.
    
    Args:
        query: Search query string
        docs_index: Index of documentation files
        base_dir: Base directory of documentation
        max_results: Maximum number of results to return
        
    Returns:
        List[Dict[str, Any]]: List of search results with path, title, snippet, and score
    """
    results = []
    
    # Normalize query
    query = query.lower()
    query_terms = query.split()
    
    for path, info in docs_index.items():
        file_path = base_dir / path
        
        try:
            # Read file content
            content = read_file_content(file_path)
            
            # Calculate score based on term frequency
            score = 0
            content_lower = content.lower()
            
            # Check title match (higher weight)
            title = info.get("title", "").lower()
            for term in query_terms:
                if term in title:
                    score += 10
            
            # Check content match
            for term in query_terms:
                term_count = content_lower.count(term)
                score += term_count
            
            # If any match found
            if score > 0:
                # Find best snippet
                snippet = extract_snippet(content, query_terms)
                
                results.append({
                    "path": path,
                    "title": info.get("title", path),
                    "snippet": snippet,
                    "score": score
                })
        except Exception as e:
            logger.warning(f"Error searching file {path}: {e}")
    
    # Sort by score and limit results
    results.sort(key=lambda x: x["score"], reverse=True)
    return results[:max_results]


def extract_snippet(content: str, query_terms: List[str], max_length: int = 200) -> str:
    """
    Extract a relevant snippet from content based on query terms.
    
    Args:
        content: Document content
        query_terms: List of query terms
        max_length: Maximum snippet length
        
    Returns:
        str: Relevant snippet from the content
    """
    # Split content into paragraphs
    paragraphs = re.split(r'\n\s*\n', content)
    
    best_paragraph = None
    best_score = -1
    
    for paragraph in paragraphs:
        if not paragraph.strip():
            continue
        
        paragraph_lower = paragraph.lower()
        score = 0
        
        for term in query_terms:
            score += paragraph_lower.count(term)
        
        if score > best_score:
            best_score = score
            best_paragraph = paragraph
    
    if not best_paragraph:
        # If no matching paragraph, use the first non-empty one
        for paragraph in paragraphs:
            if paragraph.strip():
                best_paragraph = paragraph
                break
    
    if not best_paragraph:
        return ""
    
    # Truncate if needed
    if len(best_paragraph) > max_length:
        # Try to truncate at word boundary
        truncated = best_paragraph[:max_length]
        last_space = truncated.rfind(' ')
        if last_space > max_length * 0.8:  # Only truncate at word if we're not losing too much
            truncated = truncated[:last_space]
        return truncated + "..."
    
    return best_paragraph
