import os
import json
import uuid
import threading
from flask import Flask, render_template, request, jsonify, send_file, session
from utils.crawler import CrawlJob

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Global dictionary to store active crawl jobs
crawl_jobs = {}

@app.route('/')
def index():
    """
    Render the home page.
    """
    return render_template('index.html')

@app.route('/api/crawl', methods=['POST'])
def start_crawl():
    """
    Start a new crawl job.
    
    Expects JSON with:
    - url: The starting URL to crawl
    - max_pages: Maximum number of pages to crawl (optional, default: 300)
    
    Returns:
    - job_id: Unique identifier for the job
    - status: Initial status
    - url: The starting URL
    - max_pages: Maximum number of pages
    """
    data = request.json
    url = data.get('url')
    
    if not url:
        return jsonify({'error': 'URL is required'}), 400
    
    # Create a new crawl job
    job_id = str(uuid.uuid4())
    max_pages = min(int(data.get('max_pages', 300)), 300)  # Limit to 300 pages
    
    # Initialize the job
    job = CrawlJob(job_id, url, max_pages)
    crawl_jobs[job_id] = job
    
    # Start the crawl in a background thread
    thread = threading.Thread(target=job.start_crawl)
    thread.daemon = True
    thread.start()
    
    # Return the job ID and initial status
    return jsonify({
        'job_id': job_id,
        'status': 'started',
        'url': url,
        'max_pages': max_pages
    })

@app.route('/api/status/<job_id>', methods=['GET'])
def get_status(job_id):
    """
    Get the status of a crawl job.
    
    Parameters:
    - job_id: Unique identifier for the job
    
    Returns:
    - Status information including progress
    """
    job = crawl_jobs.get(job_id)
    
    if not job:
        return jsonify({'error': 'Job not found'}), 404
    
    return jsonify(job.get_status())

@app.route('/api/results/<job_id>', methods=['GET'])
def get_results(job_id):
    """
    Get the results of a crawl job.
    
    Parameters:
    - job_id: Unique identifier for the job
    
    Returns:
    - Results and metadata
    """
    job = crawl_jobs.get(job_id)
    
    if not job:
        return jsonify({'error': 'Job not found'}), 404
    
    return jsonify(job.get_results())

@app.route('/api/download/<job_id>', methods=['GET'])
def download_results(job_id):
    """
    Download the results of a crawl job as a CSV file.
    
    Parameters:
    - job_id: Unique identifier for the job
    
    Returns:
    - CSV file for download
    """
    job = crawl_jobs.get(job_id)
    
    if not job:
        return jsonify({'error': 'Job not found'}), 404
    
    # Generate CSV file
    csv_file = job.to_csv()
    
    # Return the file for download
    return send_file(
        csv_file,
        as_attachment=True,
        download_name=f'crawl_{job_id}.csv',
        mimetype='text/csv'
    )

@app.route('/api/history', methods=['GET'])
def get_history():
    """
    Get the list of crawl jobs.
    
    Note: This is a placeholder. Actual history is managed client-side with localStorage.
    
    Returns:
    - List of active crawl jobs
    """
    # Return a list of active job IDs
    # Note: Full history is managed client-side with localStorage
    active_jobs = [
        {
            'job_id': job_id,
            'url': job.url,
            'status': job.status,
            'crawled_pages': job.crawled_pages,
            'max_pages': job.max_pages
        }
        for job_id, job in crawl_jobs.items()
    ]
    
    return jsonify({'active_jobs': active_jobs})

if __name__ == '__main__':
    app.run(debug=True)
