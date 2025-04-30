/**
 * Storage.js - Handles browser localStorage for crawl history
 */

// Load crawl history from localStorage
function loadHistory() {
    const history = getHistory();
    
    // Clear previous history
    historyTable.innerHTML = '';
    
    // Populate history table
    history.forEach(item => {
        addHistoryRow(item);
    });
}

// Get history from localStorage
function getHistory() {
    const historyJson = localStorage.getItem('crawlHistory');
    return historyJson ? JSON.parse(historyJson) : [];
}

// Save history to localStorage
function saveHistory(history) {
    localStorage.setItem('crawlHistory', JSON.stringify(history));
}

// Add a new crawl to history
function addToHistory(item) {
    const history = getHistory();
    
    // Check if item already exists
    const existingIndex = history.findIndex(h => h.id === item.id);
    if (existingIndex !== -1) {
        // Update existing item
        history[existingIndex] = { ...history[existingIndex], ...item };
    } else {
        // Add new item
        history.unshift(item);
    }
    
    // Limit history to 10 items
    if (history.length > 10) {
        history.pop();
    }
    
    saveHistory(history);
    
    // Update UI
    loadHistory();
}

// Update an existing history item
function updateHistoryItem(id, updates) {
    const history = getHistory();
    const index = history.findIndex(item => item.id === id);
    
    if (index !== -1) {
        history[index] = { ...history[index], ...updates };
        saveHistory(history);
        
        // Update UI
        loadHistory();
    }
}

// Add a history row to the UI
function addHistoryRow(item) {
    const row = document.createElement('tr');
    row.setAttribute('data-id', item.id);
    
    const dateCell = document.createElement('td');
    dateCell.textContent = new Date(item.startTime).toLocaleString();
    
    const urlCell = document.createElement('td');
    urlCell.textContent = item.url;
    
    const pagesCell = document.createElement('td');
    pagesCell.className = 'pages-cell';
    pagesCell.textContent = `${item.crawledPages || 0}/${item.maxPages}`;
    
    const statusCell = document.createElement('td');
    statusCell.className = 'status-cell';
    statusCell.textContent = item.status;
    
    const actionsCell = document.createElement('td');
    
    const viewBtn = document.createElement('button');
    viewBtn.className = 'btn btn-sm btn-info me-2';
    viewBtn.textContent = 'View';
    viewBtn.addEventListener('click', () => loadCrawl(item.id));
    
    const downloadBtn = document.createElement('button');
    downloadBtn.className = 'btn btn-sm btn-success';
    downloadBtn.textContent = 'Download';
    downloadBtn.addEventListener('click', () => window.location.href = `/api/download/${item.id}`);
    
    actionsCell.appendChild(viewBtn);
    actionsCell.appendChild(downloadBtn);
    
    row.appendChild(dateCell);
    row.appendChild(urlCell);
    row.appendChild(pagesCell);
    row.appendChild(statusCell);
    row.appendChild(actionsCell);
    
    historyTable.appendChild(row);
}

// Load a previous crawl
function loadCrawl(id) {
    currentJobId = id;
    
    // Find the crawl in history
    const history = getHistory();
    const crawl = history.find(item => item.id === id);
    
    if (crawl) {
        // Update UI
        jobIdElement.textContent = id;
        crawlUrlElement.textContent = crawl.url;
        statusTextElement.textContent = crawl.status;
        progressTextElement.textContent = `${crawl.crawledPages || 0}/${crawl.maxPages}`;
        
        const percentage = Math.round(((crawl.crawledPages || 0) / crawl.maxPages) * 100);
        progressBarElement.style.width = `${percentage}%`;
        
        crawlStatus.classList.remove('d-none');
        
        if (crawl.status === 'completed') {
            downloadBtn.classList.remove('d-none');
        } else {
            downloadBtn.classList.add('d-none');
        }
        
        // Load results
        viewResults();
    }
}

// Clear all history
function clearHistory() {
    if (confirm('Are you sure you want to clear all crawl history?')) {
        localStorage.removeItem('crawlHistory');
        historyTable.innerHTML = '';
    }
}
