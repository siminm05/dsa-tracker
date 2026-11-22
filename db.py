import sqlite3
from contextlib import closing

DB_PATH = "tracker.db"

def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def query(sql, params=()):
    with closing(get_conn()) as conn:
        return conn.execute(sql, params).fetchall()

def execute(sql, params=()):
    with closing(get_conn()) as conn:
        with conn:
            conn.execute(sql, params)

def init_db():
    execute("CREATE TABLE IF NOT EXISTS problems (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, topic TEXT NOT NULL, difficulty TEXT NOT NULL, date_solved TEXT NOT NULL, review_count INTEGER NOT NULL DEFAULT 0, next_review TEXT NOT NULL)")