import os
from dotenv import load_dotenv
from flask import Flask, redirect
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Load environment variables from .env file
load_dotenv()
SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
SPOTIFY_REDIRECT_URI = "https://localhost:8080"

# Scopes define the level of access you are requesting from the user
SPOTIFY_SCOPE = 'user-read-currently-playing'

# Authenticate with Spotify using Spotipy
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                                client_secret=SPOTIPY_CLIENT_SECRET,
                                                redirect_uri=SPOTIFY_REDIRECT_URI,
                                                scope=SPOTIFY_SCOPE))

# Function to get the currently playing track
def get_currently_playing():
    try:
        current_track = sp.currently_playing(market=None)
        if current_track is not None and 'item' in current_track:
            track_name = current_track['item']['name']
            artist_name = current_track['item']['artists'][0]['name']
            album_cover_url = current_track['item']['album']['images'][0]['url']
            return album_cover_url
        else:
            return None
    except spotipy.exceptions.SpotifyException as e:
        return None

app = Flask(__name__)

@app.route('/')
def display_album_cover():
    album_cover_url = get_currently_playing()
    if album_cover_url:
        return redirect(album_cover_url)
    else:
        return "No track is currently playing or an error occurred.", 404

# Run the function
if __name__ == '__main__':
    app.run(debug=True)
