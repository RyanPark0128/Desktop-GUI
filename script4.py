import sqlite3


def connect():
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXIST book (id INTEGER PRIMARY KEY, title text, year integer, isbn integer)")
    conn.commit()
    conn.close()
