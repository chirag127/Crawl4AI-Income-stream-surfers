#!/usr/bin/env python3
"""
Multi-URL Crawler using Crawl4AI

This script crawls a website starting from the homepage, and saves the content
of each page as a markdown file in a folder named after the website.

Features:
- Memory-adaptive crawling to prevent freezing
- Rate limiting to avoid overwhelming servers
- Caching to avoid recrawling already processed pages
- Error handling and recovery
- Progress reporting
"""

import asyncio
import json
import os
import re
import time
import argparse
from datetime import datetime
from urllib.parse import urlparse

from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
from crawl4ai.deep_crawling import BFSDeepCrawlStrategy
from crawl4ai.content_filter_strategy import PruningContentFilter
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator
from crawl4ai.async_dispatcher import MemoryAdaptiveDispatcher, RateLimiter


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


def load_cache(cache_file):
    """Load the cache of crawled URLs."""
    if os.path.exists(cache_file):
        try:
            with open(cache_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading cache: {str(e)}")
    return {}


def save_cache(cache_file, cache):
    """Save the cache of crawled URLs."""
    try:
        with open(cache_file, 'w', encoding='utf-8') as f:
            json.dump(cache, f, indent=2)
    except Exception as e:
        print(f"Error saving cache: {str(e)}")


def write_summary(output_dir, stats, config):
    """Write a summary of the crawl."""
    try:
        filepath = os.path.join(output_dir, "summary.md")

        content = f"""# Crawl Summary

## Statistics
- Total pages crawled: {stats['total']}
- Successful crawls: {stats['success']}
- Failed crawls: {stats['failed']}
- Skipped (already crawled): {stats.get('skipped', 0)}
- Skipped (pattern filtered): {stats.get('pattern_filtered', 0)}
- Time taken: {stats['time_taken']:.2f} seconds

## Configuration
- Starting URL: {config['url']}
- Max pages: {config['max_pages']}
- Max depth: {config['max_depth']}
- Include external: {config['include_external']}
- Force recrawl: {config.get('force_recrawl', False)}
- URL pattern: {config.get('url_pattern', 'None')}

## Crawled URLs
"""

        # Add a note about URL filtering if a pattern was provided
        if config.get('url_pattern'):
            content += f"\nNote: URLs not matching the pattern '{config.get('url_pattern')}' were skipped but the crawler continued processing other URLs.\n"

        # Add filtered URLs section if any URLs were filtered
        if stats.get('pattern_filtered', 0) > 0 and stats.get('filtered_urls', []):
            content += f"\n## URLs Filtered by Pattern (showing up to 20)\n"
            for url in stats.get('filtered_urls', [])[:20]:  # Limit to 20 URLs to avoid huge files
                content += f"- {url}\n"

            if len(stats.get('filtered_urls', [])) > 20:
                content += f"\n... and {len(stats.get('filtered_urls', [])) - 20} more URLs were filtered.\n"

        for url in stats['urls']:
            content += f"- {url}\n"

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        return filepath
    except Exception as e:
        print(f"Error writing summary: {str(e)}")
        return None


async def crawl_website(url, max_pages=300, output_dir=None, max_depth=3, include_external=False, force_recrawl=False, url_pattern=None):
    """
    Crawl a website and save the results as markdown files.

    Args:
        url: The starting URL (homepage)
        max_pages: Maximum number of pages to crawl
        output_dir: Directory to save the markdown files
        max_depth: Maximum depth to crawl
        include_external: Whether to follow external links
        force_recrawl: Whether to recrawl pages that have already been crawled
        url_pattern: Pattern to filter URLs (will be converted to wildcard pattern)

    Returns:
        Dictionary with statistics about the crawl
    """
    # Create output directory if not provided
    if output_dir is None:
        website_name = extract_website_name(url)
        output_dir = create_output_directory(website_name)

    # Load cache
    cache_file = os.path.join(output_dir, "crawl_cache.json")
    cache = load_cache(cache_file)

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

    # Prepare URL pattern for application-level filtering
    url_pattern_regex = None
    if url_pattern:
        try:
            # Convert the pattern to a regex for application-level filtering
            # For example: "example" becomes ".*example.*"
            regex_pattern = f".*{url_pattern}.*"
            url_pattern_regex = re.compile(regex_pattern, re.IGNORECASE)
            print(f"Using URL pattern filter: {url_pattern} (regex: {regex_pattern})")
        except Exception as e:
            print(f"Warning: Invalid URL pattern '{url_pattern}': {str(e)}")
            print("Continuing without URL pattern filtering...")

    # Set up the deep crawl strategy without URL filtering
    # This allows the crawler to discover all URLs, and we'll filter at the application level
    deep_crawl_strategy = BFSDeepCrawlStrategy(
        max_depth=max_depth,
        include_external=include_external,
        max_pages=max_pages
    )

    # Create a rate limiter
    rate_limiter = RateLimiter(
        base_delay=(1.0, 3.0),  # Random delay between 1-3 seconds
        max_delay=30.0,         # Maximum backoff delay
        max_retries=3,          # Retry failed requests up to 3 times
        rate_limit_codes=[429, 503]  # Status codes that trigger backoff
    )

    # Create a dispatcher
    dispatcher = MemoryAdaptiveDispatcher(
        memory_threshold_percent=80.0,  # Pause if memory exceeds 80%
        check_interval=1.0,             # Check memory every second
        max_session_permit=5,           # Maximum concurrent tasks
        rate_limiter=rate_limiter       # Use our rate limiter
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
        'skipped': 0,
        'pattern_filtered': 0,  # URLs filtered by pattern
        'urls': [],
        'filtered_urls': [],    # URLs that didn't match the pattern
        'start_time': time.time()
    }

    # Start crawling
    print(f"Starting crawl of {url} with max {max_pages} pages...")
    try:
        async with AsyncWebCrawler(config=browser_config) as crawler:
            async for result in await crawler.arun(url, config=run_config, dispatcher=dispatcher):
                stats['total'] += 1

                # Skip URLs that have already been crawled unless force_recrawl is True
                if not force_recrawl and result.url in cache:
                    stats['skipped'] += 1
                    print(f"[{stats['total']}] Skipped: {result.url} - Already crawled on {cache[result.url]}")
                    continue

                # Check if URL matches the pattern (if a pattern was provided)
                if url_pattern and url_pattern_regex:
                    if not url_pattern_regex.match(result.url):
                        stats['pattern_filtered'] += 1
                        stats['filtered_urls'].append(result.url)
                        print(f"[{stats['total']}] Pattern filtered: {result.url} - Does not match pattern '{url_pattern}'")
                        continue

                if result.success:
                    stats['success'] += 1
                    stats['urls'].append(result.url)

                    # Save the markdown file
                    filepath = save_markdown_file(result, output_dir, stats['total'])
                    if filepath:
                        print(f"[{stats['total']}] Saved: {result.url} -> {os.path.basename(filepath)}")

                    # Update the cache with the current timestamp
                    cache[result.url] = datetime.now().isoformat()
                    # Save cache periodically (every 10 successful crawls)
                    if stats['success'] % 10 == 0:
                        save_cache(cache_file, cache)
                else:
                    stats['failed'] += 1
                    print(f"[{stats['total']}] Failed: {result.url} - {result.error_message}")
    except Exception as e:
        print(f"Error during crawl: {str(e)}")
        # Save cache on error to preserve progress
        save_cache(cache_file, cache)
        raise

    # Calculate time taken
    stats['time_taken'] = time.time() - stats['start_time']

    # Save final cache
    save_cache(cache_file, cache)

    # Write summary
    config = {
        'url': url,
        'max_pages': max_pages,
        'max_depth': max_depth,
        'include_external': include_external,
        'force_recrawl': force_recrawl,
        'url_pattern': url_pattern
    }
    summary_path = write_summary(output_dir, stats, config)
    if summary_path:
        print(f"Summary written to {summary_path}")

    return stats


def main():
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(description='Crawl a website and save pages as markdown files.')
    parser.add_argument('url', help='The homepage URL to start crawling from')
    parser.add_argument('--max-pages', type=int, default=500, help='Maximum number of pages to crawl (default: 500)')
    parser.add_argument('--output-dir', help='Base directory for output (default: website name)')
    parser.add_argument('--include-external', action='store_true', default=False, help='Follow external links')
    parser.add_argument('--max-depth', type=int, default=2, help='Maximum depth to crawl (default: 2)')
    parser.add_argument('--force-recrawl', action='store_true', default=False, help='Force recrawling of already crawled pages')
    parser.add_argument('--concurrent-tasks', type=int, default=5, help='Maximum number of concurrent crawling tasks (default: 5)')
    parser.add_argument('--url-pattern', default="https://developer.chrome.com/docs/extensions", help='Pattern to filter URLs (only URLs containing this pattern will be processed)')

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
            include_external=args.include_external,
            force_recrawl=args.force_recrawl,
            url_pattern=args.url_pattern
        ))

        # Print final statistics
        print("\nCrawl completed!")
        print(f"Total pages: {stats['total']}")
        print(f"Successful: {stats['success']}")
        print(f"Failed: {stats['failed']}")
        print(f"Skipped (already crawled): {stats.get('skipped', 0)}")
        print(f"Skipped (pattern filtered): {stats.get('pattern_filtered', 0)}")
        if args.url_pattern:
            print(f"URL pattern: {args.url_pattern}")
        print(f"Time taken: {stats['time_taken']:.2f} seconds")
        print(f"Results saved to: {output_dir}")

        return 0
    except Exception as e:
        print(f"Error during crawl: {str(e)}")
        return 1


if __name__ == "__main__":

    main()
