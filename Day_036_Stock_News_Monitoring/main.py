# Day 36 - Stock News Monitoring
# APIs Used: Alpha Vantage (Stock Price) + NewsAPI (News)

import requests

# --- Put Your Free API Keys Here ---
STOCK_API_KEY = "YOUR_ALPHA_VANTAGE_KEY"
NEWS_API_KEY = "YOUR_NEWS_API_KEY"

STOCK = "AAPL"  # Apple - You can change to TSLA, RELIANCE.BSE, INFY
COMPANY_NAME = "Apple Inc"

def get_stock_change():
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={STOCK_API_KEY}"
    try:
        response = requests.get(url)
        data = response.json()
        daily = data["Time Series (Daily)"]
        dates = list(daily.keys())

        yesterday_close = float(daily[dates[0]]["4. close"])
        day_before_close = float(daily[dates[1]]["4. close"])

        diff = yesterday_close - day_before_close
        percent = (diff / day_before_close) * 100
        return percent
    except Exception as e:
        print("Stock API Error:", e)
        return 0

def get_news():
    url = f"https://newsapi.org/v2/everything?q={COMPANY_NAME}&sortBy=publishedAt&apiKey={NEWS_API_KEY}"
    try:
        response = requests.get(url)
        data = response.json()
        articles = data["articles"][:3]
        return articles
    except Exception as e:
        print("News API Error:", e)
        return []

def main():
    print("=== Stock News Monitoring ===")
    print(f"Checking {STOCK} - {COMPANY_NAME}...\n")

    percent = get_stock_change()
    print(f"Stock Change: {percent:.2f}%")

    # If stock moves more than 1% (for testing), show news
    # In real project, use 5%
    if abs(percent) > 1:
        if percent > 0:
            print(f"{STOCK}: UP by {percent:.2f}%")
        else:
            print(f"{STOCK}: DOWN by {percent:.2f}%")

        print("\n--- Top 3 News ---\n")
        articles = get_news()

        if not articles:
            print("No news found.")
            return

        for i, article in enumerate(articles, 1):
            print(f"{i}. {article['title']}")
            print(f"   {article['description']}")
            print(f"   Link: {article['url']}\n")
    else:
        print("Stock is stable. No major news alert.")

if __name__ == "__main__":
    main()