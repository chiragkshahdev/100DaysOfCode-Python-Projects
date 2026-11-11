# 🎵 Spotify Playlist Creator - Day 46

Create a Spotify playlist from the Billboard Hot 100 chart for any date you want.

Enter a date like your birthday, and this script will scrape the Top 100 songs from that day and automatically create a private Spotify playlist for you.

## ✨ Features

- Scrapes Billboard Hot 100 for any date (YYYY-MM-DD)
- Searches each song on Spotify using Spotipy
- Creates a private playlist named `{date} Billboard 100`
- Automatically adds all found songs to the playlist
- Skips songs that are not available on Spotify

## 🛠️ Tech Used

- Python
- BeautifulSoup4 - For web scraping Billboard
- Requests - For fetching Billboard page
- Spotipy - Spotify Web API wrapper

## ⚙️ Setup

1. Clone this repo:
```bash
git clone https://github.com/your-username/spotify-playlist-creator.git

## Go to your Spotify App Settings and change Redirect URI to this exact one:

http://127.0.0.1:8888/callback