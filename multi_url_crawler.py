#!/usr/bin/env python3
"""
Multi-URL Crawler using Crawl4AI

This script crawls a website starting from the homepage, and saves the content
of each page as a markdown file in a folder named after the website.
"""

import asyncio
import os
import re
import time
import argparse
from datetime import datetime
from urllib.parse import urlparse
from pathlib import Path

from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
from crawl4ai.deep_crawling import BFSDeepCrawlStrategy
from crawl4ai.content_filter_strategy import PruningContentFilter
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator


def extract_website_name(url):
    """Extract a clean website name from a URL."""
    parsed_url = urlparse(url)
    domain = parsed_url.netloc

    # Remove www. prefix if present
    if domain.startswith('www.'):
        domain = domain[4:]

    return domain


def create_output_directory(website_name, base_dir='.'):
    """Create an output directory for the website."""
    output_dir = os.path.join(base_dir, website_name)
    os.makedirs(output_dir, exist_ok=True)
    return output_dir


def sanitize_filename(title, index):
    """Create a sanitized filename from a title."""
    # Remove invalid characters
    sanitized = re.sub(r'[\\/*?:"<>|]', "_", title)
    # Remove extra whitespace
    sanitized = re.sub(r'\s+', ' ', sanitized).strip()
    # Limit length
    sanitized = sanitized[:50]
    # Add index for uniqueness
    return f"{index:04d}_{sanitized}.md"


def save_markdown_file(result, output_dir, index):
    """Save a crawl result as a markdown file."""
    try:
        # Extract title or use URL if title not available
        title = result.title if hasattr(result, 'title') and result.title else result.url

        # Create sanitized filename
        filename = sanitize_filename(title, index)
        filepath = os.path.join(output_dir, filename)

        # Format content with metadata
        content = f"""---
url: {result.url}
title: {title}
date: {datetime.now().isoformat()}
depth: {result.metadata.get('depth', 0)}
---

{result.markdown.fit_markdown if hasattr(result.markdown, 'fit_markdown') else result.markdown}
"""

        # Write to file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        return filepath
    except Exception as e:
        print(f"Error saving file for {result.url}: {str(e)}")
        return None


def write_summary(output_dir, stats, config):
    """Write a summary of the crawl."""
    try:
        filepath = os.path.join(output_dir, "summary.md")

        content = f"""# Crawl Summary

## Statistics
- Total pages crawled: {stats['total']}
- Successful crawls: {stats['success']}
- Failed crawls: {stats['failed']}
- Time taken: {stats['time_taken']:.2f} seconds

## Configuration
- Starting URL: {config['url']}
- Max pages: {config['max_pages']}
- Max depth: {config['max_depth']}
- Include external: {config['include_external']}

## Crawled URLs
"""

        for url in stats['urls']:
            content += f"- {url}\n"

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        return filepath
    except Exception as e:
        print(f"Error writing summary: {str(e)}")
        return None


async def crawl_website(url, max_pages=300, output_dir=None, max_depth=3, include_external=False):
    """
    Crawl a website and save the results as markdown files.

    Args:
        url: The starting URL (homepage)
        max_pages: Maximum number of pages to crawl
        output_dir: Directory to save the markdown files
        max_depth: Maximum depth to crawl
        include_external: Whether to follow external links

    Returns:
        Dictionary with statistics about the crawl
    """
    # Create output directory if not provided
    if output_dir is None:
        website_name = extract_website_name(url)
        output_dir = create_output_directory(website_name)

    # Configure the content filter for better markdown
    content_filter = PruningContentFilter(threshold=0.4, threshold_type="dynamic")
    md_generator = DefaultMarkdownGenerator(
        content_filter=content_filter,
        options={
            "ignore_links": False,
            "body_width": 0,  # No wrapping
            "escape_html": True
        }
    )

    # Configure the crawler
    browser_config = BrowserConfig(
        headless=True,
        java_script_enabled=True,
        verbose=False
    )

    # Set up the deep crawl strategy
    deep_crawl_strategy = BFSDeepCrawlStrategy(
        max_depth=max_depth,
        include_external=include_external,
        max_pages=max_pages
    )

    run_config = CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS,
        deep_crawl_strategy=deep_crawl_strategy,
        markdown_generator=md_generator,
        stream=True,
        verbose=True
    )

    # Statistics tracking
    stats = {
        'total': 0,
        'success': 0,
        'failed': 0,
        'urls': [],
        'start_time': time.time()
    }

    # Start crawling
    print(f"Starting crawl of {url} with max {max_pages} pages...")
    async with AsyncWebCrawler(config=browser_config) as crawler:
        async for result in await crawler.arun(url, config=run_config):
            stats['total'] += 1

            if result.success:
                stats['success'] += 1
                stats['urls'].append(result.url)

                # Save the markdown file
                filepath = save_markdown_file(result, output_dir, stats['total'])
                if filepath:
                    print(f"[{stats['total']}] Saved: {result.url} -> {os.path.basename(filepath)}")
            else:
                stats['failed'] += 1
                print(f"[{stats['total']}] Failed: {result.url} - {result.error_message}")

    # Calculate time taken
    stats['time_taken'] = time.time() - stats['start_time']

    # Write summary
    config = {
        'url': url,
        'max_pages': max_pages,
        'max_depth': max_depth,
        'include_external': include_external
    }
    summary_path = write_summary(output_dir, stats, config)
    if summary_path:
        print(f"Summary written to {summary_path}")

    return stats


def main():
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(description='Crawl a website and save pages as markdown files.')
    parser.add_argument('url', help='The homepage URL to start crawling from')
    parser.add_argument('--max-pages', type=int, default=500, help='Maximum number of pages to crawl (default: 300)')
    parser.add_argument('--output-dir', help='Base directory for output (default: website name)')
    parser.add_argument('--include-external', action='store_true', default=False, help='Follow external links')
    parser.add_argument('--max-depth', type=int, default=2, help='Maximum depth to crawl (default: 2)')

    args = parser.parse_args()

    # Validate URL
    try:
        parsed_url = urlparse(args.url)
        if not parsed_url.scheme or not parsed_url.netloc:
            raise ValueError("Invalid URL")
    except Exception:
        print(f"Error: '{args.url}' is not a valid URL")
        return 1

    # Create output directory if specified
    output_dir = None
    if args.output_dir:
        output_dir = args.output_dir
    else:
        website_name = extract_website_name(args.url)
        output_dir = create_output_directory(website_name)

    # Run the crawler
    try:
        stats = asyncio.run(crawl_website(
            args.url,
            max_pages=args.max_pages,
            output_dir=output_dir,
            max_depth=args.max_depth,
            include_external=args.include_external
        ))

        # Print final statistics
        print("\nCrawl completed!")
        print(f"Total pages: {stats['total']}")
        print(f"Successful: {stats['success']}")
        print(f"Failed: {stats['failed']}")
        print(f"Time taken: {stats['time_taken']:.2f} seconds")
        print(f"Results saved to: {output_dir}")

        return 0
    except Exception as e:
        print(f"Error during crawl: {str(e)}")
        return 1


if __name__ == "__main__":

    main()
