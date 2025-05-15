import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
import time
from dotenv import load_dotenv
import os

# Load credentials from .env
load_dotenv()
CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
REDIRECT_URI = os.getenv("SPOTIFY_REDIRECT_URI")
SCOPE = "user-library-read"
CACHE_PATH = ".cache"

# Set up Spotify with OAuth
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope=SCOPE,
    cache_path=CACHE_PATH
))

# Fetch liked songs
def get_liked_songs():
    songs = []
    offset = 0
    limit = 50
    print("Fetching liked songs...")
    while True:
        try:
            results = sp.current_user_saved_tracks(limit=limit, offset=offset)
            if not results['items']:
                break
            for item in results['items']:
                track = item['track']
                songs.append({
                    'Title': track['name'],
                    'Artist': ", ".join(artist['name'] for artist in track['artists']),
                    'Album': track['album']['name'],
                    'Duration (min)': round(track['duration_ms'] / 60000, 2),
                    'Popularity': track['popularity']
                })
            offset += limit
            print(f"Processed {offset} songs...")
            time.sleep(0.5)
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(2)
    return songs

# Save to CSV
def save_to_csv(songs):
    df = pd.DataFrame(songs)
    df.to_csv("liked_songs.csv", index=False)
    print(f"Saved {len(songs)} songs to liked_songs.csv")

# Run the script
songs = get_liked_songs()
save_to_csv(songs)