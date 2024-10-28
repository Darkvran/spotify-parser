import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyClientCredentials
import requests


load_dotenv('keys.env')

class SpotifyAPI:
    def __init__(self):
        proxies = {
            "http": "http://t1t7zM:FGJk1E@45.92.168.27:8000",
            "https": "http://t1t7zM:FGJk1E@45.92.168.27:8000"

        }
        self.requests_session = requests.Session()
        self.requests_session.proxies.update(proxies)

        self.auth_manager = SpotifyClientCredentials()
        self.sp = spotipy.Spotify(auth_manager=self.auth_manager, requests_session=self.requests_session)

    def get_popular_artists(self):
        genres = ['pop', 'rock', 'hip-hop', 'jazz', 'electronic', 'R&B', 'classic', 'house', 'trans']
        popular_artists = []
        for genre in genres:
            result = self.sp.search(q=f'genre:{genre}', type='artist')
            artists = result['artists']['items']
            for artist in  artists:
                print(artist)
                popular_artists.append({"Название": artist['name'], "Жанры": artist['genres'], 'Количество слушателей': artist['followers']})
        return popular_artists

spotify = SpotifyAPI()
spotify.get_popular_artists()