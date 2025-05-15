# Spotify Liked Songs Scraper

A Python script that pulls all your Spotify "Liked Songs" and saves them to a CSV file with details like title, artist, album, duration, and popularity. 
Uses the Spotipy library and Spotify API.

## How It Works

- The script (`spotifyRake.py`) connects to Spotify with your API credentials.
- It fetches all your liked songs, 50 at a time.
- Saves the data to `liked_songs.csv`, which you can open in Excel to sort or filter songs.

## How to Run It

1. **Install Python**:
    - Download Python 3.8+ from [python.org](https://www.python.org/downloads/).
    - Check “Add Python to PATH” during installation.
2. **Clone the Repository**:
    - In Command Prompt or VS Code Terminal:
        
        ```bash
        git clone https://github.com/bilzeebubb/SpotifyRake.git
        cd SpotifyRake
        
3. **Set Up Virtual Environment**:
    
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```
    
4. **Install Libraries**:
    
    ```bash
    pip install spotipy pandas python-dotenv
    ```
    
5. **Get Spotify API Credentials**:
    - Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).
    - Create an app, copy your `Client ID` and `Client Secret`.
    - Set the app’s Redirect URI to `http://127.0.0.1:8888/callback`.
    - In the `SpotifyRake` folder, create a `.env` file with:
        
        ```
        SPOTIFY_CLIENT_ID=your_client_id
        SPOTIFY_CLIENT_SECRET=your_client_secret
        SPOTIFY_REDIRECT_URI=http://127.0.0.1:8888/callback
        ```
        
6. **Run the Script**:
    
    ```bash
    python spotifyRake.py
    ```
    
    - A browser will open. Log in to Spotify, authorize, and copy the redirect URL (like `http://127.0.0.1:8888/callback?code=...`) into the terminal.
    - The script saves your songs to `liked_songs.csv`. Time depends on how many songs you have.

## Notes

- Keep `.env` and `.cache` (created after running) private. They’re ignored by `.gitignore`.
- If authentication fails, delete `.cache` and re-run the script.
- Open `liked_songs.csv` in Excel to check your songs.