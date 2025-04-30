"""
Crawler module for multi-URL crawling using Crawl4AI.
This module provides functions to crawl a website starting from its homepage,
extract links, and save the results as markdown files.
"""

import os
import re
import asyncio
import json
import pandas as pd
from urllib.parse import urlparse, urljoin
from datetime import datetime
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
from crawl4ai.async_dispatcher import MemoryAdaptiveDispatcher
from crawl4ai.content_filter_strategy import PruningContentFilter
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator


class WebsiteCrawler:
    """Class for crawling websites using Crawl4AI."""
    
    def __init__(self, base_url, max_pages=100):
        """
        Initialize the crawler with base URL and maximum pages to crawl.
        
        Args:
            base_url (str): The homepage URL to start crawling from
            max_pages (int): Maximum number of pages to crawl (default: 100)
        """
        self.base_url = base_url
        self.max_pages = min(max_pages, 300)  # Limit to 300 pages
        self.domain = urlparse(base_url).netloc
        self.crawled_urls = []
        self.results = []
        self.progress = 0
        self.total_urls = 0
        self.status = "idle"
        self.start_time = None
        self.end_time = None
        
        # Create folder for storing results
        self.folder_name = self._get_folder_name()
        os.makedirs(self.folder_name, exist_ok=True)
        
    def _get_folder_name(self):
        """Generate a folder name based on the domain and timestamp."""
        domain = self.domain.replace(".", "_")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return f"{domain}_{timestamp}"
    
    async def extract_links(self):
        """
        Extract links from the homepage.
        
        Returns:
            list: List of URLs found on the homepage
        """
        self.status = "extracting_links"
        
        browser_config = BrowserConfig(headless=True, verbose=False)
        run_config = CrawlerRunConfig(
            cache_mode=CacheMode.BYPASS,
            excluded_tags=["nav", "footer", "header", "script", "style"],
            exclude_external_links=True
        )
        
        async with AsyncWebCrawler(config=browser_config) as crawler:
            result = await crawler.arun(
                url=self.base_url,
                config=run_config
            )
            
            if not result.success:
                self.status = "error"
                return []
            
            # Extract links from the result
            links = []
            if result.media and "links" in result.media:
                for link in result.media["links"]:
                    url = link.get("href", "")
                    # Ensure URL is absolute and belongs to the same domain
                    if url and not url.startswith(("http://", "https://")):
                        url = urljoin(self.base_url, url)
                    
                    parsed_url = urlparse(url)
                    if parsed_url.netloc == self.domain and url not in links:
                        links.append(url)
            
            # Limit to max_pages
            self.total_urls = min(len(links), self.max_pages)
            return links[:self.max_pages]
    
    async def crawl_urls(self, urls):
        """
        Crawl a list of URLs and save results.
        
        Args:
            urls (list): List of URLs to crawl
        """
        self.status = "crawling"
        self.start_time = datetime.now()
        
        # Configure content filter for better markdown output
        prune_filter = PruningContentFilter(
            threshold=0.45,
            threshold_type="dynamic",
            min_word_threshold=5
        )
        
        md_generator = DefaultMarkdownGenerator(content_filter=prune_filter)
        
        browser_config = BrowserConfig(headless=True, verbose=False)
        run_config = CrawlerRunConfig(
            cache_mode=CacheMode.BYPASS,
            excluded_tags=["nav", "footer", "header", "script", "style"],
            exclude_external_links=True,
            markdown_generator=md_generator,
            stream=True  # Enable streaming for real-time progress
        )
        
        # Configure dispatcher for parallel crawling
        dispatcher = MemoryAdaptiveDispatcher(
            memory_threshold_percent=70.0,
            check_interval=1.0,
            max_session_permit=10
        )
        
        async with AsyncWebCrawler(config=browser_config) as crawler:
            # Process results as they become available
            async for result in await crawler.arun_many(
                urls=urls,
                config=run_config,
                dispatcher=dispatcher
            ):
                if result.success:
                    # Save markdown to file
                    await self._save_markdown(result)
                    
                    # Store result metadata
                    self.results.append({
                        "url": result.url,
                        "title": result.title,
                        "word_count": len(result.markdown.fit_markdown.split()),
                        "status": "success",
                        "timestamp": datetime.now().isoformat()
                    })
                    
                    # Update progress
                    self.crawled_urls.append(result.url)
                    self.progress = len(self.crawled_urls)
                else:
                    # Store error information
                    self.results.append({
                        "url": result.url,
                        "title": "",
                        "word_count": 0,
                        "status": "error",
                        "error_message": result.error_message,
                        "timestamp": datetime.now().isoformat()
                    })
                    
                    # Update progress
                    self.crawled_urls.append(result.url)
                    self.progress = len(self.crawled_urls)
        
        self.end_time = datetime.now()
        self.status = "completed"
        
        # Save results summary to CSV
        self._save_results_csv()
    
    async def _save_markdown(self, result):
        """
        Save the markdown content to a file.
        
        Args:
            result: Crawl result object
        """
        # Create a safe filename from the URL
        parsed_url = urlparse(result.url)
        path = parsed_url.path.strip("/").replace("/", "_")
        if not path:
            path = "index"
        
        # Add a unique identifier to avoid filename collisions
        filename = f"{path}_{hash(result.url) % 10000}.md"
        filepath = os.path.join(self.folder_name, filename)
        
        # Write markdown content to file
        with open(filepath, "w", encoding="utf-8") as f:
            # Add metadata header
            f.write(f"# {result.title}\n\n")
            f.write(f"URL: {result.url}\n")
            f.write(f"Crawled: {datetime.now().isoformat()}\n\n")
            f.write("---\n\n")
            
            # Write the markdown content
            f.write(result.markdown.fit_markdown)
    
    def _save_results_csv(self):
        """Save crawl results to a CSV file."""
        df = pd.DataFrame(self.results)
        csv_path = os.path.join(self.folder_name, "results.csv")
        df.to_csv(csv_path, index=False)
        
        # Also save as JSON for easier processing
        json_path = os.path.join(self.folder_name, "results.json")
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump({
                "base_url": self.base_url,
                "domain": self.domain,
                "max_pages": self.max_pages,
                "total_crawled": len(self.crawled_urls),
                "start_time": self.start_time.isoformat() if self.start_time else None,
                "end_time": self.end_time.isoformat() if self.end_time else None,
                "results": self.results
            }, f, indent=2)
    
    def get_progress(self):
        """
        Get the current crawling progress.
        
        Returns:
            dict: Progress information
        """
        return {
            "status": self.status,
            "progress": self.progress,
            "total": self.total_urls,
            "percent": int(self.progress / max(1, self.total_urls) * 100),
            "crawled_urls": len(self.crawled_urls),
            "start_time": self.start_time.isoformat() if self.start_time else None,
            "end_time": self.end_time.isoformat() if self.end_time else None
        }
    
    def get_results(self):
        """
        Get the crawling results.
        
        Returns:
            dict: Results information
        """
        return {
            "base_url": self.base_url,
            "domain": self.domain,
            "folder_name": self.folder_name,
            "total_crawled": len(self.crawled_urls),
            "results": self.results,
            "start_time": self.start_time.isoformat() if self.start_time else None,
            "end_time": self.end_time.isoformat() if self.end_time else None
        }

async def start_crawling(url, max_pages):
    """
    Start the crawling process.
    
    Args:
        url (str): The homepage URL to start crawling from
        max_pages (int): Maximum number of pages to crawl
        
    Returns:
        WebsiteCrawler: The crawler instance
    """
    crawler = WebsiteCrawler(url, max_pages)
    urls = await crawler.extract_links()
    
    if urls:
        # Start crawling in a background task
        asyncio.create_task(crawler.crawl_urls(urls))
    else:
        crawler.status = "error"
        crawler.end_time = datetime.now()
    
    return crawler
