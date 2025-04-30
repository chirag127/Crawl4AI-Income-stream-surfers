Make me a multi URL crawling flask project which takes the homepage of a website and then crawl 300 found pages using crawl4ai and allows for .csv download and saves all previous downloads in browser cache/cookies

Crawl4AI: Open-source LLM Friendly Web Crawler & Scraper.
unclecode%2Fcrawl4ai | Trendshift

GitHub Stars GitHub Forks

PyPI version Python Version Downloads

License Code style: black Security: bandit Contributor Covenant

Crawl4AI is the #1 trending GitHub repository, actively maintained by a vibrant community. It delivers blazing-fast, AI-ready web crawling tailored for LLMs, AI agents, and data pipelines. Open source, flexible, and built for real-time performance, Crawl4AI empowers developers with unmatched speed, precision, and deployment ease.

✨ Check out latest update v0.6.0

🎉 Version 0.6.0 is now available! This release candidate introduces World-aware Crawling with geolocation and locale settings, Table-to-DataFrame extraction, Browser pooling with pre-warming, Network and console traffic capture, MCP integration for AI tools, and a completely revamped Docker deployment! Read the release notes →

🤓 My Personal Story
🧐 Why Crawl4AI?
Built for LLMs: Creates smart, concise Markdown optimized for RAG and fine-tuning applications.
Lightning Fast: Delivers results 6x faster with real-time, cost-efficient performance.
Flexible Browser Control: Offers session management, proxies, and custom hooks for seamless data access.
Heuristic Intelligence: Uses advanced algorithms for efficient extraction, reducing reliance on costly models.
Open Source & Deployable: Fully open-source with no API keys—ready for Docker and cloud integration.
Thriving Community: Actively maintained by a vibrant community and the #1 trending GitHub repository.
🚀 Quick Start
Install Crawl4AI:
# Install the package
pip install -U crawl4ai

# For pre release versions
pip install crawl4ai --pre

# Run post-installation setup
crawl4ai-setup

# Verify your installation
crawl4ai-doctor
If you encounter any browser-related issues, you can install them manually:

python -m playwright install --with-deps chromium
Run a simple web crawl with Python:
import asyncio
from crawl4ai import *

async def main():
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
            url="https://www.nbcnews.com/business",
        )
        print(result.markdown)

if __name__ == "__main__":
    asyncio.run(main())
Or use the new command-line interface:
# Basic crawl with markdown output
crwl https://www.nbcnews.com/business -o markdown

# Deep crawl with BFS strategy, max 10 pages
crwl https://docs.crawl4ai.com --deep-crawl bfs --max-pages 10

# Use LLM extraction with a specific question
crwl https://www.example.com/products -q "Extract all product prices"
✨ Features
📝 Markdown Generation
📊 Structured Data Extraction
🌐 Browser Integration
🔎 Crawling & Scraping
🚀 Deployment
🎯 Additional Features
Try it Now!
✨ Play around with this Open In Colab

✨ Visit our Documentation Website

Installation 🛠️
Crawl4AI offers flexible installation options to suit various use cases. You can install it as a Python package or use Docker.

🐍 Using pip
🐳 Docker Deployment
Quick Test
Run a quick test (works for both Docker options):

import requests

# Submit a crawl job
response = requests.post(
    "http://localhost:11235/crawl",
    json={"urls": "https://example.com", "priority": 10}
)
task_id = response.json()["task_id"]

# Continue polling until the task is complete (status="completed")
result = requests.get(f"http://localhost:11235/task/{task_id}")
For more examples, see our Docker Examples. For advanced configuration, environment variables, and usage examples, see our Docker Deployment Guide.

🔬 Advanced Usage Examples 🔬
You can check the project structure in the directory https://github.com/unclecode/crawl4ai/docs/examples. Over there, you can find a variety of examples; here, some popular examples are shared.

📝 Heuristic Markdown Generation with Clean and Fit Markdown
🖥️ Executing JavaScript & Extract Structured Data without LLMs
📚 Extracting Structured Data with LLMs
🤖 Using You own Browser with Custom User Profile
✨ Recent Updates
Version 0.6.0 Release Highlights
🌎 World-aware Crawling: Set geolocation, language, and timezone for authentic locale-specific content:

  crun_cfg = CrawlerRunConfig(
      url="https://browserleaks.com/geo",          # test page that shows your location
      locale="en-US",                              # Accept-Language & UI locale
      timezone_id="America/Los_Angeles",           # JS Date()/Intl timezone
      geolocation=GeolocationConfig(                 # override GPS coords
          latitude=34.0522,
          longitude=-118.2437,
          accuracy=10.0,
      )
  )
📊 Table-to-DataFrame Extraction: Extract HTML tables directly to CSV or pandas DataFrames:

  crawler = AsyncWebCrawler(config=browser_config)
  await crawler.start()

  try:
      # Set up scraping parameters
      crawl_config = CrawlerRunConfig(
          table_score_threshold=8,  # Strict table detection
      )

      # Execute market data extraction
      results: List[CrawlResult] = await crawler.arun(
          url="https://coinmarketcap.com/?page=1", config=crawl_config
      )

      # Process results
      raw_df = pd.DataFrame()
      for result in results:
          if result.success and result.media["tables"]:
              raw_df = pd.DataFrame(
                  result.media["tables"][0]["rows"],
                  columns=result.media["tables"][0]["headers"],
              )
              break
      print(raw_df.head())

  finally:
      await crawler.stop()
🚀 Browser Pooling: Pages launch hot with pre-warmed browser instances for lower latency and memory usage

🕸️ Network and Console Capture: Full traffic logs and MHTML snapshots for debugging:

crawler_config = CrawlerRunConfig(
    capture_network=True,
    capture_console=True,
    mhtml=True
)
🔌 MCP Integration: Connect to AI tools like Claude Code through the Model Context Protocol

# Add Crawl4AI to Claude Code
claude mcp add --transport sse c4ai-sse http://localhost:11235/mcp/sse
🖥️ Interactive Playground: Test configurations and generate API requests with the built-in web interface at http://localhost:11235//playground

🐳 Revamped Docker Deployment: Streamlined multi-architecture Docker image with improved resource efficiency

📱 Multi-stage Build System: Optimized Dockerfile with platform-specific performance enhancements

Read the full details in our 0.6.0 Release Notes or check the CHANGELOG.

Previous Version: 0.5.0 Major Release Highlights
🚀 Deep Crawling System: Explore websites beyond initial URLs with BFS, DFS, and BestFirst strategies
⚡ Memory-Adaptive Dispatcher: Dynamically adjusts concurrency based on system memory
🔄 Multiple Crawling Strategies: Browser-based and lightweight HTTP-only crawlers
💻 Command-Line Interface: New crwl CLI provides convenient terminal access
👤 Browser Profiler: Create and manage persistent browser profiles
🧠 Crawl4AI Coding Assistant: AI-powered coding assistant
🏎️ LXML Scraping Mode: Fast HTML parsing using the lxml library
🌐 Proxy Rotation: Built-in support for proxy switching
🤖 LLM Content Filter: Intelligent markdown generation using LLMs
📄 PDF Processing: Extract text, images, and metadata from PDF files
Read the full details in our 0.5.0 Release Notes.

Version Numbering in Crawl4AI
Crawl4AI follows standard Python version numbering conventions (PEP 440) to help users understand the stability and features of each release.

Version Numbers Explained
Our version numbers follow this pattern: MAJOR.MINOR.PATCH (e.g., 0.4.3)

Pre-release Versions
We use different suffixes to indicate development stages:

dev (0.4.3dev1): Development versions, unstable
a (0.4.3a1): Alpha releases, experimental features
b (0.4.3b1): Beta releases, feature complete but needs testing
rc (0.4.3): Release candidates, potential final version
Installation
Regular installation (stable version):

pip install -U crawl4ai
Install pre-release versions:

pip install crawl4ai --pre
Install specific version:

pip install crawl4ai==0.4.3b1
Why Pre-releases?
We use pre-releases to:

Test new features in real-world scenarios
Gather feedback before final releases
Ensure stability for production users
Allow early adopters to try new features
For production environments, we recommend using the stable version. For testing new features, you can opt-in to pre-releases using the --pre flag.

📖 Documentation & Roadmap
🚨 Documentation Update Alert: We're undertaking a major documentation overhaul next week to reflect recent updates and improvements. Stay tuned for a more comprehensive and up-to-date guide!

For current documentation, including installation instructions, advanced features, and API reference, visit our Documentation Website.

To check our development plans and upcoming features, visit our Roadmap.

📈 Development TODOs
🤝 Contributing
We welcome contributions from the open-source community. Check out our contribution guidelines for more information.

I'll help modify the license section with badges. For the halftone effect, here's a version with it:

Here's the updated license section:

📄 License & Attribution
This project is licensed under the Apache License 2.0 with a required attribution clause. See the Apache 2.0 License file for details.

Attribution Requirements
When using Crawl4AI, you must include one of the following attribution methods:

1. Badge Attribution (Recommended)
Add one of these badges to your README, documentation, or website:

Theme	Badge
Disco Theme (Animated)	Powered by Crawl4AI
Night Theme (Dark with Neon)	Powered by Crawl4AI
Dark Theme (Classic)	Powered by Crawl4AI
Light Theme (Classic)	Powered by Crawl4AI
HTML code for adding the badges:

<!-- Disco Theme (Animated) -->
<a href="https://github.com/unclecode/crawl4ai">
  <img src="https://raw.githubusercontent.com/unclecode/crawl4ai/main/docs/assets/powered-by-disco.svg" alt="Powered by Crawl4AI" width="200"/>
</a>

<!-- Night Theme (Dark with Neon) -->
<a href="https://github.com/unclecode/crawl4ai">
  <img src="https://raw.githubusercontent.com/unclecode/crawl4ai/main/docs/assets/powered-by-night.svg" alt="Powered by Crawl4AI" width="200"/>
</a>

<!-- Dark Theme (Classic) -->
<a href="https://github.com/unclecode/crawl4ai">
  <img src="https://raw.githubusercontent.com/unclecode/crawl4ai/main/docs/assets/powered-by-dark.svg" alt="Powered by Crawl4AI" width="200"/>
</a>

<!-- Light Theme (Classic) -->
<a href="https://github.com/unclecode/crawl4ai">
  <img src="https://raw.githubusercontent.com/unclecode/crawl4ai/main/docs/assets/powered-by-light.svg" alt="Powered by Crawl4AI" width="200"/>
</a>

<!-- Simple Shield Badge -->
<a href="https://github.com/unclecode/crawl4ai">
  <img src="https://img.shields.io/badge/Powered%20by-Crawl4AI-blue?style=flat-square" alt="Powered by Crawl4AI"/>
</a>
2. Text Attribution
Add this line to your documentation:

This project uses Crawl4AI (https://github.com/unclecode/crawl4ai) for web data extraction.
📚 Citation
If you use Crawl4AI in your research or project, please cite:

@software{crawl4ai2024,
  author = {UncleCode},
  title = {Crawl4AI: Open-source LLM Friendly Web Crawler & Scraper},
  year = {2024},
  publisher = {GitHub},
  journal = {GitHub Repository},
  howpublished = {\url{https://github.com/unclecode/crawl4ai}},
  commit = {Please use the commit hash you're working with}
}
Text citation format:

UncleCode. (2024). Crawl4AI: Open-source LLM Friendly Web Crawler & Scraper [Computer software].
GitHub. https://github.com/unclecode/crawl4ai
📧 Contact
For questions, suggestions, or feedback, feel free to reach out:

GitHub: unclecode
Twitter: @unclecode
Website: crawl4ai.com
Happy Crawling! 🕸️🚀

🗾 Mission
Our mission is to unlock the value of personal and enterprise data by transforming digital footprints into structured, tradeable assets. Crawl4AI empowers individuals and organizations with open-source tools to extract and structure data, fostering a shared data economy.

We envision a future where AI is powered by real human knowledge, ensuring data creators directly benefit from their contributions. By democratizing data and enabling ethical sharing, we are laying the foundation for authentic AI advancement.

🔑 Key Opportunities
🚀 Development Pathway
Star History
Star History Chart

fetch or get the use of https://docs.crawl4ai.com/advanced/multi-url-crawling/

get or fetch the use of https://docs.crawl4ai.com/core/fit-markdown/









Fit Markdown with Pruning & BM25
Fit Markdown is a specialized filtered version of your page’s markdown, focusing on the most relevant content. By default, Crawl4AI converts the entire HTML into a broad raw_markdown. With fit markdown, we apply a content filter algorithm (e.g., Pruning or BM25) to remove or rank low-value sections—such as repetitive sidebars, shallow text blocks, or irrelevancies—leaving a concise textual “core.”

1. How “Fit Markdown” Works
1.1 The content_filter
In CrawlerRunConfig, you can specify a content_filter to shape how content is pruned or ranked before final markdown generation. A filter’s logic is applied before or during the HTML→Markdown process, producing:

result.markdown.raw_markdown (unfiltered)
result.markdown.fit_markdown (filtered or “fit” version)
result.markdown.fit_html (the corresponding HTML snippet that produced fit_markdown)
1.2 Common Filters
1. PruningContentFilter – Scores each node by text density, link density, and tag importance, discarding those below a threshold.
2. BM25ContentFilter – Focuses on textual relevance using BM25 ranking, especially useful if you have a specific user query (e.g., “machine learning” or “food nutrition”).

2. PruningContentFilter
Pruning discards less relevant nodes based on text density, link density, and tag importance. It’s a heuristic-based approach—if certain sections appear too “thin” or too “spammy,” they’re pruned.

2.1 Usage Example
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from crawl4ai.content_filter_strategy import PruningContentFilter
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator

async def main():
    # Step 1: Create a pruning filter
    prune_filter = PruningContentFilter(
        # Lower → more content retained, higher → more content pruned
        threshold=0.45,
        # "fixed" or "dynamic"
        threshold_type="dynamic",
        # Ignore nodes with <5 words
        min_word_threshold=5
    )

    # Step 2: Insert it into a Markdown Generator
    md_generator = DefaultMarkdownGenerator(content_filter=prune_filter)

    # Step 3: Pass it to CrawlerRunConfig
    config = CrawlerRunConfig(
        markdown_generator=md_generator
    )

    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
            url="https://news.ycombinator.com",
            config=config
        )

        if result.success:
            # 'fit_markdown' is your pruned content, focusing on "denser" text
            print("Raw Markdown length:", len(result.markdown.raw_markdown))
            print("Fit Markdown length:", len(result.markdown.fit_markdown))
        else:
            print("Error:", result.error_message)

if __name__ == "__main__":
    asyncio.run(main())
Copy
2.2 Key Parameters
min_word_threshold (int): If a block has fewer words than this, it’s pruned.
threshold_type (str):
"fixed" → each node must exceed threshold (0–1).
"dynamic" → node scoring adjusts according to tag type, text/link density, etc.
threshold (float, default ~0.48): The base or “anchor” cutoff.
Algorithmic Factors:

Text density – Encourages blocks that have a higher ratio of text to overall content.
Link density – Penalizes sections that are mostly links.
Tag importance – e.g., an <article> or <p> might be more important than a <div>.
Structural context – If a node is deeply nested or in a suspected sidebar, it might be deprioritized.
3. BM25ContentFilter
BM25 is a classical text ranking algorithm often used in search engines. If you have a user query or rely on page metadata to derive a query, BM25 can identify which text chunks best match that query.

3.1 Usage Example
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from crawl4ai.content_filter_strategy import BM25ContentFilter
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator

async def main():
    # 1) A BM25 filter with a user query
    bm25_filter = BM25ContentFilter(
        user_query="startup fundraising tips",
        # Adjust for stricter or looser results
        bm25_threshold=1.2
    )

    # 2) Insert into a Markdown Generator
    md_generator = DefaultMarkdownGenerator(content_filter=bm25_filter)

    # 3) Pass to crawler config
    config = CrawlerRunConfig(
        markdown_generator=md_generator
    )

    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
            url="https://news.ycombinator.com",
            config=config
        )
        if result.success:
            print("Fit Markdown (BM25 query-based):")
            print(result.markdown.fit_markdown)
        else:
            print("Error:", result.error_message)

if __name__ == "__main__":
    asyncio.run(main())
Copy
3.2 Parameters
user_query (str, optional): E.g. "machine learning". If blank, the filter tries to glean a query from page metadata.
bm25_threshold (float, default 1.0):
Higher → fewer chunks but more relevant.
Lower → more inclusive.
In more advanced scenarios, you might see parameters like use_stemming, case_sensitive, or priority_tags to refine how text is tokenized or weighted.

4. Accessing the “Fit” Output
After the crawl, your “fit” content is found in result.markdown.fit_markdown.

fit_md = result.markdown.fit_markdown
fit_html = result.markdown.fit_html
Copy
If the content filter is BM25, you might see additional logic or references in fit_markdown that highlight relevant segments. If it’s Pruning, the text is typically well-cleaned but not necessarily matched to a query.

5. Code Patterns Recap
5.1 Pruning
prune_filter = PruningContentFilter(
    threshold=0.5,
    threshold_type="fixed",
    min_word_threshold=10
)
md_generator = DefaultMarkdownGenerator(content_filter=prune_filter)
config = CrawlerRunConfig(markdown_generator=md_generator)
Copy
5.2 BM25
bm25_filter = BM25ContentFilter(
    user_query="health benefits fruit",
    bm25_threshold=1.2
)
md_generator = DefaultMarkdownGenerator(content_filter=bm25_filter)
config = CrawlerRunConfig(markdown_generator=md_generator)
Copy
6. Combining with “word_count_threshold” & Exclusions
Remember you can also specify:

config = CrawlerRunConfig(
    word_count_threshold=10,
    excluded_tags=["nav", "footer", "header"],
    exclude_external_links=True,
    markdown_generator=DefaultMarkdownGenerator(
        content_filter=PruningContentFilter(threshold=0.5)
    )
)
Copy
Thus, multi-level filtering occurs:

The crawler’s excluded_tags are removed from the HTML first.
The content filter (Pruning, BM25, or custom) prunes or ranks the remaining text blocks.
The final “fit” content is generated in result.markdown.fit_markdown.
7. Custom Filters
If you need a different approach (like a specialized ML model or site-specific heuristics), you can create a new class inheriting from RelevantContentFilter and implement filter_content(html). Then inject it into your markdown generator:

from crawl4ai.content_filter_strategy import RelevantContentFilter

class MyCustomFilter(RelevantContentFilter):
    def filter_content(self, html, min_word_threshold=None):
        # parse HTML, implement custom logic
        return [block for block in ... if ... some condition...]
Copy
Steps:

Subclass RelevantContentFilter.
Implement filter_content(...).
Use it in your DefaultMarkdownGenerator(content_filter=MyCustomFilter(...)).
8. Final Thoughts
Fit Markdown is a crucial feature for:

Summaries: Quickly get the important text from a cluttered page.
Search: Combine with BM25 to produce content relevant to a query.
AI Pipelines: Filter out boilerplate so LLM-based extraction or summarization runs on denser text.
Key Points: - PruningContentFilter: Great if you just want the “meatiest” text without a user query.
- BM25ContentFilter: Perfect for query-based extraction or searching.
- Combine with excluded_tags, exclude_external_links, word_count_threshold to refine your final “fit” text.
- Fit markdown ends up in result.markdown.fit_markdown; eventually result.markdown.fit_markdown in future versions.

With these tools, you can zero in on the text that truly matters, ignoring spammy or boilerplate content, and produce a concise, relevant “fit markdown” for your AI or data pipelines. Happy pruning and searching!

Last Updated: 2025-01-01
Advanced Multi-URL Crawling with Dispatchers
Heads Up: Crawl4AI supports advanced dispatchers for parallel or throttled crawling, providing dynamic rate limiting and memory usage checks. The built-in arun_many() function uses these dispatchers to handle concurrency efficiently.

1. Introduction
When crawling many URLs:

Basic: Use arun() in a loop (simple but less efficient)
Better: Use arun_many(), which efficiently handles multiple URLs with proper concurrency control
Best: Customize dispatcher behavior for your specific needs (memory management, rate limits, etc.)
Why Dispatchers?

Adaptive: Memory-based dispatchers can pause or slow down based on system resources
Rate-limiting: Built-in rate limiting with exponential backoff for 429/503 responses
Real-time Monitoring: Live dashboard of ongoing tasks, memory usage, and performance
Flexibility: Choose between memory-adaptive or semaphore-based concurrency
2. Core Components
2.1 Rate Limiter
class RateLimiter:
    def __init__(
        # Random delay range between requests
        base_delay: Tuple[float, float] = (1.0, 3.0),

        # Maximum backoff delay
        max_delay: float = 60.0,

        # Retries before giving up
        max_retries: int = 3,

        # Status codes triggering backoff
        rate_limit_codes: List[int] = [429, 503]
    )
Copy
Here’s the revised and simplified explanation of the RateLimiter, focusing on constructor parameters and adhering to your markdown style and mkDocs guidelines.

RateLimiter Constructor Parameters
The RateLimiter is a utility that helps manage the pace of requests to avoid overloading servers or getting blocked due to rate limits. It operates internally to delay requests and handle retries but can be configured using its constructor parameters.

Parameters of the RateLimiter constructor:

1. base_delay (Tuple[float, float], default: (1.0, 3.0))
  The range for a random delay (in seconds) between consecutive requests to the same domain.

A random delay is chosen between base_delay[0] and base_delay[1] for each request.
This prevents sending requests at a predictable frequency, reducing the chances of triggering rate limits.
Example:
If base_delay = (2.0, 5.0), delays could be randomly chosen as 2.3s, 4.1s, etc.

2. max_delay (float, default: 60.0)
  The maximum allowable delay when rate-limiting errors occur.

When servers return rate-limit responses (e.g., 429 or 503), the delay increases exponentially with jitter.
The max_delay ensures the delay doesn’t grow unreasonably high, capping it at this value.
Example:
For a max_delay = 30.0, even if backoff calculations suggest a delay of 45s, it will cap at 30s.

3. max_retries (int, default: 3)
  The maximum number of retries for a request if rate-limiting errors occur.

After encountering a rate-limit response, the RateLimiter retries the request up to this number of times.
If all retries fail, the request is marked as failed, and the process continues.
Example:
If max_retries = 3, the system retries a failed request three times before giving up.

4. rate_limit_codes (List[int], default: [429, 503])
  A list of HTTP status codes that trigger the rate-limiting logic.

These status codes indicate the server is overwhelmed or actively limiting requests.
You can customize this list to include other codes based on specific server behavior.
Example:
If rate_limit_codes = [429, 503, 504], the crawler will back off on these three error codes.

How to Use the RateLimiter:

Here’s an example of initializing and using a RateLimiter in your project:

from crawl4ai import RateLimiter

# Create a RateLimiter with custom settings
rate_limiter = RateLimiter(
    base_delay=(2.0, 4.0),  # Random delay between 2-4 seconds
    max_delay=30.0,         # Cap delay at 30 seconds
    max_retries=5,          # Retry up to 5 times on rate-limiting errors
    rate_limit_codes=[429, 503]  # Handle these HTTP status codes
)

# RateLimiter will handle delays and retries internally
# No additional setup is required for its operation
Copy
The RateLimiter integrates seamlessly with dispatchers like MemoryAdaptiveDispatcher and SemaphoreDispatcher, ensuring requests are paced correctly without user intervention. Its internal mechanisms manage delays and retries to avoid overwhelming servers while maximizing efficiency.

2.2 Crawler Monitor
The CrawlerMonitor provides real-time visibility into crawling operations:

from crawl4ai import CrawlerMonitor, DisplayMode
monitor = CrawlerMonitor(
    # Maximum rows in live display
    max_visible_rows=15,

    # DETAILED or AGGREGATED view
    display_mode=DisplayMode.DETAILED
)
Copy
Display Modes:

DETAILED: Shows individual task status, memory usage, and timing
AGGREGATED: Displays summary statistics and overall progress
3. Available Dispatchers
3.1 MemoryAdaptiveDispatcher (Default)
Automatically manages concurrency based on system memory usage:

from crawl4ai.async_dispatcher import MemoryAdaptiveDispatcher

dispatcher = MemoryAdaptiveDispatcher(
    memory_threshold_percent=90.0,  # Pause if memory exceeds this
    check_interval=1.0,             # How often to check memory
    max_session_permit=10,          # Maximum concurrent tasks
    rate_limiter=RateLimiter(       # Optional rate limiting
        base_delay=(1.0, 2.0),
        max_delay=30.0,
        max_retries=2
    ),
    monitor=CrawlerMonitor(         # Optional monitoring
        max_visible_rows=15,
        display_mode=DisplayMode.DETAILED
    )
)
Copy
Constructor Parameters:

1. memory_threshold_percent (float, default: 90.0)
  Specifies the memory usage threshold (as a percentage). If system memory usage exceeds this value, the dispatcher pauses crawling to prevent system overload.

2. check_interval (float, default: 1.0)
  The interval (in seconds) at which the dispatcher checks system memory usage.

3. max_session_permit (int, default: 10)
  The maximum number of concurrent crawling tasks allowed. This ensures resource limits are respected while maintaining concurrency.

4. memory_wait_timeout (float, default: 300.0)
  Optional timeout (in seconds). If memory usage exceeds memory_threshold_percent for longer than this duration, a MemoryError is raised.

5. rate_limiter (RateLimiter, default: None)
  Optional rate-limiting logic to avoid server-side blocking (e.g., for handling 429 or 503 errors). See RateLimiter for details.

6. monitor (CrawlerMonitor, default: None)
  Optional monitoring for real-time task tracking and performance insights. See CrawlerMonitor for details.

3.2 SemaphoreDispatcher
Provides simple concurrency control with a fixed limit:

from crawl4ai.async_dispatcher import SemaphoreDispatcher

dispatcher = SemaphoreDispatcher(
    max_session_permit=20,         # Maximum concurrent tasks
    rate_limiter=RateLimiter(      # Optional rate limiting
        base_delay=(0.5, 1.0),
        max_delay=10.0
    ),
    monitor=CrawlerMonitor(        # Optional monitoring
        max_visible_rows=15,
        display_mode=DisplayMode.DETAILED
    )
)
Copy
Constructor Parameters:

1. max_session_permit (int, default: 20)
  The maximum number of concurrent crawling tasks allowed, irrespective of semaphore slots.

2. rate_limiter (RateLimiter, default: None)
  Optional rate-limiting logic to avoid overwhelming servers. See RateLimiter for details.

3. monitor (CrawlerMonitor, default: None)
  Optional monitoring for tracking task progress and resource usage. See CrawlerMonitor for details.

4. Usage Examples
4.1 Batch Processing (Default)
async def crawl_batch():
    browser_config = BrowserConfig(headless=True, verbose=False)
    run_config = CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS,
        stream=False  # Default: get all results at once
    )

    dispatcher = MemoryAdaptiveDispatcher(
        memory_threshold_percent=70.0,
        check_interval=1.0,
        max_session_permit=10,
        monitor=CrawlerMonitor(
            display_mode=DisplayMode.DETAILED
        )
    )

    async with AsyncWebCrawler(config=browser_config) as crawler:
        # Get all results at once
        results = await crawler.arun_many(
            urls=urls,
            config=run_config,
            dispatcher=dispatcher
        )

        # Process all results after completion
        for result in results:
            if result.success:
                await process_result(result)
            else:
                print(f"Failed to crawl {result.url}: {result.error_message}")
Copy
Review:
- Purpose: Executes a batch crawl with all URLs processed together after crawling is complete.
- Dispatcher: Uses MemoryAdaptiveDispatcher to manage concurrency and system memory.
- Stream: Disabled (stream=False), so all results are collected at once for post-processing.
- Best Use Case: When you need to analyze results in bulk rather than individually during the crawl.

4.2 Streaming Mode
async def crawl_streaming():
    browser_config = BrowserConfig(headless=True, verbose=False)
    run_config = CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS,
        stream=True  # Enable streaming mode
    )

    dispatcher = MemoryAdaptiveDispatcher(
        memory_threshold_percent=70.0,
        check_interval=1.0,
        max_session_permit=10,
        monitor=CrawlerMonitor(
            display_mode=DisplayMode.DETAILED
        )
    )

    async with AsyncWebCrawler(config=browser_config) as crawler:
        # Process results as they become available
        async for result in await crawler.arun_many(
            urls=urls,
            config=run_config,
            dispatcher=dispatcher
        ):
            if result.success:
                # Process each result immediately
                await process_result(result)
            else:
                print(f"Failed to crawl {result.url}: {result.error_message}")
Copy
Review:
- Purpose: Enables streaming to process results as soon as they’re available.
- Dispatcher: Uses MemoryAdaptiveDispatcher for concurrency and memory management.
- Stream: Enabled (stream=True), allowing real-time processing during crawling.
- Best Use Case: When you need to act on results immediately, such as for real-time analytics or progressive data storage.

4.3 Semaphore-based Crawling
async def crawl_with_semaphore(urls):
    browser_config = BrowserConfig(headless=True, verbose=False)
    run_config = CrawlerRunConfig(cache_mode=CacheMode.BYPASS)

    dispatcher = SemaphoreDispatcher(
        semaphore_count=5,
        rate_limiter=RateLimiter(
            base_delay=(0.5, 1.0),
            max_delay=10.0
        ),
        monitor=CrawlerMonitor(
            max_visible_rows=15,
            display_mode=DisplayMode.DETAILED
        )
    )

    async with AsyncWebCrawler(config=browser_config) as crawler:
        results = await crawler.arun_many(
            urls,
            config=run_config,
            dispatcher=dispatcher
        )
        return results
Copy
Review:
- Purpose: Uses SemaphoreDispatcher to limit concurrency with a fixed number of slots.
- Dispatcher: Configured with a semaphore to control parallel crawling tasks.
- Rate Limiter: Prevents servers from being overwhelmed by pacing requests.
- Best Use Case: When you want precise control over the number of concurrent requests, independent of system memory.

4.4 Robots.txt Consideration
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode

async def main():
    urls = [
        "https://example1.com",
        "https://example2.com",
        "https://example3.com"
    ]

    config = CrawlerRunConfig(
        cache_mode=CacheMode.ENABLED,
        check_robots_txt=True,  # Will respect robots.txt for each URL
        semaphore_count=3      # Max concurrent requests
    )

    async with AsyncWebCrawler() as crawler:
        async for result in crawler.arun_many(urls, config=config):
            if result.success:
                print(f"Successfully crawled {result.url}")
            elif result.status_code == 403 and "robots.txt" in result.error_message:
                print(f"Skipped {result.url} - blocked by robots.txt")
            else:
                print(f"Failed to crawl {result.url}: {result.error_message}")

if __name__ == "__main__":
    asyncio.run(main())
Copy
Review:
- Purpose: Ensures compliance with robots.txt rules for ethical and legal web crawling.
- Configuration: Set check_robots_txt=True to validate each URL against robots.txt before crawling.
- Dispatcher: Handles requests with concurrency limits (semaphore_count=3).
- Best Use Case: When crawling websites that strictly enforce robots.txt policies or for responsible crawling practices.

5. Dispatch Results
Each crawl result includes dispatch information:

@dataclass
class DispatchResult:
    task_id: str
    memory_usage: float
    peak_memory: float
    start_time: datetime
    end_time: datetime
    error_message: str = ""
Copy
Access via result.dispatch_result:

for result in results:
    if result.success:
        dr = result.dispatch_result
        print(f"URL: {result.url}")
        print(f"Memory: {dr.memory_usage:.1f}MB")
        print(f"Duration: {dr.end_time - dr.start_time}")
Copy
6. Summary
1. Two Dispatcher Types:

MemoryAdaptiveDispatcher (default): Dynamic concurrency based on memory
SemaphoreDispatcher: Fixed concurrency limit
2. Optional Components:

RateLimiter: Smart request pacing and backoff
CrawlerMonitor: Real-time progress visualization
3. Key Benefits:

Automatic memory management
Built-in rate limiting
Live progress monitoring
Flexible concurrency control
Choose the dispatcher that best fits your needs:

MemoryAdaptiveDispatcher: For large crawls or limited resources
SemaphoreDispatcher: For simple, fixed-concurrency scenarios
Site