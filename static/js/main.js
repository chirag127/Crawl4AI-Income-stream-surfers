/**
 * Main.js - Main JavaScript functionality for the Crawl4AI Web Crawler
 */

// Global variables
let currentJobId = null;
let statusInterval = null;
let crawlResults = [];

// DOM elements
const crawlForm = document.getElementById('crawlForm');
const crawlStatus = document.getElementById('crawlStatus');
const resultsCard = document.getElementById('resultsCard');
const jobIdElement = document.getElementById('jobId');
const crawlUrlElement = document.getElementById('crawlUrl');
const statusTextElement = document.getElementById('statusText');
const progressTextElement = document.getElementById('progressText');
const progressBarElement = document.getElementById('progressBar');
const downloadBtn = document.getElementById('downloadBtn');
const viewResultsBtn = document.getElementById('viewResultsBtn');
const resultsTable = document.getElementById('resultsTable');
const historyTable = document.getElementById('historyTable');
const clearHistoryBtn = document.getElementById('clearHistoryBtn');

// Event listeners
document.addEventListener('DOMContentLoaded', () => {
    loadHistory();
    
    crawlForm.addEventListener('submit', startCrawl);
    viewResultsBtn.addEventListener('click', viewResults);
    downloadBtn.addEventListener('click', downloadResults);
    clearHistoryBtn.addEventListener('click', clearHistory);
});

// Start a new crawl
async function startCrawl(event) {
    event.preventDefault();
    
    const url = document.getElementById('url').value;
    const maxPages = parseInt(document.getElementById('maxPages').value);
    
    if (!url) {
        alert('Please enter a valid URL');
        return;
    }
    
    try {
        const response = await fetch('/api/crawl', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ url, max_pages: maxPages })
        });
        
        const data = await response.json();
        
        if (response.ok) {
            currentJobId = data.job_id;
            
            // Update UI
            jobIdElement.textContent = currentJobId;
            crawlUrlElement.textContent = url;
            statusTextElement.textContent = 'in_progress';
            progressTextElement.textContent = '0/' + maxPages;
            progressBarElement.style.width = '0%';
            
            crawlStatus.classList.remove('d-none');
            downloadBtn.classList.add('d-none');
            resultsCard.classList.add('d-none');
            
            // Start polling for status updates
            if (statusInterval) {
                clearInterval(statusInterval);
            }
            statusInterval = setInterval(updateStatus, 2000);
            
            // Add to history
            addToHistory({
                id: currentJobId,
                url: url,
                maxPages: maxPages,
                startTime: new Date().toISOString(),
                status: 'in_progress',
                crawledPages: 0
            });
        } else {
            alert('Error: ' + (data.error || 'Failed to start crawl'));
        }
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred. Please try again.');
    }
}

// Update crawl status
async function updateStatus() {
    if (!currentJobId) return;
    
    try {
        const response = await fetch(`/api/status/${currentJobId}`);
        const data = await response.json();
        
        if (response.ok) {
            // Update progress
            const progress = data.crawled_pages;
            const total = data.max_pages;
            const percentage = Math.round((progress / total) * 100);
            
            statusTextElement.textContent = data.status;
            progressTextElement.textContent = `${progress}/${total}`;
            progressBarElement.style.width = `${percentage}%`;
            
            // Update history
            updateHistoryItem(currentJobId, {
                status: data.status,
                crawledPages: progress
            });
            
            // If completed, stop polling and enable download
            if (data.status === 'completed') {
                clearInterval(statusInterval);
                downloadBtn.classList.remove('d-none');
                
                // Update history
                updateHistoryItem(currentJobId, {
                    status: 'completed',
                    endTime: new Date().toISOString(),
                    crawledPages: progress
                });
            }
        } else {
            console.error('Error:', data.error);
        }
    } catch (error) {
        console.error('Error:', error);
    }
}

// View crawl results
async function viewResults() {
    if (!currentJobId) return;
    
    try {
        const response = await fetch(`/api/results/${currentJobId}`);
        const data = await response.json();
        
        if (response.ok) {
            crawlResults = data.results;
            
            // Clear previous results
            resultsTable.innerHTML = '';
            
            // Populate results table
            crawlResults.forEach(result => {
                const row = document.createElement('tr');
                
                const urlCell = document.createElement('td');
                const urlLink = document.createElement('a');
                urlLink.href = result.url;
                urlLink.textContent = result.url;
                urlLink.target = '_blank';
                urlCell.appendChild(urlLink);
                
                const titleCell = document.createElement('td');
                titleCell.textContent = result.title;
                
                const statusCell = document.createElement('td');
                statusCell.textContent = result.status_code;
                
                const contentCell = document.createElement('td');
                contentCell.textContent = result.content ? result.content.length : 0;
                
                row.appendChild(urlCell);
                row.appendChild(titleCell);
                row.appendChild(statusCell);
                row.appendChild(contentCell);
                
                resultsTable.appendChild(row);
            });
            
            resultsCard.classList.remove('d-none');
        } else {
            alert('Error: ' + (data.error || 'Failed to fetch results'));
        }
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred. Please try again.');
    }
}

// Download results as CSV
function downloadResults() {
    if (!currentJobId) return;
    
    window.location.href = `/api/download/${currentJobId}`;
}
