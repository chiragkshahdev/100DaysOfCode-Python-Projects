# Day 45 - Alternative Method - More Reliable

import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(URL, headers=headers)
print(response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

# Empire ab h3 me nahi, div me deta hai - dono try karo
movies = []

# Method 1: h3.title
titles = soup.find_all("h3", class_="title")
if titles:
    movies = [t.getText().strip() for t in titles]
else:
    # Method 2: Sabhi h3 / h2 try karo
    all_h3 = soup.find_all("h3")
    movies = [h.getText().strip() for h in all_h3 if h.getText().strip()]

movies = movies[::-1]

with open("movies.txt", "w", encoding="utf-8") as f:
    for i, movie in enumerate(movies, 1):
        f.write(f"{i}. {movie}\n")
        print(f"{i}. {movie}")

print(f"\nTotal: {len(movies)} movies saved!")