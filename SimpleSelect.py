import sqlalchemy


def req_to_tab(req):
    return conn.execute(f'''{req}''').fetchall()


req1 = '''SELECT album_name, album_year FROM albums 
          WHERE album_year=2018;'''

req2 = '''SELECT track_name, track_time FROM tracks 
          WHERE track_time = (select max(track_time) from tracks);'''

req3 = '''SELECT track_name, track_time FROM tracks 
          WHERE track_time >= 210;'''

req4 = '''SELECT compilation_name FROM compilations 
          WHERE compilation_year >= 2018 AND compilation_year <= 2020;'''

req5 = '''SELECT singer_name FROM singers 
          WHERE singer_name NOT LIKE '%% %%';'''

req6 = '''SELECT track_name FROM tracks 
          WHERE track_name ILIKE '%%you%%' OR track_name ILIKE '%%ты%%';'''

if __name__ == '__main__':
    db = 'postgresql://dima:1242@localhost:5432/music'
    engine = sqlalchemy.create_engine(db)
    conn = engine.connect()
    print(*req_to_tab(req6), sep='\n')

