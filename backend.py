import sqlite3
import sys

def connect():
    conn = sqlite3.connect("storage.db")
    conn.commit()
    conn.close()
    
def create():
    conn = sqlite3.connect("storage.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS notes (title TEXT, note TEXT)")
    conn.commit()
    conn.close()
    
def insert_val(title, note):
    conn = sqlite3.connect("storage.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO notes VALUES (?,?)", (title, note))
    conn.commit()
    conn.close()
    
def det(title):
    conn = sqlite3.connect("storage.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM notes WHERE title=? ", (title,)) 
    conn.commit()
    conn.close()
    
def close():
    sys.exit()
    