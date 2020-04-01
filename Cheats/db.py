import sqlite3
def connect():
    conn = None
    try:
        conn = sqlite3.connect("database")
        conn.set_client_encoding('UTF8')
    except Exception as e:
        print("Unable to connect to the database")
        print(e)
    return conn