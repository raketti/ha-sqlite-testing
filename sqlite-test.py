# From: https://www.sqlitetutorial.net/sqlite-python/creating-database/

import sqlite3
from sqlite3 import Error

def connect(db_file):
  conn = None
  try:
    conn = sqlite3.connect(db_file)
    print(sqlite3.version)
  except Error as e:
    print(e)
  finally:
    if conn:
      conn.close()

if __name__ == '__main__':
    connect(r"chinook.db")