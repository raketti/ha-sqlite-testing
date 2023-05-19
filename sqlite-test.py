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

  return conn

# Modified from:
# https://www.sqlitetutorial.net/sqlite-python/sqlite-python-select/

def select_all_genres(conn):
    """
    Query all rows in the genres table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM genres")

    rows = cur.fetchall()

    for row in rows:
        print(row)

def select_task_by_genre(conn, genreid):
    """
    Query tasks by GenreId
    :param conn: the Connection object
    :param genreid:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM genres WHERE GenreId=?", (genreid,))

    rows = cur.fetchall()

    for row in rows:
        print(row)

def main():
    database = r"chinook.db"

    # create a database connection
    conn = connect(database)
    with conn:
        genre_id = input("1. Query task by GenreId (1-25):")
        select_task_by_genre(conn, genre_id)

        print("2. Query all tasks")
        select_all_genres(conn)

if __name__ == '__main__':
    main()