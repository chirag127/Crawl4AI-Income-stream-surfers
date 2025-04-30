"""
Flask application for multi-URL crawling using Crawl4AI.
This application provides a web interface for crawling websites,
viewing results, and downloading data.
"""

import os
import asyncio
import uuid
from urllib.parse import urlparse
from datetime import datetime
from flask import Flask, render_template, request, jsonify, send_file

from crawler import start_crawling

app = Flask(__name__)

# Store active crawlers in memory
active_crawlers = {}

@app.route('/')
def index():
    """Render the home page."""
    return render_template('index.html')

@app.route('/api/crawl', methods=['POST'])
async def crawl():
    """
    Start a new crawling job.

    Expected JSON payload:
    {
        "url": "https://example.com",
        "max_pages": 100
    }

    Returns:
        JSON with crawler_id for tracking progress
    """
    data = request.json
    url = data.get('url')
    max_pages = int(data.get('max_pages', 100))

    # Validate URL
    if not url or not url.startswith(('http://', 'https://')):
        return jsonify({'error': 'Invalid URL. Please provide a valid URL starting with http:// or https://'}), 400

    # Validate max_pages
    if max_pages < 1 or max_pages > 300:
        return jsonify({'error': 'Invalid page count. Please provide a number between 1 and 300'}), 400

    # Generate a unique ID for this crawling job
    crawler_id = str(uuid.uuid4())

    # Start crawling
    crawler = await start_crawling(url, max_pages)

    # Store crawler in memory
    active_crawlers[crawler_id] = crawler

    return jsonify({
        'crawler_id': crawler_id,
        'status': crawler.status,
        'base_url': crawler.base_url,
        'max_pages': crawler.max_pages,
        'folder_name': crawler.folder_name
    })

@app.route('/api/progress/<crawler_id>', methods=['GET'])
def get_progress(crawler_id):
    """
    Get the progress of a crawling job.

    Args:
        crawler_id: The ID of the crawler to check

    Returns:
        JSON with progress information
    """
    crawler = active_crawlers.get(crawler_id)
    if not crawler:
        return jsonify({'error': 'Crawler not found'}), 404

    return jsonify(crawler.get_progress())

@app.route('/api/results/<crawler_id>', methods=['GET'])
def get_results(crawler_id):
    """
    Get the results of a completed crawling job.

    Args:
        crawler_id: The ID of the crawler to get results from

    Returns:
        JSON with results information
    """
    crawler = active_crawlers.get(crawler_id)
    if not crawler:
        return jsonify({'error': 'Crawler not found'}), 404

    return jsonify(crawler.get_results())

@app.route('/api/download/<crawler_id>', methods=['GET'])
def download_results(crawler_id):
    """
    Download the results of a crawling job as CSV.

    Args:
        crawler_id: The ID of the crawler to download results from

    Returns:
        CSV file download
    """
    crawler = active_crawlers.get(crawler_id)
    if not crawler:
        return jsonify({'error': 'Crawler not found'}), 404

    # Check if results CSV exists
    csv_path = os.path.join(crawler.folder_name, 'results.csv')
    if not os.path.exists(csv_path):
        return jsonify({'error': 'Results file not found'}), 404

    # Generate a filename for download
    domain = urlparse(crawler.base_url).netloc.replace('.', '_')
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"{domain}_crawl_results_{timestamp}.csv"

    return send_file(
        csv_path,
        as_attachment=True,
        download_name=filename,
        mimetype='text/csv'
    )

@app.route('/api/download/markdown/<crawler_id>', methods=['GET'])
def download_markdown(crawler_id):
    """
    Download all markdown files as a zip archive.

    Args:
        crawler_id: The ID of the crawler to download markdown files from

    Returns:
        ZIP file download
    """
    import zipfile
    from io import BytesIO

    crawler = active_crawlers.get(crawler_id)
    if not crawler:
        return jsonify({'error': 'Crawler not found'}), 404

    # Create a zip file in memory
    memory_file = BytesIO()
    with zipfile.ZipFile(memory_file, 'w', zipfile.ZIP_DEFLATED) as zf:
        # Add all markdown files from the crawler's folder
        for root, _, files in os.walk(crawler.folder_name):
            for file in files:
                if file.endswith('.md'):
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, crawler.folder_name)
                    zf.write(file_path, arcname)

    # Reset file pointer
    memory_file.seek(0)

    # Generate a filename for download
    domain = urlparse(crawler.base_url).netloc.replace('.', '_')
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"{domain}_markdown_files_{timestamp}.zip"

    return send_file(
        memory_file,
        as_attachment=True,
        download_name=filename,
        mimetype='application/zip'
    )

if __name__ == '__main__':
    # Run the Flask app with asyncio support
    import asyncio
    from aioflask import run_app

    # For Windows compatibility
    if asyncio.get_event_loop_policy()._loop_factory is asyncio.SelectorEventLoop:
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    run_app(app, debug=True, port=5000)
