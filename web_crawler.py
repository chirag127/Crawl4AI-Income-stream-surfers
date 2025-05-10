#!/usr/bin/env python3
"""
Multi-URL Website Crawler

This script crawls a website starting from the homepage, finds internal links,
and saves the content of a specified number of pages as Markdown files.
The files are stored in a folder named after the website's domain.
"""

import asyncio
import os
import re
import argparse
import logging
from urllib.parse import urlparse
from datetime import datetime
from pathlib import Path

from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
from crawl4ai.deep_crawling import BFSDeepCrawlStrategy
from crawl4ai.deep_crawling.filters import FilterChain, DomainFilter
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator
from crawl4ai.content_filter_strategy import PruningContentFilter

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def extract_domain(url):
    """Extract and clean domain name from URL."""
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    # Remove www. if present
    domain = re.sub(r'^www\.', '', domain)
    return domain

def create_output_directory(domain):
    """Create directory for storing markdown files."""
    dir_path = Path(domain)
    dir_path.mkdir(exist_ok=True)
    return dir_path

def clean_filename(text):
    """Convert text to a valid filename."""
    if not text:
        return "unnamed"
    
    # Replace invalid filename characters with underscores
    cleaned = re.sub(r'[\\/*?:"<>|]', '_', text)
    # Replace multiple spaces with a single underscore
    cleaned = re.sub(r'\s+', '_', cleaned)
    # Limit length to avoid too long filenames
    return cleaned[:100]

def generate_filename(url, title=None, index=None):
    """Generate a unique filename for the markdown file."""
    parsed_url = urlparse(url)
    path = parsed_url.path
    
    # Use path or title for the filename
    if title and title.strip():
        base_name = clean_filename(title)
    else:
        # Use path or domain if path is empty/root
        path = path.strip('/')
        base_name = clean_filename(path) if path else parsed_url.netloc
    
    # Add index if provided to ensure uniqueness
    if index is not None:
        base_name = f"{index:03d}_{base_name}"
    
    return f"{base_name}.md"

def extract_title_from_markdown(markdown):
    """Extract title from markdown content (first heading)."""
    if not markdown:
        return None
    
    # Try to find the first heading
    title_match = re.search(r'^# (.+)$', markdown, re.MULTILINE)
    if title_match:
        return title_match.group(1)
    
    # If no heading found, try to use the first line
    lines = markdown.strip().split('\n')
    if lines:
        return lines[0][:100]  # Limit to 100 chars
    
    return None

async def save_markdown(output_dir, url, markdown, metadata=None, index=None):
    """
    Save markdown content to a file.
    
    Args:
        output_dir: Directory to save the file
        url: Original URL of the page
        markdown: Markdown content to save
        metadata: Dictionary of additional metadata
        index: Optional index for filename uniqueness
    
    Returns:
        Path to the saved file
    """
    # Extract title from markdown
    title = extract_title_from_markdown(markdown)
    
    # Generate filename
    filename = generate_filename(url, title, index)
    filepath = output_dir / filename
    
    # Ensure filename is unique by adding a suffix if needed
    counter = 1
    while filepath.exists():
        new_filename = f"{filename.rsplit('.', 1)[0]}_{counter}.md"
        filepath = output_dir / new_filename
        counter += 1
    
    # Prepare metadata header
    meta_header = "---\n"
    meta_header += f"url: {url}\n"
    meta_header += f"date_crawled: {datetime.now().isoformat()}\n"
    
    # Add additional metadata if provided
    if metadata:
        for key, value in metadata.items():
            meta_header += f"{key}: {value}\n"
    
    meta_header += "---\n\n"
    
    # Write to file
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(meta_header + markdown)
        return filepath
    except Exception as e:
        logger.error(f"Error saving file {filepath}: {e}")
        return None

async def crawl_website(homepage_url, num_pages=10, verbose=False):
    """
    Crawl a website starting from the homepage and save markdown files.
    
    Args:
        homepage_url: The homepage URL to start crawling from
        num_pages: Maximum number of pages to crawl
        verbose: Whether to print detailed progress
    
    Returns:
        List of paths to saved markdown files
    """
    # Set logging level based on verbosity
    if verbose:
        logger.setLevel(logging.DEBUG)
    
    # Extract domain for folder name and filtering
    domain = extract_domain(homepage_url)
    logger.info(f"Crawling {homepage_url} (domain: {domain})")
    
    # Create output directory
    output_dir = create_output_directory(domain)
    logger.info(f"Saving results to {output_dir}")
    
    # Configure browser
    browser_config = BrowserConfig(
        headless=True,  # Run in headless mode
        java_script_enabled=True,  # Enable JavaScript
        verbose=verbose
    )
    
    # Configure domain filter to stay within the same domain
    domain_filter = DomainFilter(
        allowed_domains=[domain]
    )
    filter_chain = FilterChain([domain_filter])
    
    # Configure deep crawl strategy
    deep_crawl_strategy = BFSDeepCrawlStrategy(
        max_depth=2,  # Crawl up to 2 levels deep
        include_external=False,  # Stay within the same domain
        max_pages=num_pages,  # Limit number of pages
        filter_chain=filter_chain  # Apply domain filtering
    )
    
    # Configure markdown generator with content filter
    md_generator = DefaultMarkdownGenerator(
        content_filter=PruningContentFilter(threshold=0.4),
        options={"ignore_links": False}  # Keep links in the markdown
    )
    
    # Configure crawler run
    run_config = CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS,  # Don't use cache
        deep_crawl_strategy=deep_crawl_strategy,
        markdown_generator=md_generator,
        stream=True,  # Enable streaming for processing results as they arrive
        verbose=verbose
    )
    
    # Initialize crawler and start crawling
    saved_files = []
    failed_urls = []
    
    try:
        async with AsyncWebCrawler(config=browser_config) as crawler:
            # Start the crawl with streaming enabled
            stream_results = await crawler.arun(homepage_url, config=run_config)
            async for i, result in enumerate(stream_results):
                if result.success:
                    logger.info(f"Successfully crawled: {result.url}")
                    
                    # Extract markdown content - handle both raw and filtered markdown
                    if hasattr(result.markdown, 'fit_markdown') and result.markdown.fit_markdown:
                        markdown_content = result.markdown.fit_markdown
                        markdown_type = "filtered"
                    elif hasattr(result.markdown, 'raw_markdown') and result.markdown.raw_markdown:
                        markdown_content = result.markdown.raw_markdown
                        markdown_type = "raw"
                    else:
                        markdown_content = str(result.markdown)
                        markdown_type = "default"
                    
                    # Prepare metadata
                    metadata = {
                        'crawl_depth': result.metadata.get('depth', 0),
                        'markdown_type': markdown_type,
                        'title': extract_title_from_markdown(markdown_content)
                    }
                    
                    # Save to file
                    filepath = await save_markdown(
                        output_dir, 
                        result.url, 
                        markdown_content, 
                        metadata=metadata,
                        index=i
                    )
                    
                    if filepath:
                        saved_files.append(filepath)
                        logger.info(f"Saved to {filepath}")
                    else:
                        logger.warning(f"Failed to save content from {result.url}")
                else:
                    logger.warning(f"Failed to crawl {result.url}: {result.error_message}")
                    failed_urls.append((result.url, result.error_message))
    
    except Exception as e:
        logger.error(f"Error during crawling: {e}")
        raise
    
    # Log summary
    logger.info(f"Crawling completed. Saved {len(saved_files)} files.")
    if failed_urls:
        logger.warning(f"Failed to crawl {len(failed_urls)} URLs:")
        for url, error in failed_urls[:5]:  # Show first 5 failures
            logger.warning(f"  - {url}: {error}")
        if len(failed_urls) > 5:
            logger.warning(f"  ... and {len(failed_urls) - 5} more.")
    
    return saved_files

def main():
    """Main entry point with argument parsing."""
    parser = argparse.ArgumentParser(description='Crawl a website and save pages as markdown files.')
    parser.add_argument('url', help='Homepage URL to start crawling from')
    parser.add_argument('-n', '--num-pages', type=int, default=10, 
                        help='Maximum number of pages to crawl (default: 10)')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='Print detailed progress')
    
    args = parser.parse_args()
    
    try:
        # Run the crawler
        saved_files = asyncio.run(crawl_website(args.url, args.num_pages, args.verbose))
        
        # Print summary
        print(f"\nCrawling completed. Saved {len(saved_files)} files.")
        
    except Exception as e:
        logger.error(f"Error: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())
