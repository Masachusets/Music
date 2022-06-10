import sqlalchemy


def req_to_tab(req):
    return conn.execute(f'''{req}''').fetchall()


req1 = '''select genre_name, count(singer_id) count_singer 
          from genres
               join singergenre USING(genre_id)
                    join singers USING(singer_id)
          group by genre_name;'''

req2 = '''select track_name, album_name, album_year 
          from tracks
               join albums USING(album_id)
          where album_year = 2020 or album_year = 2019;'''

req3 = '''select album_name, avg(track_time)  
          from tracks
               join albums USING(album_id)
          group by album_name;'''

req4 = '''select singer_name 
          from singers
               join singeralbum USING(singer_id)
                    join albums USING(album_id)
          where singer_name not in (select singer_name where album_year = 2020);'''

req5 = '''select singer_name, compilation_name 
          from singers
               join singeralbum USING(singer_id)
                    join albums USING(album_id)
                         join tracks USING(album_id)
                              join compilationtrack USING(track_id)
                                   join compilations USING(compilation_id)
          where singer_name = 'Basta';'''

req6 = '''SELECT album_name 
          FROM albums
               JOIN singeralbum USING(album_id)
                    JOIN singers USING(singer_id)
                         JOIN singergenre USING(singer_id)
          GROUP BY album_name
          HAVING count(genre_id) <> 1;'''

req7 = '''select track_name
          from tracks 
               left join compilationtrack USING(track_id)
          WHERE compilation_id is null;'''

req8 = '''select singer_name, track_name, track_time
          from singers
               join singeralbum using(singer_id)
                    join albums USING(album_id)
                         join tracks USING(album_id)
          where track_time = (select min(track_time) from tracks);'''

req9 = '''select album_name, count(track_id) count_track
          from albums
               join tracks USING(album_id)
          group by album_id
          having count(track_id) = (select count(track_id) 
                                    from tracks
                                    group by album_id
                                    order by count(track_id)
                                    limit 1);'''

if __name__ == '__main__':
    db = 'postgresql://dima:1242@localhost:5432/music'
    engine = sqlalchemy.create_engine(db)
    conn = engine.connect()
    print(*req_to_tab(req6), sep='\n')