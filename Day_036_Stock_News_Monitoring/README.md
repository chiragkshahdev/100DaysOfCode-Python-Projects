# Day 36 - Stock News Monitoring

Monitors stock price and if it moves significantly, it shows top 3 latest news for that company.

## Features
- Fetches Stock Price from Alpha Vantage API
- Calculates % Change between last 2 days
- If change > 1%, fetches News from NewsAPI
- Shows Top 3 Headlines with Description and Link

## APIs Used
1. Alpha Vantage - https://www.alphavantage.co
2. NewsAPI - https://newsapi.org

Both are Free. Create account and paste your API Key in main.py

## How to Run
1. Install requests:
   pip install requests

2. Add your API Keys in main.py:
   STOCK_API_KEY = "your_key"
   NEWS_API_KEY = "your_key"

3. Run the app:
   python main.py

## Tech Used
- Python
- Requests Library
- Alpha Vantage API
- NewsAPI

## Change Stock
Change STOCK and COMPANY_NAME in main.py
Example: STOCK = "TSLA", COMPANY_NAME = "Tesla Inc"