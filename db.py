import sqlalchemy
from pprint import pprint

db = 'postgresql://postgres:1242@localhost:5432/music'
engine = sqlalchemy.create_engine(db)
conn = engine.connect()

sel = conn.execute(
"""
SELECT * FROM genres;
""").fetchall()
pprint(sel)