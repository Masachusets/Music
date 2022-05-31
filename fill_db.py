import sqlalchemy
# from pprint import pprint
import Spotify
from create_tables import create_tables


db = 'postgresql://dima:1242@localhost:5432/music'
engine = sqlalchemy.create_engine(db)
conn = engine.connect()


def fill_genres(genres):
    for genre in genres:
        conn.execute(f'''INSERT INTO genres (genre_name) 
                         VALUES ('{genre}');
                      ''')


def fill_singers(singers):
    for singer in singers:
        conn.execute(f'''INSERT INTO singers (singer_name) 
                         VALUES ('{singer}');
                      ''')


def fill_singergenre(singer_genre):
    for singer, genres in singer_genre.items():
        if singer not in Spotify.singers:
            continue
        singer_id = list(conn.execute(f'''SELECT singer_id FROM singers 
                                          WHERE singer_name='{singer}';
                                       ''').fetchone())[0]
        for genre in genres:
            genre_id = conn.execute(f'''SELECT genre_id FROM genres 
                                             WHERE genre_name='{genre}';
                                          ''').fetchone()[0]
            conn.execute(f'''INSERT INTO singergenre (singer_id, genre_id) 
                             VALUES ({singer_id}, {genre_id});
                          ''')


def fill_albums(albums):
    for album in albums:
        conn.execute(f'''INSERT INTO albums (album_name, album_year) 
                         VALUES ('{album[0]}', {album[1]});
                      ''')


def fill_singeralbum(singer_album):
    for sin_al in singer_album:
        singer_id = list(conn.execute(f'''SELECT singer_id FROM singers 
                                          WHERE singer_name='{sin_al[0]}';
                                       ''').fetchone())[0]
        album_id = list(conn.execute(f'''SELECT album_id FROM albums 
                                         WHERE album_name='{sin_al[1]}';
                                      ''').fetchone())[0]
        conn.execute(f'''INSERT INTO singeralbum (singer_id, album_id) 
                         VALUES ({singer_id}, {album_id});
                      ''')


def fill_tracks(tracks):
    for track in tracks:
        album_id = list(conn.execute(f'''SELECT album_id FROM albums 
                                         WHERE album_name='{track[2]}';
                                      ''').fetchone())[0]
        conn.execute(f'''INSERT INTO tracks (track_name, track_time, album_id) 
                         VALUES ('{track[0]}', {track[1]}, {album_id});
                      ''')


def fill_compilations(compilations):
    for compilation in compilations:
        conn.execute(f'''INSERT INTO compilations (compilation_name, compilation_year) 
                         VALUES ('{compilation[0]}', {compilation[1]});
                      ''')


def fill_compilationtrack(compilation_track):
    for compilation, tracks in compilation_track.items():
        compilation_id = list(conn.execute(f'''SELECT compilation_id FROM compilations 
                                               WHERE compilation_name='{compilation}';
                                            ''').fetchone())[0]
        for track in tracks:
            track_id = list(conn.execute(f'''SELECT track_id FROM tracks 
                                             WHERE track_name='{track}';
                                          ''').fetchone())[0]
            conn.execute(f'''INSERT INTO compilationtrack (compilation_id, track_id) 
                             VALUES ({compilation_id}, {track_id});
                          ''')


# sel = conn.execute(
# """
# SELECT * FROM albums;
# """).fetchall()
#
# pprint(sel)
if __name__ == '__main__':
    create_tables()
    fill_genres(Spotify.genres)
    fill_singers(Spotify.singers)
    fill_singergenre(Spotify.singer_genre)
    fill_albums(Spotify.albums)
    fill_singeralbum(Spotify.singer_album)
    fill_tracks(Spotify.tracks)
    fill_compilations(Spotify.compilations)
    fill_compilationtrack(Spotify.compilation_track)
