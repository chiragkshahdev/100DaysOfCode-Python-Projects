# Day 45 - Web Scraping - 100 Movies to Watch

Scrape Empire's 100 Greatest Movies list using BeautifulSoup.

## What I Learned
- requests.get() - Website ka HTML lana
- BeautifulSoup - HTML ko parse karna
- find_all() - Saare tags dhundhna
- getText() - Sirf text nikalna
- List slicing [::-1] - List reverse karna
- File writing - movies.txt me save karna

## How Web Scraping Works
1. Browser ki tarah request bhejo
2. HTML response aata hai
3. BeautifulSoup us HTML ko readable banata hai
4. Tumhe chahiye wala tag (h3.title) find karo
5. Text nikal ke file me save karo

## Files
- main.py - Main scraper
- movies.txt - Output (100 movies)
- requirements.txt - Libraries

## How to Run
pip install requests beautifulsoup4 lxml
python main.py

## Important Note
- Empire site kabhi-kabhi block karta hai, isliye web.archive.org wala link use kiya hai (stable hai)
- Sirf learning ke liye scraping karo, heavy scraping mat karo