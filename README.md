# Crawl4AI Web Crawler

A Flask-based web application for crawling websites using the Crawl4AI library. This application allows you to:

-   Enter a homepage URL and crawl up to 300 pages from that website
-   View real-time crawling progress
-   Browse and search crawled pages
-   Download results as CSV
-   Save crawl history in browser storage

## Features

-   **Multi-URL Crawling**: Start with a homepage and crawl up to 300 linked pages
-   **Real-time Progress**: Monitor the crawling process with a live progress indicator
-   **Results Table**: View crawled pages in a searchable, sortable table
-   **CSV Export**: Download crawled data as a CSV file
-   **Crawl History**: Access previous crawls stored in browser localStorage
-   **Responsive Design**: Works on desktop and mobile devices

## Installation

1. Clone the repository:

    ```
    git clone https://github.com/chirag127/Crawl4AI-Income-stream-surfers.git
    cd Crawl4AI-Income-stream-surfers
    ```

2. Create a virtual environment:

    ```
    python -m venv venv
    venv\Scripts\activate  # Windows
    source venv/bin/activate  # Linux/Mac
    ```

3. Install dependencies:

    ```
    pip install -r requirements.txt
    ```

4. Install browser dependencies for Crawl4AI:

    ```
    python -m playwright install --with-deps chromium
    ```

5. Run the application:

    ```
    python app.py
    ```

6. Open your browser and navigate to:
    ```
    http://127.0.0.1:5000/
    ```

## Usage

1. Enter a website URL in the form (e.g., https://example.com)
2. Set the maximum number of pages to crawl (1-300)
3. Click "Start Crawling"
4. Monitor the progress in real-time
5. View results in the table below
6. Download the data as CSV when complete
7. Access previous crawls from the history section

## Technical Details

-   **Backend**: Flask (Python)
-   **Frontend**: HTML, CSS, JavaScript
-   **Crawling Engine**: Crawl4AI
-   **Data Processing**: Pandas
-   **Storage**: Browser localStorage

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

<a href="https://github.com/unclecode/crawl4ai">
  <img src="https://img.shields.io/badge/Powered%20by-Crawl4AI-blue?style=flat-square" alt="Powered by Crawl4AI"/>
</a>

This project uses [Crawl4AI](https://github.com/unclecode/crawl4ai) for web data extraction.

## Author

Created by [Chirag Singhal](https://github.com/chirag127)
