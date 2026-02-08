import sqlite3
from config import DB_FILE

conn = sqlite3.connect(DB_FILE, check_same_thread=False)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS players (
    user_id INTEGER PRIMARY KEY,
    name TEXT,
    games_played INTEGER DEFAULT 0,
    games_won INTEGER DEFAULT 0
)
""")

conn.commit()


def register_player(user_id: int, name: str):
    cur.execute(
        "INSERT OR IGNORE INTO players (user_id, name) VALUES (?, ?)",
        (user_id, name)
    )
    conn.commit()
