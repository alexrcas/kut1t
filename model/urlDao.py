import sqlite3

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


def listUrls():
    conn = get_db_connection()
    urls = conn.execute('SELECT * FROM redirect').fetchall()
    conn.close()
    return urls;


def saveUrl(url):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO redirect (url) VALUES (?)",((url,)))
    conn.commit()

    urls = conn.execute('SELECT * FROM redirect').fetchall()
    conn.close()

    return urls[-1];


def get(id):
    conn = get_db_connection()
    url = conn.execute('SELECT * FROM redirect WHERE id = ?', (id,)).fetchall()
    conn.close()
    return url