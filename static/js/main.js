/**
 * Main JavaScript for Crawl4AI Web Crawler
 * Handles form submission, progress tracking, and result display
 */

// Global variables
let activeCrawlerId = null;
let progressInterval = null;
let startTime = null;
let crawlHistory = [];

// DOM elements
const crawlForm = document.getElementById('crawlForm');
const startCrawlBtn = document.getElementById('startCrawlBtn');
const progressSection = document.getElementById('progressSection');
const progressBar = document.getElementById('progressBar');
const progressStats = document.getElementById('progressStats');
const progressTime = document.getElementById('progressTime');
const progressStatus = document.getElementById('progressStatus');
const resultsSection = document.getElementById('resultsSection');
const resultsTableBody = document.getElementById('resultsTableBody');
const resultsSummary = document.getElementById('resultsSummary');
const downloadCsvBtn = document.getElementById('downloadCsvBtn');
const downloadMarkdownBtn = document.getElementById('downloadMarkdownBtn');
const searchResults = document.getElementById('searchResults');
const clearSearch = document.getElementById('clearSearch');
const historyEmpty = document.getElementById('historyEmpty');
const historyList = document.getElementById('historyList');

// Initialize the application
document.addEventListener('DOMContentLoaded', () => {
    // Load crawl history from localStorage
    loadCrawlHistory();
    
    // Set up event listeners
    crawlForm.addEventListener('submit', handleFormSubmit);
    downloadCsvBtn.addEventListener('click', handleDownloadCsv);
    downloadMarkdownBtn.addEventListener('click', handleDownloadMarkdown);
    searchResults.addEventListener('input', filterResults);
    clearSearch.addEventListener('click', clearSearchResults);
});

/**
 * Handle form submission to start crawling
 * @param {Event} event - Form submit event
 */
async function handleFormSubmit(event) {
    event.preventDefault();
    
    // Get form data
    const url = document.getElementById('url').value;
    const maxPages = parseInt(document.getElementById('maxPages').value);
    
    // Validate input
    if (!url || !url.startsWith('http')) {
        alert('Please enter a valid URL starting with http:// or https://');
        return;
    }
    
    if (isNaN(maxPages) || maxPages < 1 || maxPages > 300) {
        alert('Please enter a valid number of pages between 1 and 300');
        return;
    }
    
    // Disable form and show progress section
    startCrawlBtn.disabled = true;
    startCrawlBtn.innerHTML = '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Starting...';
    progressSection.classList.remove('d-none');
    resultsSection.classList.add('d-none');
    
    try {
        // Start crawling
        const response = await fetch('/api/crawl', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ url, max_pages: maxPages })
        });
        
        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.error || 'Failed to start crawling');
        }
        
        const data = await response.json();
        activeCrawlerId = data.crawler_id;
        startTime = new Date();
        
        // Start tracking progress
        trackProgress();
        
        // Add to history
        addToCrawlHistory({
            id: activeCrawlerId,
            url: url,
            maxPages: maxPages,
            timestamp: new Date().toISOString(),
            domain: new URL(url).hostname
        });
        
    } catch (error) {
        console.error('Error starting crawl:', error);
        alert(`Error: ${error.message}`);
        resetForm();
    }
}

/**
 * Track crawling progress
 */
function trackProgress() {
    // Clear any existing interval
    if (progressInterval) {
        clearInterval(progressInterval);
    }
    
    // Update progress immediately
    updateProgress();
    
    // Set interval to update progress every 2 seconds
    progressInterval = setInterval(updateProgress, 2000);
}

/**
 * Update progress display
 */
async function updateProgress() {
    if (!activeCrawlerId) return;
    
    try {
        const response = await fetch(`/api/progress/${activeCrawlerId}`);
        
        if (!response.ok) {
            throw new Error('Failed to get progress');
        }
        
        const data = await response.json();
        
        // Update progress bar
        const percent = data.percent || 0;
        progressBar.style.width = `${percent}%`;
        progressBar.setAttribute('aria-valuenow', percent);
        progressBar.textContent = `${percent}%`;
        
        // Update stats
        progressStats.textContent = `Crawled: ${data.progress} / ${data.total} pages`;
        
        // Update elapsed time
        if (startTime) {
            const elapsed = Math.floor((new Date() - startTime) / 1000);
            const minutes = Math.floor(elapsed / 60);
            const seconds = elapsed % 60;
            progressTime.textContent = `Time: ${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
        }
        
        // Update status message
        let statusMessage = 'Crawling in progress...';
        
        switch (data.status) {
            case 'idle':
                statusMessage = 'Initializing...';
                break;
            case 'extracting_links':
                statusMessage = 'Extracting links from homepage...';
                break;
            case 'crawling':
                statusMessage = `Crawling pages (${data.progress} of ${data.total})...`;
                break;
            case 'completed':
                statusMessage = 'Crawling completed!';
                clearInterval(progressInterval);
                loadResults();
                break;
            case 'error':
                statusMessage = 'Error occurred during crawling.';
                clearInterval(progressInterval);
                break;
        }
        
        progressStatus.textContent = statusMessage;
        
    } catch (error) {
        console.error('Error updating progress:', error);
        progressStatus.textContent = 'Error updating progress.';
    }
}

/**
 * Load crawling results
 */
async function loadResults() {
    if (!activeCrawlerId) return;
    
    try {
        const response = await fetch(`/api/results/${activeCrawlerId}`);
        
        if (!response.ok) {
            throw new Error('Failed to get results');
        }
        
        const data = await response.json();
        
        // Show results section
        resultsSection.classList.remove('d-none');
        
        // Clear existing results
        resultsTableBody.innerHTML = '';
        
        // Add results to table
        data.results.forEach(result => {
            const row = document.createElement('tr');
            
            // Set row class based on status
            if (result.status === 'error') {
                row.classList.add('table-danger');
            }
            
            row.innerHTML = `
                <td class="truncate" title="${result.title}">${result.title || 'N/A'}</td>
                <td class="truncate" title="${result.url}">
                    <a href="${result.url}" target="_blank">${result.url}</a>
                </td>
                <td>${result.word_count}</td>
                <td>
                    ${result.status === 'success' 
                        ? '<span class="badge bg-success">Success</span>' 
                        : `<span class="badge bg-danger" title="${result.error_message || ''}">Error</span>`}
                </td>
            `;
            
            resultsTableBody.appendChild(row);
        });
        
        // Update summary
        resultsSummary.textContent = `Total: ${data.results.length} pages (${data.results.filter(r => r.status === 'success').length} successful)`;
        
        // Enable download buttons
        downloadCsvBtn.disabled = false;
        downloadMarkdownBtn.disabled = false;
        
        // Reset form
        resetForm();
        
        // Update history item with completion status
        updateCrawlHistoryStatus(activeCrawlerId, 'completed', data.results.length);
        
    } catch (error) {
        console.error('Error loading results:', error);
        alert(`Error: ${error.message}`);
    }
}

/**
 * Handle CSV download
 */
function handleDownloadCsv() {
    if (!activeCrawlerId) return;
    
    window.location.href = `/api/download/${activeCrawlerId}`;
}

/**
 * Handle markdown files download
 */
function handleDownloadMarkdown() {
    if (!activeCrawlerId) return;
    
    window.location.href = `/api/download/markdown/${activeCrawlerId}`;
}

/**
 * Filter results table based on search input
 */
function filterResults() {
    const searchTerm = searchResults.value.toLowerCase();
    const rows = resultsTableBody.querySelectorAll('tr');
    
    rows.forEach(row => {
        const text = row.textContent.toLowerCase();
        if (text.includes(searchTerm)) {
            row.style.display = '';
        } else {
            row.style.display = 'none';
        }
    });
}

/**
 * Clear search results
 */
function clearSearchResults() {
    searchResults.value = '';
    filterResults();
}

/**
 * Reset form and UI state
 */
function resetForm() {
    startCrawlBtn.disabled = false;
    startCrawlBtn.innerHTML = '<i class="fas fa-play me-2"></i>Start Crawling';
}

/**
 * Load crawl history from localStorage
 */
function loadCrawlHistory() {
    try {
        const savedHistory = localStorage.getItem('crawlHistory');
        if (savedHistory) {
            crawlHistory = JSON.parse(savedHistory);
            renderCrawlHistory();
        }
    } catch (error) {
        console.error('Error loading crawl history:', error);
        crawlHistory = [];
    }
}

/**
 * Save crawl history to localStorage
 */
function saveCrawlHistory() {
    try {
        localStorage.setItem('crawlHistory', JSON.stringify(crawlHistory));
    } catch (error) {
        console.error('Error saving crawl history:', error);
    }
}

/**
 * Add a crawl to history
 * @param {Object} crawl - Crawl data to add to history
 */
function addToCrawlHistory(crawl) {
    // Add to beginning of array
    crawlHistory.unshift(crawl);
    
    // Limit history to 10 items
    if (crawlHistory.length > 10) {
        crawlHistory = crawlHistory.slice(0, 10);
    }
    
    // Save and render
    saveCrawlHistory();
    renderCrawlHistory();
}

/**
 * Update a crawl history item's status
 * @param {string} id - Crawler ID
 * @param {string} status - New status
 * @param {number} pageCount - Number of pages crawled
 */
function updateCrawlHistoryStatus(id, status, pageCount) {
    const index = crawlHistory.findIndex(item => item.id === id);
    if (index !== -1) {
        crawlHistory[index].status = status;
        crawlHistory[index].pageCount = pageCount;
        saveCrawlHistory();
        renderCrawlHistory();
    }
}

/**
 * Render crawl history in the UI
 */
function renderCrawlHistory() {
    if (crawlHistory.length === 0) {
        historyEmpty.classList.remove('d-none');
        historyList.classList.add('d-none');
        return;
    }
    
    historyEmpty.classList.add('d-none');
    historyList.classList.remove('d-none');
    
    // Clear existing history
    historyList.innerHTML = '';
    
    // Add history items
    crawlHistory.forEach(item => {
        const date = new Date(item.timestamp);
        const formattedDate = date.toLocaleDateString() + ' ' + date.toLocaleTimeString();
        
        const historyItem = document.createElement('div');
        historyItem.className = 'list-group-item history-item';
        
        historyItem.innerHTML = `
            <div class="d-flex w-100 justify-content-between">
                <h5 class="mb-1">${item.domain}</h5>
                <small>${formattedDate}</small>
            </div>
            <p class="mb-1 truncate" title="${item.url}">${item.url}</p>
            <div class="d-flex justify-content-between align-items-center">
                <small>
                    <span class="badge bg-primary">${item.maxPages} pages max</span>
                    ${item.pageCount ? `<span class="badge bg-info">${item.pageCount} pages crawled</span>` : ''}
                    ${item.status === 'completed' ? '<span class="badge bg-success">Completed</span>' : ''}
                </small>
                <button class="btn btn-sm btn-outline-primary load-history" data-id="${item.id}">
                    Load Results
                </button>
            </div>
        `;
        
        // Add event listener to load button
        const loadButton = historyItem.querySelector('.load-history');
        loadButton.addEventListener('click', () => {
            activeCrawlerId = item.id;
            loadResults();
        });
        
        historyList.appendChild(historyItem);
    });
}

/**
 * Format a date as a string
 * @param {Date} date - Date to format
 * @returns {string} Formatted date string
 */
function formatDate(date) {
    return date.toLocaleDateString() + ' ' + date.toLocaleTimeString();
}
