from pprint import pprint
import spotipy
from Passwords import SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI
from spotipy.oauth2 import SpotifyOAuth


scope = 'user-library-read'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope=scope))

results = sp.current_user_saved_tracks()

for idx, item in enumerate(results['items']):
    track = item['track']
    # print(idx, track['artists'][0]['name'], " – ", track['name'])
    pprint(track['uri'])
    break

# if __name__ == '__main__':
#     print(SPOTIFY_REDIRECT_URI)
