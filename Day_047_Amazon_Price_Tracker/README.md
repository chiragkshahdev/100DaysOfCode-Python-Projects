# Day 47 - Amazon Price Tracker

An automated price tracker that scrapes Amazon product prices and sends you an email alert when the price drops below your target price.

## Features

- Scrapes live price from any Amazon product page
- Compares current price with your target price
- Sends instant email alert on price drop
- Can run automatically every 24 hours
- No database needed

## How It Works

1. User sets a Target Price for a product
2. Script fetches the product page using `requests` + `BeautifulSoup`
3. Extracts the product title and current price
4. If Current Price < Target Price -> Sends email via Gmail SMTP
5. If not, it waits and checks again later

## Tech Stack

- **Python 3**
- **Requests** - To fetch Amazon product page
- **BeautifulSoup (lxml)** - To scrape price and title
- **SMTP (smtplib)** - To send email alert
- **Gmail App Password** - For secure login

## Installation

```bash
pip install requests beautifulsoup4 lxml
