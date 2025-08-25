# Enhanced HTML Template with fancy UI
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>AI Customer Sentiment Watchdog</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.0/chart.min.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            color: #333;
        }
        
        .container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 20px;
        }
        
        .header {
            text-align: center;
            color: white;
            margin-bottom: 30px;
            text-shadow: 0 2px 4px rgba(0,0,0,0.3);
        }
        
        .header h1 {
            font-size: 3rem;
            margin-bottom: 10px;
            background: linear-gradient(45deg, #FFD700, #FF6B6B);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        
        .header p {
            font-size: 1.2rem;
            opacity: 0.9;
        }
        
        .status-bar {
            background: rgba(255,255,255,0.1);
            backdrop-filter: blur(10px);
            border-radius: 15px;
            padding: 15px;
            margin-bottom: 30px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border: 1px solid rgba(255,255,255,0.2);
        }
        
        .refresh-btn {
            background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
            color: white;
            border: none;
            padding: 12px 24px;
            border-radius: 50px;
            cursor: pointer;
            font-weight: bold;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        }
        
        .refresh-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(0,0,0,0.3);
        }
        
        .timestamp {
            color: white;
            opacity: 0.8;
        }
        
        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 25px;
            margin-bottom: 30px;
        }
        
        .card {
            background: rgba(255,255,255,0.95);
            backdrop-filter: blur(20px);
            border-radius: 20px;
            padding: 25px;
            box-shadow: 0 8px 32px rgba(0,0,0,0.1);
            border: 1px solid rgba(255,255,255,0.3);
            transition: all 0.3s ease;
        }
        
        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 12px 40px rgba(0,0,0,0.15);
        }
        
        .card h2 {
            margin-bottom: 20px;
            color: #2c3e50;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .card h2 i {
            background: linear-gradient(45deg, #667eea, #764ba2);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        
        .metrics {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
            gap: 15px;
        }
        
        .metric {
            text-align: center;
            padding: 20px;
            border-radius: 15px;
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            transition: all 0.3s ease;
        }
        
        .metric:hover {
            transform: scale(1.05);
        }
        
        .metric h3 {
            font-size: 2.5em;
            margin: 10px 0 5px 0;
            font-weight: bold;
        }
        
        .metric p {
            color: #666;
            font-weight: 500;
            text-transform: uppercase;
            font-size: 0.85em;
            letter-spacing: 0.5px;
        }
        
        .positive { color: #27ae60; }
        .negative { color: #e74c3c; }
        .neutral { color: #f39c12; }
        .high-urgency { color: #e74c3c; }
        .medium-urgency { color: #f39c12; }
        .low-urgency { color: #27ae60; }
        
        .alert-item {
            background: linear-gradient(135deg, #ffebee, #ffcdd2);
            border-left: 5px solid #e74c3c;
            padding: 15px;
            margin: 10px 0;
            border-radius: 10px;
            transition: all 0.3s ease;
        }
        
        .alert-item:hover {
            transform: translateX(5px);
            box-shadow: 0 4px 15px rgba(231,76,60,0.2);
        }
        
        .urgent-item {
            background: linear-gradient(135deg, #fff3e0, #ffe0b2);
            border-left: 5px solid #ff9800;
            padding: 15px;
            margin: 10px 0;
            border-radius: 10px;
            transition: all 0.3s ease;
        }
        
        .urgent-item:hover {
            transform: translateX(5px);
            box-shadow: 0 4px 15px rgba(255,152,0,0.2);
        }
        
        .chart-container {
            width: 100%;
            height: 400px;
            position: relative;
        }
        
        .full-width {
            grid-column: 1 / -1;
        }
        
        .badge {
            display: inline-block;
            padding: 4px 8px;
            border-radius: 12px;
            font-size: 0.8em;
            font-weight: bold;
            margin: 2px;
        }
        
        .badge-positive { background: #d4edda; color: #155724; }
        .badge-negative { background: #f8d7da; color: #721c24; }
        .badge-neutral { background: #fff3cd; color: #856404; }
        .badge-high { background: #f8d7da; color: #721c24; }
        .badge-medium { background: #fff3cd; color: #856404; }
        .badge-low { background: #d4edda; color: #155724; }
        
        .translation-box {
            background: #e3f2fd;
            border-radius: 8px;
            padding: 10px;
            margin-top: 8px;
            font-style: italic;
            color: #1565c0;
        }
        
        .stats-row {
            display: flex;
            justify-content: space-between;
            margin: 10px 0;
            padding: 8px;
            background: rgba(0,0,0,0.05);
            border-radius: 8px;
        }
        
        .loading {
            text-align: center;
            padding: 40px;
            color: #666;
        }
        
        .loading i {
            font-size: 3em;
            animation: spin 2s linear infinite;
        }
        
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        
        .no-alerts {
            text-align: center;
            padding: 40px;
            color: #27ae60;
            font-size: 1.2em;
        }
        
        @media (max-width: 768px) {
            .container { padding: 10px; }
            .header h1 { font-size: 2rem; }
            .grid { grid-template-columns: 1fr; }
            .metrics { grid-template-columns: repeat(2, 1fr); }
            .status-bar { flex-direction: column; gap: 10px; }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>AI Customer Sentiment Watchdog</h1>
            <p>Powered by DeepSeek V3 Intelligence</p>
        </div>
        
        <div class="status-bar">
            <div style="display: flex; gap: 15px; align-items: center;">
                <button class="refresh-btn" onclick="refreshData()">
                    <i class="fas fa-sync-alt"></i> Refresh Data
                </button>
                <a href="/upload" class="refresh-btn" style="text-decoration: none;">
                    <i class="fas fa-upload"></i> Upload CSV
                </a>
            </div>
            <div style="text-align: right;">
                <div class="timestamp" id="lastUpdate"></div>
                <div class="timestamp" id="fileInfo" style="font-size: 0.9em; opacity: 0.7;"></div>
            </div>
        </div>
        
        <div class="grid">
            <div class="card">
                <h2><i class="fas fa-chart-pie"></i> Sentiment Overview</h2>
                <div class="metrics" id="metrics">
                    <div class="loading">
                        <i class="fas fa-spinner"></i>
                        <p>Loading...</p>
                    </div>
                </div>
            </div>
            
            <div class="card">
                <h2><i class="fas fa-globe"></i> Language Distribution</h2>
                <div id="languages">
                    <div class="loading">
                        <i class="fas fa-spinner"></i>
                        <p>Loading...</p>
                    </div>
                </div>
            </div>
            
            <div class="card">
                <h2><i class="fas fa-tags"></i> Category Breakdown</h2>
                <div id="categories">
                    <div class="loading">
                        <i class="fas fa-spinner"></i>
                        <p>Loading...</p>
                    </div>
                </div>
            </div>
            
            <div class="card">
                <h2><i class="fas fa-heart"></i> Emotion Analysis</h2>
                <div id="emotions">
                    <div class="loading">
                        <i class="fas fa-spinner"></i>
                        <p>Loading...</p>
                    </div>
                </div>
            </div>
            
            <div class="card full-width">
                <h2><i class="fas fa-chart-line"></i> Sentiment Trends</h2>
                <div class="chart-container">
                    <canvas id="trendsChart" width="400" height="200"></canvas>
                </div>
            </div>
            
            <div class="card">
                <h2><i class="fas fa-exclamation-triangle"></i> High Priority Tickets</h2>
                <div id="urgent">
                    <div class="loading">
                        <i class="fas fa-spinner"></i>
                        <p>Loading...</p>
                    </div>
                </div>
            </div>
            
            <div class="card">
                <h2><i class="fas fa-bell"></i> Recent Negative Alerts</h2>
                <div id="alerts">
                    <div class="loading">
                        <i class="fas fa-spinner"></i>
                        <p>Loading...</p>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script>
        let trendsChart;
        
        function updateMetrics(data) {
            const metricsDiv = document.getElementById('metrics');
            const total = data.total_tickets;
            
            metricsDiv.innerHTML = `
                <div class="metric">
                    <h3 class="positive">${data.summary.positive}</h3>
                    <p>Positive</p>
                </div>
                <div class="metric">
                    <h3 class="neutral">${data.summary.neutral}</h3>
                    <p>Neutral</p>
                </div>
                <div class="metric">
                    <h3 class="negative">${data.summary.negative}</h3>
                    <p>Negative</p>
                </div>
                <div class="metric">
                    <h3>${total}</h3>
                    <p>Total</p>
                </div>
                <div class="metric">
                    <h3 class="${data.average_score >= 0 ? 'positive' : 'negative'}">${data.average_score}</h3>
                    <p>Avg Score</p>
                </div>
                <div class="metric">
                    <h3>${data.confidence_average}</h3>
                    <p>AI Confidence</p>
                </div>
            `;
        }
        
        function updateLanguages(languages) {
            const langDiv = document.getElementById('languages');
            if (Object.keys(languages).length === 0) {
                langDiv.innerHTML = '<p>No language data available</p>';
                return;
            }
            
            const total = Object.values(languages).reduce((a, b) => a + b, 0);
            langDiv.innerHTML = Object.entries(languages)
                .sort(([,a], [,b]) => b - a)
                .map(([lang, count]) => `
                    <div class="stats-row">
                        <span>${lang.charAt(0).toUpperCase() + lang.slice(1)}</span>
                        <span><strong>${count}</strong> (${Math.round(count/total*100)}%)</span>
                    </div>
                `).join('');
        }
        
        function updateEmotions(emotions) {
            const emoDiv = document.getElementById('emotions');
            if (Object.keys(emotions).length === 0) {
                emoDiv.innerHTML = '<p>No emotion data available</p>';
                return;
            }
            
            const total = Object.values(emotions).reduce((a, b) => a + b, 0);
            emoDiv.innerHTML = Object.entries(emotions)
                .sort(([,a], [,b]) => b - a)
                .map(([emotion, count]) => `
                    <div class="stats-row">
                        <span>${emotion.charAt(0).toUpperCase() + emotion.slice(1)}</span>
                        <span><strong>${count}</strong> (${Math.round(count/total*100)}%)</span>
                    </div>
                `).join('');
        }
        
        function updateAlerts(alerts) {
            const alertsDiv = document.getElementById('alerts');
            
            if (alerts.length === 0) {
                alertsDiv.innerHTML = '<div class="no-alerts"><i class="fas fa-check-circle"></i><br>No negative sentiment alerts!</div>';
                return;
            }
            
            alertsDiv.innerHTML = alerts.map(alert => `
                <div class="alert-item">
                    <div style="display: flex; justify-content: space-between; align-items: start; margin-bottom: 8px;">
                        <strong>Ticket #${alert.ticket_id}</strong>
                        <div>
                            <span class="badge badge-${alert.emotion}">${alert.emotion}</span>
                            <span class="badge badge-negative">Score: ${alert.sentiment_score}</span>
                        </div>
                    </div>
                    <p>${alert.message}</p>
                    ${alert.translation ? `<div class="translation-box"><i class="fas fa-language"></i> Translation: ${alert.translation}</div>` : ''}
                    <small style="color: #666;">
                        ${alert.datetime} | ${alert.category} | ${alert.language} | Confidence: ${alert.confidence}
                    </small>
                </div>
            `).join('');
        }
        
        function updateUrgent(urgent) {
            const urgentDiv = document.getElementById('urgent');
            
            if (urgent.length === 0) {
                urgentDiv.innerHTML = '<div class="no-alerts"><i class="fas fa-check-circle"></i><br>No high priority tickets!</div>';
                return;
            }
            
            urgentDiv.innerHTML = urgent.map(ticket => `
                <div class="urgent-item">
                    <div style="display: flex; justify-content: space-between; align-items: start; margin-bottom: 8px;">
                        <strong>Ticket #${ticket.ticket_id}</strong>
                        <div>
                            <span class="badge badge-high">HIGH PRIORITY</span>
                            <span class="badge badge-${ticket.emotion}">${ticket.emotion}</span>
                        </div>
                    </div>
                    <p>${ticket.message}</p>
                    ${ticket.translation !== ticket.message ? `<div class="translation-box"><i class="fas fa-language"></i> Translation: ${ticket.translation}</div>` : ''}
                    <small style="color: #666;">
                        ${ticket.datetime} | ${ticket.category} | Confidence: ${ticket.confidence}
                    </small>
                </div>
            `).join('');
        }
        
        function updateTrends(trends) {
            const ctx = document.getElementById('trendsChart');
            if (!ctx) {
                console.error('Chart canvas not found');
                return;
            }
            
            // Destroy existing chart if it exists
            if (trendsChart) {
                trendsChart.destroy();
            }
            
            // Wait for DOM to be ready
            setTimeout(() => {
                try {
                    trendsChart = new Chart(ctx, {
                        type: 'line',
                        data: {
                            labels: trends.map(t => t.date),
                            datasets: [
                                {
                                    label: 'Positive',
                                    data: trends.map(t => t.positive),
                                    borderColor: '#27ae60',
                                    backgroundColor: 'rgba(39, 174, 96, 0.1)',
                                    fill: true,
                                    tension: 0.4
                                },
                                {
                                    label: 'Neutral',
                                    data: trends.map(t => t.neutral),
                                    borderColor: '#f39c12',
                                    backgroundColor: 'rgba(243, 156, 18, 0.1)',
                                    fill: true,
                                    tension: 0.4
                                },
                                {
                                    label: 'Negative',
                                    data: trends.map(t => t.negative),
                                    borderColor: '#e74c3c',
                                    backgroundColor: 'rgba(231, 76, 60, 0.1)',
                                    fill: true,
                                    tension: 0.4
                                }
                            ]
                        },
                        options: {
                            responsive: true,
                            maintainAspectRatio: false,
                            plugins: {
                                title: {
                                    display: true,
                                    text: 'Daily Sentiment Trends',
                                    font: { size: 16, weight: 'bold' }
                                },
                                legend: {
                                    position: 'top',
                                    labels: { usePointStyle: true }
                                }
                            },
                            scales: {
                                y: {
                                    beginAtZero: true,
                                    title: {
                                        display: true,
                                        text: 'Number of Tickets'
                                    },
                                    grid: { color: 'rgba(0,0,0,0.1)' }
                                },
                                x: {
                                    title: {
                                        display: true,
                                        text: 'Date'
                                    },
                                    grid: { color: 'rgba(0,0,0,0.1)' }
                                }
                            },
                            interaction: {
                                intersect: false,
                                mode: 'index'
                            }
                        }
                    });
                } catch (error) {
                    console.error('Error creating chart:', error);
                    document.getElementById('trendsChart').parentElement.innerHTML = '<p style="text-align: center; padding: 40px; color: #666;">Chart could not be loaded</p>';
                }
            }, 100);
        }
        
        async function loadData() {
            try {
                // Show loading state
                document.getElementById('lastUpdate').textContent = 'Loading...';
                
                // Load file info
                const fileResponse = await fetch('/api/file-info');
                const fileData = await fileResponse.json();
                document.getElementById('fileInfo').textContent = `File: ${fileData.current_file} (${fileData.total_records} records)`;
                
                // Load summary data
                const summaryResponse = await fetch('/api/summary');
                const summaryData = await summaryResponse.json();
                
                updateMetrics(summaryData);
                updateLanguages(summaryData.languages);
                updateCategories(summaryData.categories);
                updateEmotions(summaryData.emotions);
                
                // Load alerts
                const alertsResponse = await fetch('/api/alerts');
                const alertsData = await alertsResponse.json();
                updateAlerts(alertsData.alerts);
                
                // Load urgent tickets
                const urgentResponse = await fetch('/api/urgent');
                const urgentData = await urgentResponse.json();
                updateUrgent(urgentData.urgent);
                
                // Load trends
                const trendsResponse = await fetch('/api/trends');
                const trendsData = await trendsResponse.json();
                updateTrends(trendsData.trends);
                
                // Update timestamp
                document.getElementById('lastUpdate').textContent = `Last updated: ${new Date().toLocaleString()}`;
                
            } catch (error) {
                console.error('Error loading data:', error);
                document.getElementById('lastUpdate').textContent = 'Error loading data';
            }
        }
        
        async function refreshData() {
            const refreshBtn = document.querySelector('.refresh-btn');
            const originalText = refreshBtn.innerHTML;
            
            refreshBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Refreshing...';
            refreshBtn.disabled = true;
            
            try {
                await fetch('/api/reload');
                await loadData();
            } finally {
                refreshBtn.innerHTML = originalText;
                refreshBtn.disabled = false;
            }
        }
        
        // Load data on page load
        document.addEventListener('DOMContentLoaded', function() {
            // Wait a bit for DOM to be fully ready
            setTimeout(loadData, 500);
        });
        
        // Auto-refresh every 5 minutes
        setInterval(loadData, 300000);
        
        // Add some interactive features
        document.addEventListener('click', function(e) {
            if (e.target.closest('.metric')) {
                e.target.closest('.metric').style.transform = 'scale(1.1)';
                setTimeout(() => {
                    e.target.closest('.metric').style.transform = '';
                }, 200);
            }
        });
    </script>
</body>
</html>
'''

# Upload template
UPLOAD_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Upload CSV - AI Sentiment Watchdog</title>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #333;
        }
        
        .upload-container {
            background: rgba(255,255,255,0.95);
            backdrop-filter: blur(20px);
            border-radius: 20px;
            padding: 40px;
            box-shadow: 0 8px 32px rgba(0,0,0,0.1);
            border: 1px solid rgba(255,255,255,0.3);
            max-width: 600px;
            width: 90%;
        }
        
        .header {
            text-align: center;
            margin-bottom: 30px;
        }
        
        .header h1 {
            color: #2c3e50;
            margin-bottom: 10px;
            background: linear-gradient(45deg, #667eea, #764ba2);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        
        .upload-zone {
            border: 2px dashed #667eea;
            border-radius: 15px;
            padding: 40px;
            text-align: center;
            margin: 20px 0;
            transition: all 0.3s ease;
            cursor: pointer;
        }
        
        .upload-zone:hover {
            border-color: #764ba2;
            background: rgba(102,126,234,0.05);
        }
        
        .upload-zone.dragover {
            border-color: #FF6B6B;
            background: rgba(255,107,107,0.05);
        }
        
        .upload-zone i {
            font-size: 3em;
            color: #667eea;
            margin-bottom: 15px;
        }
        
        .upload-btn {
            background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
            color: white;
            border: none;
            padding: 12px 30px;
            border-radius: 50px;
            cursor: pointer;
            font-weight: bold;
            font-size: 1.1em;
            margin: 20px 10px;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        }
        
        .upload-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(0,0,0,0.3);
        }
        
        .back-btn {
            background: linear-gradient(45deg, #667eea, #764ba2);
        }
        
        .file-input {
            display: none;
        }
        
        .requirements {
            background: #f8f9fa;
            border-radius: 10px;
            padding: 20px;
            margin: 20px 0;
        }
        
        .requirements h3 {
            color: #2c3e50;
            margin-bottom: 15px;
        }
        
        .requirements ul {
            margin-left: 20px;
            color: #666;
        }
        
        .requirements li {
            margin: 5px 0;
        }
        
        .alert {
            padding: 15px;
            border-radius: 10px;
            margin: 20px 0;
            font-weight: bold;
        }
        
        .alert-success {
            background: #d4edda;
            color: #155724;
            border: 1px solid #c3e6cb;
        }
        
        .alert-error {
            background: #f8d7da;
            color: #721c24;
            border: 1px solid #f5c6cb;
        }
        
        .selected-file {
            background: #e3f2fd;
            border-radius: 10px;
            padding: 15px;
            margin: 15px 0;
            color: #1565c0;
        }
    </style>
</head>
<body>
    <div class="upload-container">
        <div class="header">
            <h1><i class="fas fa-upload"></i> Upload CSV File</h1>
            <p>Upload your customer feedback CSV for AI analysis</p>
        </div>
        
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="alert alert-{{ 'success' if category == 'success' else 'error' }}">
                        <i class="fas fa-{{ 'check-circle' if category == 'success' else 'exclamation-triangle' }}"></i>
                        {{ message }}
                    </div>
                {% endfor %}
            {% endif %}
        {% endwith %}
        
        <form method="post" enctype="multipart/form-data" id="uploadForm">
            <div class="upload-zone" onclick="document.getElementById('fileInput').click()">
                <i class="fas fa-cloud-upload-alt"></i>
                <h3>Click to select CSV file or drag & drop</h3>
                <p>Maximum file size: 16MB</p>
                <div id="selectedFile" class="selected-file" style="display: none;"></div>
            </div>
            <input type="file" id="fileInput" name="file" class="file-input" accept=".csv" onchange="showSelectedFile(this)">
            
            <div class="requirements">
                <h3><i class="fas fa-info-circle"></i> Required CSV Format</h3>
                <ul>
                    <li><strong>ticket_id</strong> - Unique identifier for each ticket</li>
                    <li><strong>message</strong> - Customer feedback text</li>
                    <li><strong>date</strong> - Date in YYYY-MM-DD format</li>
                    <li><strong>time</strong> - Time in HH:MM:SS format</li>
                </ul>
                <p style="margin-top: 10px; font-style: italic; color: #666;">
                    Example: ticket_id,message,date,time<br>
                    1,"Great product!",2024-01-15,10:30:00
                </p>
            </div>
            
            <div style="text-align: center;">
                <button type="submit" class="upload-btn">
                    <i class="fas fa-upload"></i> Upload & Analyze
                </button>
                <a href="/" class="upload-btn back-btn" style="text-decoration: none;">
                    <i class="fas fa-arrow-left"></i> Back to Dashboard
                </a>
            </div>
        </form>
    </div>
    
    <script>
        function showSelectedFile(input) {
            const selectedFileDiv = document.getElementById('selectedFile');
            if (input.files.length > 0) {
                const file = input.files[0];
                selectedFileDiv.innerHTML = `
                    <i class="fas fa-file-csv"></i>
                    <strong>Selected:</strong> ${file.name} (${(file.size / 1024 / 1024).toFixed(2)} MB)
                `;
                selectedFileDiv.style.display = 'block';
            } else {
                selectedFileDiv.style.display = 'none';
            }
        }
        
        // Drag and drop functionality
        const uploadZone = document.querySelector('.upload-zone');
        
        uploadZone.addEventListener('dragover', function(e) {
            e.preventDefault();
            uploadZone.classList.add('dragover');
        });
        
        uploadZone.addEventListener('dragleave', function(e) {
            e.preventDefault();
            uploadZone.classList.remove('dragover');
        });
        
        uploadZone.addEventListener('drop', function(e) {
            e.preventDefault();
            uploadZone.classList.remove('dragover');
            
            const files = e.dataTransfer.files;
            if (files.length > 0 && files[0].name.toLowerCase().endsWith('.csv')) {
                document.getElementById('fileInput').files = files;
                showSelectedFile(document.getElementById('fileInput'));
            }
        });
        
        // Form submission with loading state
        document.getElementById('uploadForm').addEventListener('submit', function(e) {
            const submitBtn = document.querySelector('button[type="submit"]');
            const originalText = submitBtn.innerHTML;
            
            submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Analyzing...';
            submitBtn.disabled = true;
        });
    </script>
</body>
</html>
'''('');
        }
        
        function updateCategories(categories) {
            const catDiv = document.getElementById('categories');
            if (Object.keys(categories).length === 0) {
                catDiv.innerHTML = '<p>No category data available</p>';
                return;
            }
            
            const total = Object.values(categories).reduce((a, b) => a + b, 0);
            catDiv.innerHTML = Object.entries(categories)
                .sort(([,a], [,b]) => b - a)
                .map(([cat, count]) => `
                    <div class="stats-row">
                        <span>${cat.charAt(0).toUpperCase() + cat.slice(1)}</span>
                        <span><strong>${count}</strong> (${Math.round(count/total*100)}%)</span>
                    </div>
                `).join@app.route('/api/reload')
def api_reload():
    watchdog.load_data()
    return jsonify({'status': 'Data reloaded successfully'})from flask import Flask, render_template, jsonify, request, redirect, url_for, flash
import pandas as pd
import requests
import json
from datetime import datetime, timedelta
from collections import Counter
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'sentiment_watchdog_secret_key_2024'
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Create upload directory
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# OpenRouter API Configuration
OPENROUTER_API_KEY = "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"
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

class AIAnalyzer:
    def __init__(self):
        self.headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        }
    
    def analyze_sentiment_with_ai(self, text):
        """Use DeepSeek to analyze sentiment with detailed reasoning"""
        try:
            prompt = f"""Analyze the sentiment of this customer feedback and provide a JSON response:

Text: "{text}"

Provide response in this exact JSON format:
{{
    "sentiment": "positive/negative/neutral",
    "confidence": 0.95,
    "score": 0.8,
    "language": "detected_language",
    "translation": "english_translation_if_needed",
    "key_issues": ["issue1", "issue2"],
    "emotion": "happy/angry/frustrated/satisfied/confused",
    "urgency": "low/medium/high",
    "category": "product/service/delivery/technical/billing"
}}

Score should be between -1 (very negative) and 1 (very positive).
Only translate if the original text is not in English."""

            payload = {
                "model": "deepseek/deepseek-chat",
                "messages": [
                    {"role": "system", "content": "You are an expert customer sentiment analyst. Always respond with valid JSON only."},
                    {"role": "user", "content": prompt}
                ],
                "temperature": 0.3,
                "max_tokens": 500
            }
            
            response = requests.post(OPENROUTER_URL, headers=self.headers, json=payload, timeout=10)
            
            if response.status_code == 200:
                result = response.json()
                content = result['choices'][0]['message']['content'].strip()
                
                # Extract JSON from the response
                if content.startswith('```json'):
                    content = content.replace('```json', '').replace('```', '').strip()
                
                return json.loads(content)
            else:
                return self.fallback_analysis(text)
                
        except Exception as e:
            print(f"AI Analysis error: {e}")
            return self.fallback_analysis(text)
    
    def fallback_analysis(self, text):
        """Fallback sentiment analysis when AI fails"""
        text_lower = text.lower()
        positive_words = ['love', 'great', 'excellent', 'amazing', 'perfect', 'satisfied', 'good']
        negative_words = ['terrible', 'awful', 'hate', 'worst', 'bad', 'poor', 'frustrated']
        
        pos_count = sum(1 for word in positive_words if word in text_lower)
        neg_count = sum(1 for word in negative_words if word in text_lower)
        
        if pos_count > neg_count:
            sentiment = "positive"
            score = 0.6
        elif neg_count > pos_count:
            sentiment = "negative" 
            score = -0.6
        else:
            sentiment = "neutral"
            score = 0.0
            
        return {
            "sentiment": sentiment,
            "confidence": 0.7,
            "score": score,
            "language": "unknown",
            "translation": text if self.is_english(text) else "Translation unavailable",
            "key_issues": [],
            "emotion": "neutral",
            "urgency": "medium",
            "category": "general"
        }
    
    def is_english(self, text):
        # Simple check for English text
        english_chars = sum(1 for c in text if c.isascii())
        return english_chars / len(text) > 0.8 if text else True

class SentimentWatchdog:
    def __init__(self, csv_file=None):
        self.csv_file = csv_file or 'test_tickets.csv'
        self.analyzer = AIAnalyzer()
        self.df = pd.DataFrame()
        if os.path.exists(self.csv_file):
            self.load_data()
    
    def set_csv_file(self, csv_file):
        self.csv_file = csv_file
        self.load_data()
    
    def validate_csv_format(self, df):
        """Validate that the CSV has the required columns"""
        required_columns = ['ticket_id', 'message', 'date', 'time']
        missing_columns = [col for col in required_columns if col not in df.columns]
        
        if missing_columns:
            return False, f"Missing required columns: {', '.join(missing_columns)}"
        
        return True, "Valid format"
    
    def load_data(self):
        try:
            if not os.path.exists(self.csv_file):
                print(f"CSV file {self.csv_file} not found")
                self.df = pd.DataFrame()
                return
                
            self.df = pd.read_csv(self.csv_file)
            
            # Validate CSV format
            is_valid, message = self.validate_csv_format(self.df)
            if not is_valid:
                print(f"Invalid CSV format: {message}")
                self.df = pd.DataFrame()
                return
            
            self.df['datetime'] = pd.to_datetime(self.df['date'] + ' ' + self.df['time'])
            
            # Check if we need to analyze tickets
            if 'ai_analysis' not in self.df.columns:
                print("Analyzing tickets with AI... This may take a moment...")
                self.df['ai_analysis'] = self.df['message'].apply(
                    lambda x: json.dumps(self.analyzer.analyze_sentiment_with_ai(x))
                )
                # Save the analyzed data
                self.df.to_csv(self.csv_file, index=False)
            
            # Parse AI analysis results
            self.df['analysis'] = self.df['ai_analysis'].apply(json.loads)
            self.df['sentiment'] = self.df['analysis'].apply(lambda x: x['sentiment'])
            self.df['sentiment_score'] = self.df['analysis'].apply(lambda x: x['score'])
            self.df['confidence'] = self.df['analysis'].apply(lambda x: x['confidence'])
            self.df['language'] = self.df['analysis'].apply(lambda x: x['language'])
            self.df['translation'] = self.df['analysis'].apply(lambda x: x['translation'])
            self.df['emotion'] = self.df['analysis'].apply(lambda x: x['emotion'])
            self.df['urgency'] = self.df['analysis'].apply(lambda x: x['urgency'])
            self.df['category'] = self.df['analysis'].apply(lambda x: x['category'])
            
        except Exception as e:
            print(f"Error loading data: {e}")
            self.df = pd.DataFrame()
    
    def get_sentiment_summary(self):
        if self.df.empty:
            return {'positive': 0, 'negative': 0, 'neutral': 0}
        
        sentiment_counts = self.df['sentiment'].value_counts().to_dict()
        return {
            'positive': sentiment_counts.get('positive', 0),
            'negative': sentiment_counts.get('negative', 0),
            'neutral': sentiment_counts.get('neutral', 0)
        }
    
    def get_language_breakdown(self):
        if self.df.empty:
            return {}
        return self.df['language'].value_counts().to_dict()
    
    def get_category_breakdown(self):
        if self.df.empty:
            return {}
        return self.df['category'].value_counts().to_dict()
    
    def get_emotion_breakdown(self):
        if self.df.empty:
            return {}
        return self.df['emotion'].value_counts().to_dict()
    
    def get_urgent_tickets(self):
        if self.df.empty:
            return []
        
        urgent = self.df[self.df['urgency'] == 'high'].copy()
        
        tickets = []
        for _, ticket in urgent.iterrows():
            tickets.append({
                'ticket_id': ticket['ticket_id'],
                'message': ticket['message'][:100] + '...' if len(ticket['message']) > 100 else ticket['message'],
                'translation': ticket['translation'],
                'datetime': ticket['datetime'].strftime('%Y-%m-%d %H:%M'),
                'sentiment_score': round(ticket['sentiment_score'], 2),
                'emotion': ticket['emotion'],
                'category': ticket['category'],
                'confidence': round(ticket['confidence'], 2)
            })
        
        return sorted(tickets, key=lambda x: x['sentiment_score'])
    
    def get_recent_alerts(self, hours=24):
        if self.df.empty:
            return []
        
        cutoff_time = datetime.now() - timedelta(hours=hours)
        recent_df = self.df[self.df['datetime'] >= cutoff_time]
        
        alerts = []
        negative_tickets = recent_df[recent_df['sentiment'] == 'negative']
        
        for _, ticket in negative_tickets.iterrows():
            alerts.append({
                'ticket_id': ticket['ticket_id'],
                'message': ticket['message'][:100] + '...' if len(ticket['message']) > 100 else ticket['message'],
                'translation': ticket['translation'] if ticket['translation'] != ticket['message'] else None,
                'datetime': ticket['datetime'].strftime('%Y-%m-%d %H:%M'),
                'sentiment_score': round(ticket['sentiment_score'], 2),
                'emotion': ticket['emotion'],
                'category': ticket['category'],
                'language': ticket['language'],
                'confidence': round(ticket['confidence'], 2)
            })
        
        return sorted(alerts, key=lambda x: x['sentiment_score'])
    
    def get_daily_trends(self, days=7):
        if self.df.empty:
            return []
        
        cutoff_date = datetime.now() - timedelta(days=days)
        recent_df = self.df[self.df['datetime'] >= cutoff_date]
        
        daily_sentiment = recent_df.groupby([recent_df['datetime'].dt.date, 'sentiment']).size().unstack(fill_value=0)
        
        trends = []
        for date, row in daily_sentiment.iterrows():
            trends.append({
                'date': date.strftime('%Y-%m-%d'),
                'positive': int(row.get('positive', 0)),
                'negative': int(row.get('negative', 0)),
                'neutral': int(row.get('neutral', 0))
            })
        
        return trends
    
    def get_average_sentiment_score(self):
        if self.df.empty:
            return 0
        return round(self.df['sentiment_score'].mean(), 3)
    
    def get_confidence_average(self):
        if self.df.empty:
            return 0
        return round(self.df['confidence'].mean(), 3)

# Initialize watchdog
watchdog = SentimentWatchdog()

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() == 'csv'

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/api/summary')
def api_summary():
    summary = watchdog.get_sentiment_summary()
    avg_score = watchdog.get_average_sentiment_score()
    confidence = watchdog.get_confidence_average()
    languages = watchdog.get_language_breakdown()
    categories = watchdog.get_category_breakdown()
    emotions = watchdog.get_emotion_breakdown()
    
    return jsonify({
        'summary': summary,
        'average_score': avg_score,
        'confidence_average': confidence,
        'total_tickets': len(watchdog.df),
        'languages': languages,
        'categories': categories,
        'emotions': emotions
    })

@app.route('/api/alerts')
def api_alerts():
    hours = request.args.get('hours', 24, type=int)
    alerts = watchdog.get_recent_alerts(hours)
    return jsonify({'alerts': alerts})

@app.route('/api/urgent')
def api_urgent():
    urgent = watchdog.get_urgent_tickets()
    return jsonify({'urgent': urgent})

@app.route('/api/trends')
def api_trends():
    days = request.args.get('days', 7, type=int)
    trends = watchdog.get_daily_trends(days)
    return jsonify({'trends': trends})

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file selected', 'error')
            return redirect(request.url)
        
        file = request.files['file']
        if file.filename == '':
            flash('No file selected', 'error')
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            try:
                filename = secure_filename(file.filename)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)
                
                # Validate the uploaded CSV
                test_df = pd.read_csv(filepath)
                is_valid, message = watchdog.validate_csv_format(test_df)
                
                if not is_valid:
                    os.remove(filepath)
                    flash(f'Invalid CSV format: {message}', 'error')
                    return redirect(request.url)
                
                # Set the new CSV file for analysis
                watchdog.set_csv_file(filepath)
                flash('File uploaded and analyzed successfully!', 'success')
                return redirect(url_for('dashboard'))
                
            except Exception as e:
                flash(f'Error processing file: {str(e)}', 'error')
                return redirect(request.url)
        else:
            flash('Please upload a CSV file', 'error')
            return redirect(request.url)
    
    return render_template('upload.html')

@app.route('/api/file-info')
def api_file_info():
    return jsonify({
        'current_file': os.path.basename(watchdog.csv_file),
        'file_exists': os.path.exists(watchdog.csv_file),
        'total_records': len(watchdog.df) if not watchdog.df.empty else 0
    })

# Enhanced HTML Template with fancy UI
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>AI Customer Sentiment Watchdog</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.0/chart.min.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            color: #333;
        }
        
        .container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 20px;
        }
        
        .header {
            text-align: center;
            color: white;
            margin-bottom: 30px;
            text-shadow: 0 2px 4px rgba(0,0,0,0.3);
        }
        
        .header h1 {
            font-size: 3rem;
            margin-bottom: 10px;
            background: linear-gradient(45deg, #FFD700, #FF6B6B);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        
        .header p {
            font-size: 1.2rem;
            opacity: 0.9;
        }
        
        .status-bar {
            background: rgba(255,255,255,0.1);
            backdrop-filter: blur(10px);
            border-radius: 15px;
            padding: 15px;
            margin-bottom: 30px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border: 1px solid rgba(255,255,255,0.2);
        }
        
        .refresh-btn {
            background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
            color: white;
            border: none;
            padding: 12px 24px;
            border-radius: 50px;
            cursor: pointer;
            font-weight: bold;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        }
        
        .refresh-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(0,0,0,0.3);
        }
        
        .timestamp {
            color: white;
            opacity: 0.8;
        }
        
        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 25px;
            margin-bottom: 30px;
        }
        
        .card {
            background: rgba(255,255,255,0.95);
            backdrop-filter: blur(20px);
            border-radius: 20px;
            padding: 25px;
            box-shadow: 0 8px 32px rgba(0,0,0,0.1);
            border: 1px solid rgba(255,255,255,0.3);
            transition: all 0.3s ease;
        }
        
        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 12px 40px rgba(0,0,0,0.15);
        }
        
        .card h2 {
            margin-bottom: 20px;
            color: #2c3e50;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .card h2 i {
            background: linear-gradient(45deg, #667eea, #764ba2);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        
        .metrics {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
            gap: 15px;
        }
        
        .metric {
            text-align: center;
            padding: 20px;
            border-radius: 15px;
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            transition: all 0.3s ease;
        }
        
        .metric:hover {
            transform: scale(1.05);
        }
        
        .metric h3 {
            font-size: 2.5em;
            margin: 10px 0 5px 0;
            font-weight: bold;
        }
        
        .metric p {
            color: #666;
            font-weight: 500;
            text-transform: uppercase;
            font-size: 0.85em;
            letter-spacing: 0.5px;
        }
        
        .positive { color: #27ae60; }
        .negative { color: #e74c3c; }
        .neutral { color: #f39c12; }
        .high-urgency { color: #e74c3c; }
        .medium-urgency { color: #f39c12; }
        .low-urgency { color: #27ae60; }
        
        .alert-item {
            background: linear-gradient(135deg, #ffebee, #ffcdd2);
            border-left: 5px solid #e74c3c;
            padding: 15px;
            margin: 10px 0;
            border-radius: 10px;
            transition: all 0.3s ease;
        }
        
        .alert-item:hover {
            transform: translateX(5px);
            box-shadow: 0 4px 15px rgba(231,76,60,0.2);
        }
        
        .urgent-item {
            background: linear-gradient(135deg, #fff3e0, #ffe0b2);
            border-left: 5px solid #ff9800;
            padding: 15px;
            margin: 10px 0;
            border-radius: 10px;
            transition: all 0.3s ease;
        }
        
        .urgent-item:hover {
            transform: translateX(5px);
            box-shadow: 0 4px 15px rgba(255,152,0,0.2);
        }
        
        .chart-container {
            width: 100%;
            height: 400px;
            position: relative;
        }
        
        .full-width {
            grid-column: 1 / -1;
        }
        
        .badge {
            display: inline-block;
            padding: 4px 8px;
            border-radius: 12px;
            font-size: 0.8em;
            font-weight: bold;
            margin: 2px;
        }
        
        .badge-positive { background: #d4edda; color: #155724; }
        .badge-negative { background: #f8d7da; color: #721c24; }
        .badge-neutral { background: #fff3cd; color: #856404; }
        .badge-high { background: #f8d7da; color: #721c24; }
        .badge-medium { background: #fff3cd; color: #856404; }
        .badge-low { background: #d4edda; color: #155724; }
        
        .translation-box {
            background: #e3f2fd;
            border-radius: 8px;
            padding: 10px;
            margin-top: 8px;
            font-style: italic;
            color: #1565c0;
        }
        
        .stats-row {
            display: flex;
            justify-content: space-between;
            margin: 10px 0;
            padding: 8px;
            background: rgba(0,0,0,0.05);
            border-radius: 8px;
        }
        
        .loading {
            text-align: center;
            padding: 40px;
            color: #666;
        }
        
        .loading i {
            font-size: 3em;
            animation: spin 2s linear infinite;
        }
        
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        
        .no-alerts {
            text-align: center;
            padding: 40px;
            color: #27ae60;
            font-size: 1.2em;
        }
        
        @media (max-width: 768px) {
            .container { padding: 10px; }
            .header h1 { font-size: 2rem; }
            .grid { grid-template-columns: 1fr; }
            .metrics { grid-template-columns: repeat(2, 1fr); }
            .status-bar { flex-direction: column; gap: 10px; }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>AI Customer Sentiment Watchdog</h1>
            <p>Powered by DeepSeek V3 Intelligence</p>
        </div>
        
        <div class="status-bar">
            <div style="display: flex; gap: 15px; align-items: center;">
                <button class="refresh-btn" onclick="refreshData()">
                    <i class="fas fa-sync-alt"></i> Refresh Data
                </button>
                <a href="/upload" class="refresh-btn" style="text-decoration: none;">
                    <i class="fas fa-upload"></i> Upload CSV
                </a>
            </div>
            <div style="text-align: right;">
                <div class="timestamp" id="lastUpdate"></div>
                <div class="timestamp" id="fileInfo" style="font-size: 0.9em; opacity: 0.7;"></div>
            </div>
        </div>
        
        <div class="grid">
            <div class="card">
                <h2><i class="fas fa-chart-pie"></i> Sentiment Overview</h2>
                <div class="metrics" id="metrics">
                    <div class="loading">
                        <i class="fas fa-spinner"></i>
                        <p>Loading...</p>
                    </div>
                </div>
            </div>
            
            <div class="card">
                <h2><i class="fas fa-globe"></i> Language Distribution</h2>
                <div id="languages">
                    <div class="loading">
                        <i class="fas fa-spinner"></i>
                        <p>Loading...</p>
                    </div>
                </div>
            </div>
            
            <div class="card">
                <h2><i class="fas fa-tags"></i> Category Breakdown</h2>
                <div id="categories">
                    <div class="loading">
                        <i class="fas fa-spinner"></i>
                        <p>Loading...</p>
                    </div>
                </div>
            </div>
            
            <div class="card">
                <h2><i class="fas fa-heart"></i> Emotion Analysis</h2>
                <div id="emotions">
                    <div class="loading">
                        <i class="fas fa-spinner"></i>
                        <p>Loading...</p>
                    </div>
                </div>
            </div>
            
            <div class="card full-width">
                <h2><i class="fas fa-chart-line"></i> Sentiment Trends</h2>
                <div class="chart-container">
                    <canvas id="trendsChart"></canvas>
                </div>
            </div>
            
            <div class="card">
                <h2><i class="fas fa-exclamation-triangle"></i> High Priority Tickets</h2>
                <div id="urgent">
                    <div class="loading">
                        <i class="fas fa-spinner"></i>
                        <p>Loading...</p>
                    </div>
                </div>
            </div>
            
            <div class="card">
                <h2><i class="fas fa-bell"></i> Recent Negative Alerts</h2>
                <div id="alerts">
                    <div class="loading">
                        <i class="fas fa-spinner"></i>
                        <p>Loading...</p>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script>
        let trendsChart;
        
        function updateMetrics(data) {
            const metricsDiv = document.getElementById('metrics');
            const total = data.total_tickets;
            
            metricsDiv.innerHTML = `
                <div class="metric">
                    <h3 class="positive">${data.summary.positive}</h3>
                    <p>Positive</p>
                </div>
                <div class="metric">
                    <h3 class="neutral">${data.summary.neutral}</h3>
                    <p>Neutral</p>
                </div>
                <div class="metric">
                    <h3 class="negative">${data.summary.negative}</h3>
                    <p>Negative</p>
                </div>
                <div class="metric">
                    <h3>${total}</h3>
                    <p>Total</p>
                </div>
                <div class="metric">
                    <h3 class="${data.average_score >= 0 ? 'positive' : 'negative'}">${data.average_score}</h3>
                    <p>Avg Score</p>
                </div>
                <div class="metric">
                    <h3>${data.confidence_average}</h3>
                    <p>AI Confidence</p>
                </div>
            `;
        }
        
        function updateLanguages(languages) {
            const langDiv = document.getElementById('languages');
            if (Object.keys(languages).length === 0) {
                langDiv.innerHTML = '<p>No language data available</p>';
                return;
            }
            
            const total = Object.values(languages).reduce((a, b) => a + b, 0);
            langDiv.innerHTML = Object.entries(languages)
                .sort(([,a], [,b]) => b - a)
                .map(([lang, count]) => `
                    <div class="stats-row">
                        <span>${lang.charAt(0).toUpperCase() + lang.slice(1)}</span>
                        <span><strong>${count}</strong> (${Math.round(count/total*100)}%)</span>
                    </div>
                `).join('');
        }
        
        function updateCategories(categories) {
            const catDiv = document.getElementById('categories');
            if (Object.keys(categories).length === 0) {
                catDiv.innerHTML = '<p>No category data available</p>';
                return;
            }
            
            const total = Object.values(categories).reduce((a, b) => a + b, 0);
            catDiv.innerHTML = Object.entries(categories)
                .sort(([,a], [,b]) => b - a)
                .map(([cat, count]) => `
                    <div class="stats-row">
                        <span>${cat.charAt(0).toUpperCase() + cat.slice(1)}</span>
                        <span><strong>${count}</strong> (${Math.round(count/total*100)}%)</span>
                    </div>
                `).join('');
        }
        
        function updateEmotions(emotions) {
            const emoDiv = document.getElementById('emotions');
            if (Object.keys(emotions).length === 0) {
                emoDiv.innerHTML = '<p>No emotion data available</p>';
                return;
            }
            
            const total = Object.values(emotions).reduce((a, b) => a + b, 0);
            emoDiv.innerHTML = Object.entries(emotions)
                .sort(([,a], [,b]) => b - a)
                .map(([emotion, count]) => `
                    <div class="stats-row">
                        <span>${emotion.charAt(0).toUpperCase() + emotion.slice(1)}</span>
                        <span><strong>${count}</strong> (${Math.round(count/total*100)}%)</span>
                    </div>
                `).join('');
        }
        
        function updateAlerts(alerts) {
            const alertsDiv = document.getElementById('alerts');
            
            if (alerts.length === 0) {
                alertsDiv.innerHTML = '<div class="no-alerts"><i class="fas fa-check-circle"></i><br>No negative sentiment alerts!</div>';
                return;
            }
            
            alertsDiv.innerHTML = alerts.map(alert => `
                <div class="alert-item">
                    <div style="display: flex; justify-content: space-between; align-items: start; margin-bottom: 8px;">
                        <strong>Ticket #${alert.ticket_id}</strong>
                        <div>
                            <span class="badge badge-${alert.emotion}">${alert.emotion}</span>
                            <span class="badge badge-negative">Score: ${alert.sentiment_score}</span>
                        </div>
                    </div>
                    <p>${alert.message}</p>
                    ${alert.translation ? `<div class="translation-box"><i class="fas fa-language"></i> Translation: ${alert.translation}</div>` : ''}
                    <small style="color: #666;">
                        ${alert.datetime} | ${alert.category} | ${alert.language} | Confidence: ${alert.confidence}
                    </small>
                </div>
            `).join('');
        }
        
        function updateUrgent(urgent) {
            const urgentDiv = document.getElementById('urgent');
            
            if (urgent.length === 0) {
                urgentDiv.innerHTML = '<div class="no-alerts"><i class="fas fa-check-circle"></i><br>No high priority tickets!</div>';
                return;
            }
            
            urgentDiv.innerHTML = urgent.map(ticket => `
                <div class="urgent-item">
                    <div style="display: flex; justify-content: space-between; align-items: start; margin-bottom: 8px;">
                        <strong>Ticket #${ticket.ticket_id}</strong>
                        <div>
                            <span class="badge badge-high">HIGH PRIORITY</span>
                            <span class="badge badge-${ticket.emotion}">${ticket.emotion}</span>
                        </div>
                    </div>
                    <p>${ticket.message}</p>
                    ${ticket.translation !== ticket.message ? `<div class="translation-box"><i class="fas fa-language"></i> Translation: ${ticket.translation}</div>` : ''}
                    <small style="color: #666;">
                        ${ticket.datetime} | ${ticket.category} | Confidence: ${ticket.confidence}
                    </small>
                </div>
            `).join('');
        }
        
        function updateTrends(trends) {
            const ctx = document.getElementById('trendsChart').getContext('2d');
            
            if (trendsChart) {
                trendsChart.destroy();
            }
            
            trendsChart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: trends.map(t => t.date),
                    datasets: [
                        {
                            label: 'Positive',
                            data: trends.map(t => t.positive),
                            borderColor: '#27ae60',
                            backgroundColor: 'rgba(39, 174, 96, 0.1)',
                            fill: true,
                            tension: 0.4
                        },
                        {
                            label: 'Neutral',
                            data: trends.map(t => t.neutral),
                            borderColor: '#f39c12',
                            backgroundColor: 'rgba(243, 156, 18, 0.1)',
                            fill: true,
                            tension: 0.4
                        },
                        {
                            label: 'Negative',
                            data: trends.map(t => t.negative),
                            borderColor: '#e74c3c',
                            backgroundColor: 'rgba(231, 76, 60, 0.1)',
                            fill: true,
                            tension: 0.4
                        }
                    ]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        title: {
                            display: true,
                            text: 'Daily Sentiment Trends',
                            font: { size: 16, weight: 'bold' }
                        },
                        legend: {
                            position: 'top',
                            labels: { usePointStyle: true }
                        }
                    },
                    scales: {
                        y: {
                            beginAtZero: true,
                            title: {
                                display: true,
                                text: 'Number of Tickets'
                            },
                            grid: { color: 'rgba(0,0,0,0.1)' }
                        },
                        x: {
                            title: {
                                display: true,
                                text: 'Date'
                            },
                            grid: { color: 'rgba(0,0,0,0.1)' }
                        }
                    },
                    interaction: {
                        intersect: false,
                        mode: 'index'
                    }
                }
            });
        }
        
        async function loadData() {
            try {
                // Show loading state
                document.getElementById('lastUpdate').textContent = 'Loading...';
                
                // Load file info
                const fileResponse = await fetch('/api/file-info');
                const fileData = await fileResponse.json();
                document.getElementById('fileInfo').textContent = `File: ${fileData.current_file} (${fileData.total_records} records)`;
                
                // Load summary data
                const summaryResponse = await fetch('/api/summary');
                const summaryData = await summaryResponse.json();
                
                updateMetrics(summaryData);
                updateLanguages(summaryData.languages);
                updateCategories(summaryData.categories);
                updateEmotions(summaryData.emotions);
                
                // Load alerts
                const alertsResponse = await fetch('/api/alerts');
                const alertsData = await alertsResponse.json();
                updateAlerts(alertsData.alerts);
                
                // Load urgent tickets
                const urgentResponse = await fetch('/api/urgent');
                const urgentData = await urgentResponse.json();
                updateUrgent(urgentData.urgent);
                
                // Load trends
                const trendsResponse = await fetch('/api/trends');
                const trendsData = await trendsResponse.json();
                updateTrends(trendsData.trends);
                
                // Update timestamp
                document.getElementById('lastUpdate').textContent = `Last updated: ${new Date().toLocaleString()}`;
                
            } catch (error) {
                console.error('Error loading data:', error);
                document.getElementById('lastUpdate').textContent = 'Error loading data';
            }
        }
        
        async function refreshData() {
            const refreshBtn = document.querySelector('.refresh-btn');
            const originalText = refreshBtn.innerHTML;
            
            refreshBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Refreshing...';
            refreshBtn.disabled = true;
            
            try {
                await fetch('/api/reload');
                await loadData();
            } finally {
                refreshBtn.innerHTML = originalText;
                refreshBtn.disabled = false;
            }
        }
        
        // Load data on page load
        document.addEventListener('DOMContentLoaded', loadData);
        
        // Auto-refresh every 5 minutes
        setInterval(loadData, 300000);
        
        // Add some interactive features
        document.addEventListener('click', function(e) {
            if (e.target.closest('.metric')) {
                e.target.closest('.metric').style.transform = 'scale(1.1)';
                setTimeout(() => {
                    e.target.closest('.metric').style.transform = '';
                }, 200);
            }
        });
    </script>
</body>
</html>
'''

# Create templates directory and file
import os
if not os.path.exists('templates'):
    os.makedirs('templates')

with open('templates/dashboard.html', 'w', encoding='utf-8') as f:
    f.write(HTML_TEMPLATE)

if __name__ == '__main__':
    print("AI Customer Sentiment Watchdog starting...")
    print("Powered by DeepSeek V3 for advanced sentiment analysis")
    print("Dashboard available at: http://localhost:5000")
    print("Features: Multi-language support, AI translation, emotion analysis")
    
    app.run(debug=True, host='0.0.0.0', port=5000)