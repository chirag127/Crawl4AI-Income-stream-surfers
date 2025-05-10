---
url: https://docs.crawl4ai.com/core/examples
title: https://docs.crawl4ai.com/core/examples
date: 2025-04-30T16:19:48.157249
depth: 1
---

[ unclecode/crawl4ai 41.7k 3.8k ](https://github.com/unclecode/crawl4ai)
# Code Examples
This page provides a comprehensive list of example scripts that demonstrate various features and capabilities of Crawl4AI. Each example is designed to showcase specific functionality, making it easier for you to understand how to implement these features in your own projects.
## Getting Started Examples
Example | Description | Link  
---|---|---  
Hello World | A simple introductory example demonstrating basic usage of AsyncWebCrawler with JavaScript execution and content filtering.  
Quickstart | A comprehensive collection of examples showcasing various features including basic crawling, content cleaning, link analysis, JavaScript execution, CSS selectors, media handling, custom hooks, proxy configuration, screenshots, and multiple extraction strategies.  
Quickstart Set 1 | Basic examples for getting started with Crawl4AI.  
Quickstart Set 2 | More advanced examples for working with Crawl4AI.  
## Browser & Crawling Features
Example | Description | Link  
---|---|---  
Built-in Browser | Demonstrates how to use the built-in browser capabilities.  
Browser Optimization | Focuses on browser performance optimization techniques.  
arun vs arun_many | Compares the `arun` and `arun_many` methods for single vs. multiple URL crawling.  
Multiple URLs | Shows how to crawl multiple URLs asynchronously.  
Page Interaction | Guide on interacting with dynamic elements through clicks.  
Crawler Monitor | Shows how to monitor the crawler's activities and status.  
Full Page Screenshot & PDF | Guide on capturing full-page screenshots and PDFs from massive webpages.  
## Advanced Crawling & Deep Crawling
Example | Description | Link  
---|---|---  
Deep Crawling | An extensive tutorial on deep crawling capabilities, demonstrating BFS and BestFirst strategies, stream vs. non-stream execution, filters, scorers, and advanced configurations.  
Dispatcher | Shows how to use the crawl dispatcher for advanced workload management.  
Storage State | Tutorial on managing browser storage state for persistence.  
Network Console Capture | Demonstrates how to capture and analyze network requests and console logs.  
## Extraction Strategies
Example | Description | Link  
---|---|---  
Extraction Strategies | Demonstrates different extraction strategies with various input formats (markdown, HTML, fit_markdown) and JSON-based extractors (CSS and XPath).  
Scraping Strategies | Compares the performance of different scraping strategies.  
LLM Extraction | Demonstrates LLM-based extraction specifically for OpenAI pricing data.  
LLM Markdown | Shows how to use LLMs to generate markdown from crawled content.  
Summarize Page | Shows how to summarize web page content.  
## E-commerce & Specialized Crawling
Example | Description | Link  
---|---|---  
Amazon Product Extraction | Demonstrates how to extract structured product data from Amazon search results using CSS selectors.  
Amazon with Hooks | Shows how to use hooks with Amazon product extraction.  
Amazon with JavaScript | Demonstrates using custom JavaScript for Amazon product extraction.  
Crypto Analysis | Demonstrates how to crawl and analyze cryptocurrency data.  
SERP API | Demonstrates using Crawl4AI with search engine result pages.  
## Customization & Security
Example | Description | Link  
---|---|---  
Hooks | Illustrates how to use hooks at different stages of the crawling process for advanced customization.  
Identity-Based Browsing | Illustrates identity-based browsing configurations for authentic browsing experiences.  
Proxy Rotation | Shows how to use proxy rotation for web scraping and avoiding IP blocks.  
SSL Certificate | Illustrates SSL certificate handling and verification.  
Language Support | Shows how to handle different languages during crawling.  
Geolocation | Demonstrates how to use geolocation features.  
## Docker & Deployment
Example | Description | Link  
---|---|---  
Docker Config | Demonstrates how to create and use Docker configuration objects.  
Docker Basic | A test suite for Docker deployment, showcasing various functionalities through the Docker API.  
Docker REST API | Shows how to interact with Crawl4AI Docker using REST API calls.  
Docker SDK | Demonstrates using the Python SDK for Crawl4AI Docker.  
## Application Examples
Example | Description | Link  
---|---|---  
Research Assistant | Demonstrates how to build a research assistant using Crawl4AI.  
REST Call | Shows how to make REST API calls with Crawl4AI.  
Chainlit Integration | Shows how to integrate Crawl4AI with Chainlit.  
Crawl4AI vs FireCrawl | Compares Crawl4AI with the FireCrawl library.  
## Content Generation & Markdown
Example | Description | Link  
---|---|---  
Content Source | Demonstrates how to work with different content sources in markdown generation.  
Content Source (Short) | A simplified version of content source usage.  
Built-in Browser Guide | Guide for using the built-in browser capabilities.  
## Running the Examples
To run any of these examples, you'll need to have Crawl4AI installed:
```
pip install crawl4ai
Copy
```

Then, you can run an example script like this:
```
python -m docs.examples.hello_world
Copy
```

For examples that require additional dependencies or environment variables, refer to the comments at the top of each file.
Some examples may require: - API keys (for LLM-based examples) - Docker setup (for Docker-related examples) - Additional dependencies (specified in the example files)
## Contributing New Examples
If you've created an interesting example that demonstrates a unique use case or feature of Crawl4AI, we encourage you to contribute it to our examples collection. Please see our [contribution guidelines](https://github.com/unclecode/crawl4ai/blob/main/CONTRIBUTORS.md) for more information.
##### Search
xClose
Type to start searching
[ Ask AI ](https://docs.crawl4ai.com/core/ask-ai/ "Ask Crawl4AI Assistant")

