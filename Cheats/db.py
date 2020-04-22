import sqlite3
def connect():
    conn = None
    try:
        conn = sqlite3.connect("database")
    except Exception as e:
        print("Unable to connect to the database")
        print(e)
    return conn