import urllib.request
import urllib.parse
import json
import re
import webbrowser
import base64
from http.server import HTTPServer, BaseHTTPRequestHandler

# --- PUT YOUR SPOTIFY CREDENTIALS HERE ---
CLIENT_ID = "Your_Client_ID_Here"
CLIENT_SECRET = "Your_Client_Secret_Here"
REDIRECT_URI = "http://127.0.0.1:8888/callback"

# 1. Get date from user
date = input("Which date playlist do you want? Enter in YYYY-MM-DD format (e.g. 2000-08-12): ")
year = date.split("-")[0]

# 2. Scrape Billboard Hot 100 - No BeautifulSoup needed
print("Fetching songs from Billboard...")
URL = f"https://www.billboard.com/charts/hot-100/{date}/"
req = urllib.request.Request(URL, headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(req) as res:
    html = res.read().decode("utf-8", errors="ignore")

# Extract song titles
song_names = re.findall(r'id="title-of-a-story"[^>]*>(.*?)</h3>', html)
song_names = [re.sub(r'<[^>]+>', '', s).strip() for s in song_names]
song_names = [s for s in song_names if s]

# Fallback method if first one fails
if not song_names:
    song_names = re.findall(r'<h3[^>]*class="[^"]*c-title[^"]*"[^>]*>(.*?)</h3>', html)
    song_names = [re.sub(r'<[^>]+>', '', s).strip() for s in song_names]

print(f"Found {len(song_names)} songs!")
for s in song_names[:5]:
    print(" -", s)

if not song_names:
    print("No songs found. Check your date or Billboard is blocking the request.")
    exit()

# 3. Spotify Login - No Spotipy needed
print("\nOpening Spotify login... Click Allow in your browser.")

auth_url = (
    "https://accounts.spotify.com/authorize?"
    + urllib.parse.urlencode({
        "client_id": CLIENT_ID,
        "response_type": "code",
        "redirect_uri": REDIRECT_URI,
        "scope": "playlist-modify-private",
        "show_dialog": "true"
    })
)

code_holder = {}

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if "code=" in self.path:
            code = self.path.split("code=")[1].split("&")[0]
            code_holder["code"] = code
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"<h1>Success! Go back to your terminal.</h1>")
        else:
            self.send_response(400)
            self.end_headers()
    def log_message(self, *args):
        pass

webbrowser.open(auth_url)
server = HTTPServer(("127.0.0.1", 8888), Handler)
server.handle_request()
server.server_close()

code = code_holder.get("code")
if not code:
    print("Login failed.")
    exit()

# Get Access Token
auth_str = f"{CLIENT_ID}:{CLIENT_SECRET}"
auth_b64 = base64.b64encode(auth_str.encode()).decode()
data = urllib.parse.urlencode({
    "grant_type": "authorization_code",
    "code": code,
    "redirect_uri": REDIRECT_URI
}).encode()

token_req = urllib.request.Request(
    "https://accounts.spotify.com/api/token",
    data=data,
    headers={"Authorization": f"Basic {auth_b64}", "Content-Type": "application/x-www-form-urlencoded"}
)
with urllib.request.urlopen(token_req) as res:
    token_data = json.loads(res.read())
access_token = token_data["access_token"]
headers = {"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"}

def spotify_get(path, params):
    q = urllib.parse.urlencode(params)
    req = urllib.request.Request(f"https://api.spotify.com/v1{path}?{q}", headers=headers)
    with urllib.request.urlopen(req) as res:
        return json.loads(res.read())

def spotify_post(path, body):
    req = urllib.request.Request(
        f"https://api.spotify.com/v1{path}",
        data=json.dumps(body).encode(),
        headers=headers,
        method="POST"
    )
    with urllib.request.urlopen(req) as res:
        return json.loads(res.read())

# Get User ID
user = spotify_get("/me", {})
user_id = user["id"]
print(f"Logged in as: {user_id}")

# 4. Search each song on Spotify
song_uris = []
for song in song_names:
    try:
        result = spotify_get("/search", {"q": f"track:{song} year:{year}", "type": "track", "limit": 1})
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
        print(f"Found: {song}")
    except:
        print(f"Skipped: {song} not found")

# 5. Create Playlist and Add Songs
playlist = spotify_post(f"/users/{user_id}/playlists", {"name": f"{date} Billboard 100", "public": False})
playlist_id = playlist["id"]

# Add in batches of 100
for i in range(0, len(song_uris), 100):
    spotify_post(f"/playlists/{playlist_id}/tracks", {"uris": song_uris[i:i+100]})

print(f"\nDONE! Playlist created: {date} Billboard 100")
print("Open Spotify and check your library.")