import os
import asyncio
import tempfile
import pandas as pd
from datetime import datetime

# Import Crawl4AI components
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, BrowserConfig, CacheMode, CrawlerMonitor
from crawl4ai.async_dispatcher import MemoryAdaptiveDispatcher

class CrawlJob:
    """
    Represents a web crawling job using Crawl4AI.
    Manages the crawling process, status tracking, and result processing.
    """

    def __init__(self, job_id: str, url: str, max_pages: int = 300):
        """
        Initialize a new crawl job.

        Args:
            job_id: Unique identifier for the job
            url: The starting URL to crawl
            max_pages: Maximum number of pages to crawl (default: 300)
        """
        self.job_id = job_id
        self.url = url
        self.max_pages = max_pages
        self.start_time = datetime.now()
        self.end_time = None
        self.status = "initialized"
        self.crawled_pages = 0
        self.results = []
        self.error = None

    def start_crawl(self):
        """
        Start the crawling process in a background thread.
        This method runs the async crawl using asyncio.run.
        """
        try:
            self.status = "in_progress"
            # Run the async crawl using asyncio.run
            asyncio.run(self._crawl_website())
            self.status = "completed"
        except Exception as e:
            self.status = "failed"
            self.error = str(e)
            print(f"Error in crawl job {self.job_id}: {e}")
        finally:
            self.end_time = datetime.now()

    async def _crawl_website(self):
        """
        Asynchronous method to crawl the website using Crawl4AI.
        """
        # Configure the browser
        browser_config = BrowserConfig(
            headless=True,
            verbose=False
        )

        # Configure the crawler run
        run_config = CrawlerRunConfig(
            cache_mode=CacheMode.BYPASS,
            stream=True,  # Enable streaming mode
            check_robots_txt=True,  # Respect robots.txt
            excluded_tags=["nav", "footer", "header"],  # Exclude common non-content elements
            exclude_external_links=True  # Only crawl internal links
        )

        # Configure the dispatcher
        # Create a monitor without display_mode parameter
        monitor = CrawlerMonitor(
            urls_total=self.max_pages,
            refresh_rate=1.0,
            enable_ui=True
        )

        # Configure the dispatcher
        dispatcher = MemoryAdaptiveDispatcher(
            memory_threshold_percent=70.0,
            check_interval=1.0,
            max_session_permit=10,
            monitor=monitor
        )

        # Start the crawler
        async with AsyncWebCrawler(config=browser_config) as crawler:
            # Use arun_many with a list of URLs
            # First, get the links from the homepage
            homepage_result = await crawler.arun(
                url=self.url,
                config=run_config
            )

            # Extract links from the homepage
            urls_to_crawl = []
            if homepage_result.success and hasattr(homepage_result, "links"):
                # Filter links to only include those from the same domain
                base_domain = self.url.split("//")[-1].split("/")[0]
                for link in homepage_result.links:
                    if base_domain in link and link not in urls_to_crawl and link != self.url:
                        urls_to_crawl.append(link)
                        if len(urls_to_crawl) >= self.max_pages - 1:  # -1 to account for the homepage
                            break

            # Process the homepage result
            if homepage_result.success:
                processed_result = self._process_result(homepage_result)
                self.results.append(processed_result)
                self.crawled_pages = len(self.results)

            # Crawl the remaining URLs
            if urls_to_crawl:
                # Enable streaming to process results as they come in
                run_config.stream = True

                # Use arun_many to crawl the remaining URLs
                async for result in await crawler.arun_many(
                    urls=urls_to_crawl,
                    config=run_config,
                    dispatcher=dispatcher
                ):
                    if result.success:
                        # Process and store the result
                        processed_result = self._process_result(result)
                        self.results.append(processed_result)
                        self.crawled_pages = len(self.results)
                    else:
                        # Log the error but continue with other pages
                        print(f"Failed to crawl {result.url}: {result.error_message}")

    def _process_result(self, result):
        """
        Process a crawl result into a standardized format.

        Args:
            result: The CrawlResult object from Crawl4AI

        Returns:
            dict: Processed result with standardized fields
        """
        # Extract the fit_markdown if available, otherwise use raw_markdown
        content = ""
        if hasattr(result, "markdown"):
            if hasattr(result.markdown, "fit_markdown"):
                content = result.markdown.fit_markdown
            else:
                content = result.markdown

        # Extract links
        links = []
        if hasattr(result, "links"):
            links = result.links

        # Extract tables if available
        tables = []
        if hasattr(result, "media") and "tables" in result.media:
            tables = result.media["tables"]

        # Create a standardized result dictionary
        return {
            "url": result.url,
            "title": result.metadata.get("title", "") if hasattr(result, "metadata") else "",
            "description": result.metadata.get("description", "") if hasattr(result, "metadata") else "",
            "content": content,
            "links": links,
            "timestamp": datetime.now().isoformat(),
            "status_code": result.status_code if hasattr(result, "status_code") else 0,
            "content_type": result.metadata.get("content_type", "") if hasattr(result, "metadata") else "",
            "tables": tables
        }

    def get_status(self):
        """
        Get the current status of the crawl job.

        Returns:
            dict: Status information including progress
        """
        return {
            "job_id": self.job_id,
            "url": self.url,
            "status": self.status,
            "crawled_pages": self.crawled_pages,
            "max_pages": self.max_pages,
            "start_time": self.start_time.isoformat(),
            "end_time": self.end_time.isoformat() if self.end_time else None,
            "error": self.error
        }

    def get_results(self):
        """
        Get the results of the crawl job.

        Returns:
            dict: Results and metadata
        """
        return {
            "job_id": self.job_id,
            "url": self.url,
            "status": self.status,
            "crawled_pages": self.crawled_pages,
            "max_pages": self.max_pages,
            "results": self.results
        }

    def to_csv(self):
        """
        Convert the crawl results to a CSV file.

        Returns:
            str: Path to the generated CSV file
        """
        # Create a list of dictionaries for the DataFrame
        data = []
        for result in self.results:
            # Flatten the result for CSV
            row = {
                "url": result["url"],
                "title": result["title"],
                "description": result["description"],
                "content_length": len(result["content"]) if result["content"] else 0,
                "links_count": len(result["links"]) if result["links"] else 0,
                "status_code": result["status_code"],
                "content_type": result["content_type"],
                "timestamp": result["timestamp"]
            }

            # Add the first few links as separate columns
            for i, link in enumerate(result["links"][:5]):
                row[f"link_{i+1}"] = link

            data.append(row)

        # Create a DataFrame
        df = pd.DataFrame(data)

        # Create a temporary file
        fd, path = tempfile.mkstemp(suffix='.csv')
        os.close(fd)

        # Save the DataFrame to CSV
        df.to_csv(path, index=False)

        return path
