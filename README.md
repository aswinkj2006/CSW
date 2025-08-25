# AI Customer Sentiment Watchdog

A real-time customer feedback analysis dashboard powered by AI, providing sentiment analysis, language detection, and trend visualization for customer support tickets.

## Features

- 🎯 Real-time sentiment analysis of customer feedback
- 🌍 Multi-language support with automatic translation
- 📊 Interactive data visualization with Chart.js
- 🔄 Auto-refresh and real-time updates
- 📱 Responsive design for all devices
- 💡 AI-powered sentiment scoring and emotion detection
- 🔍 Advanced filtering and sorting capabilities

## Setup Instructions

1. Clone the repository:
```bash
git clone <your-repo-url>
cd CSW
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
Create a `.env` file in the root directory with:
```env
OPENROUTER_API_KEY=your_api_key_here
SENTIMENT_WATCH_SECRET=your_secret_key_here
```

4. Run the application:
```bash
python app.py
```

5. Open your browser and navigate to:
```
http://localhost:5000
```

## Creating a Dataset

The application expects CSV files with the following columns:

- `ticket_id`: Unique identifier for each ticket
- `message`: The customer feedback text
- `date`: Date in YYYY-MM-DD format
- `time`: Time in HH:MM:SS format

Example Excel/CSV format:

| ticket_id | message | date | time |
|-----------|---------|------|------|
| 1 | Great customer service! | 2025-08-26 | 10:30:00 |
| 2 | Product needs improvement | 2025-08-26 | 11:15:00 |

Tips for creating your dataset:
1. Use Excel or Google Sheets to create your data
2. Ensure dates are in YYYY-MM-DD format
3. Ensure times are in HH:MM:SS format
4. Save as CSV (Comma Separated Values)
5. Maximum file size: 16MB

You can download a [sample dataset template here](sample_template.csv).

## Deploying to Render

1. Create a free account on [Render](https://render.com)

2. Create a new Web Service:
   - Connect your GitHub repository
   - Choose Python environment
   - Set build command: `pip install -r requirements.txt`
   - Set start command: `gunicorn app:app`

3. Add environment variables in Render dashboard:
   - OPENROUTER_API_KEY
   - SENTIMENT_WATCH_SECRET

4. Your app will be available at the URL provided by Render

## Environment Variables

| Variable | Description |
|----------|-------------|
| OPENROUTER_API_KEY | Your OpenRouter API key for sentiment analysis |
| SENTIMENT_WATCH_SECRET | Secret key for Flask session security |

## Project Structure

```
CSW/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── templates/         # HTML templates
│   ├── dashboard.html  # Main dashboard template
│   └── upload.html     # File upload template
├── uploads/           # Uploaded CSV files
└── .env              # Environment variables
```

## API Endpoints

- `/api/summary` - Get sentiment summary statistics
- `/api/alerts` - Get recent negative sentiment alerts
- `/api/urgent` - Get high-priority tickets
- `/api/trends` - Get daily sentiment trends
- `/api/all-tickets` - Get full ticket list with analysis

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

This project is licensed under the MIT License.
