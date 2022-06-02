import spotipy
from Passwords import SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint

#
# class Spotify:
#     scope = 'user-library-read'
#     def __init__(self, client_id, client_secret, redirect_url):
#         self.client_id = client_id
#         self.client_secret = client_secret
#         self.redirect_uri = redirect_url
#         self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=self.client_id,
#                                                             client_secret=self.client_secret,
#                                                             redirect_uri=self.redirect_uri,
#                                                             scope=self.scope))

scope = 'user-library-read'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope=scope))

current_user_saved_tracks = sp.current_user_saved_tracks(limit=50)


genres = ('acoustic', 'alternative', 'blues', 'classical', 'country', 'dance', 'electro', 'folk', 'guitar', 'hip-hop',
          'jazz', 'metal', 'opera', 'piano', 'pop', 'punk', 'reggae', 'rock', 'rock-n-roll', 'romance', 'soundtrack')


singers = set(artist['name'] for item in current_user_saved_tracks['items'] for artist in item['track']['artists'])


singer_genre = {'25/17': ('alternative', 'hip-hop', 'rock'),
                '7B': ('alternative', 'pop', 'rock'),
                'Adelitas Way': ('rock',),
                'Animal Jazz': ('alternative', 'rock'),
                'Basta': ('alternative', 'folk', 'hip-hop', 'pop', 'rock'),
                'Chaif': ('blues', 'country', 'reggae', 'rock', 'rock-n-roll'),
                'DREZDEN': ('electro', 'rock'),
                'Kino': ('rock',),
                'Korol i Shut': ('folk', 'punk', 'rock'),
                'Kukryniksy': ('alternative', 'punk', 'rock'),
                'Lyapis Trubetskoy': ('alternative', 'folk', 'pop', 'rock'),
                'Nautilus Pompilius': ('alternative', 'pop', 'rock'),
                'Nikolai Noskov': ('pop', 'rock', 'romance'),
                'Nizkiz': ('alternative', 'pop', 'rock'),
                'Odyn v Kanoe': ('rock',),
                'Okean Elzy': ('alternative', 'pop', 'rock'),
                'Piknik': ('rock', 'rock-n-roll'),
                'Pornofilmy': ('pop', 'punk', 'rock'),
                'Splean': ('alternative', 'pop', 'rock'),
                'System Of A Down': ('alternative', 'metal', 'rock'),
                'Zero People': ('piano', 'rock'),
                'Алексей Горшенёв': ('alternative', 'punk', 'rock'),
                'Владимир Златоустовский': ('soundtrack',),
                'ДДТ': ('alternative', 'folk', 'rock'),
                'Евгения Рыбакова': ('guitar', 'rock'),
                'Калинов Мост': ('blues', 'folk', 'rock'),
                'Чиж & Co': ('blues', 'country', 'folk', 'jazz', 'rock', 'rock-n-roll', 'romance')}


albums = set((item['track']['album']['name'], int(item['track']['album']['release_date'][:4]))
             for item in current_user_saved_tracks['items'])


singer_album = set((artist['name'], item['track']['album']['name'])
                   for item in current_user_saved_tracks['items'] for artist in item['track']['artists'])


tracks = set((item['track']['name'], item['track']['duration_ms'] // 1000, item['track']['album']['name'])
          for item in current_user_saved_tracks['items'])


compilations = (('one word', 2020),
                ('two words', 2021),
                ('more two words', 2022),
                ('russian', 2020),
                ('not russian', 2021),
                ('before 2001', 2001),
                ('from 2001 to 2011', 2011),
                ('after 2010', 2022))


compilation_track = {compilation[0]: [] for compilation in compilations}
for item in current_user_saved_tracks['items']:
    track = item['track']
    count_words = len(track['name'].split())
    if count_words == 1:
        compilation_track['one word'].append(track['name'])
    elif count_words == 2:
        compilation_track['two words'].append(track['name'])
    else:
        compilation_track['more two words'].append(track['name'])

    if ord(track['name'][0]) > 191:
        compilation_track['russian'].append(track['name'])
    else:
        compilation_track['not russian'].append(track['name'])

    if int(track['album']['release_date'][:4]) < 2001:
        compilation_track['before 2001'].append(track['name'])
    elif int(track['album']['release_date'][:4]) > 2010:
        compilation_track['after 2010'].append(track['name'])
    else:
        compilation_track['from 2001 to 2011'].append(track['name'])
for compilation in compilation_track:
    compilation_track[compilation] = set(compilation_track[compilation])

# for item in current_user_saved_tracks['items']:
#     track = item['track']['album']['artists']
# pprint(compilation_track)

# pprint(genres['genres'])
# if __name__ == '__main__':
