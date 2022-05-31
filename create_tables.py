import sqlalchemy

db = 'postgresql://dima:1242@localhost:5432/music'
engine = sqlalchemy.create_engine(db)
conn = engine.connect()


def create_tables():
    conn.execute('''CREATE table if not EXISTS genres (
                    genre_id SERIAL primary key,
                    genre_name VARCHAR(20) not null);

                    CREATE table if not EXISTS singers (
                    singer_id SERIAL primary key,
                    singer_name VARCHAR(40) not null);

                    CREATE table if not EXISTS singergenre (
                    singer_id INT references singers(singer_id),
                    genre_id INT references genres(genre_id),
                    constraint singer_genre primary key (singer_id, genre_id));

                    CREATE table if not EXISTS albums (
                    album_id SERIAL primary key,
                    album_name VARCHAR(40) not null,
                    album_year INT);

                    CREATE table if not EXISTS singeralbum (
                    singer_id INT references singers(singer_id),
                    album_id INT references albums(album_id),
                    constraint singer_album primary key (singer_id, album_id));

                    CREATE table if not EXISTS tracks (
                    track_id SERIAL primary key,
                    album_id INTEGER references albums(album_id),
                    track_name VARCHAR(40) not null,
                    track_time INT);

                    CREATE table if not EXISTS compilations (
                    compilation_id SERIAL primary key,
                    compilation_name VARCHAR(40) not null,
                    compilation_year VARCHAR(4));

                    CREATE table if not EXISTS compilationtrack (
                    compilation_id  INT references compilations(compilation_id),
                    track_id  INT references tracks(track_id),
                    constraint compilation_track primary key (compilation_id, track_id));
                 ''')