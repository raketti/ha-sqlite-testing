# From: https://www.sqlitetutorial.net/sqlite-python/creating-database/

import sqlite3
from sqlite3 import Error
from statistics import mean

def connect(db_file):
  conn = None
  try:
    conn = sqlite3.connect(db_file)
  except Error as e:
    print(e)

  return conn

# Modified from:
# https://www.sqlitetutorial.net/sqlite-python/sqlite-python-select/

def select_all_songs_from_album(conn, albumID):
  cur = conn.cursor()
  cur.execute("SELECT * FROM tracks WHERE AlbumID=? LIMIT 5", (albumID,))

  rows = cur.fetchall()

  temp_list = []
  for row in rows:
    temperature = row[0] # Track numbers
    temp_list.append(temperature)

  print(temp_list)
  sum_temp = sum(temp_list)
  temp_avg = sum_temp/len(temp_list)
  print("Average value of temperature:\n")
  print(round(temp_avg,2))

def main():
  database = r"chinook.db"

  # create a database connection
  conn = connect(database)
  with conn:
    print("All track numbers based on albumID")
    select_all_songs_from_album(conn, albumID=1) # Hardcode albumID for testing purposes

if __name__ == '__main__':
  main()