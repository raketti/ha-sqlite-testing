import sqlite3
from sqlite3 import Error

entityID = "sensor.vilp_melcloud_outside_temperature"
metadataID = ""

def connect(database):
  conn = None
  try:
    conn = sqlite3.connect(database)
    print("Connection succesful!")
  except Error as e:
    print(e)

  return conn

def get_metadata_id_by_entity_id(conn, entityID):
  """
  Query metadata_id by entity_id
  :param conn: the Connection object
  :param entityID: HA entity_id to fetch
  :return:
  """
  cur = conn.cursor()
  cur.execute("SELECT * FROM states_meta WHERE entity_id=?", (entityID,))
  
  rows = cur.fetchall()

  for row in rows:
    metadataID = row[0] # this will link the data from the states table

  cur = conn.cursor()  
  last_row = cur.execute('SELECT * FROM states WHERE metadata_id=?', (metadataID,)).fetchall()[-1]
  temperature = last_row[3] # temperature value from last row, fourth column
  print(temperature)
    
def main():
  database = r"home-assistant_v2.db"

  # create a database connection
  conn = connect(database)
  with conn:
    entityID = "sensor.vilp_melcloud_outside_temperature"
    get_metadata_id_by_entity_id(conn, entityID)

if __name__ == '__main__':
    main()