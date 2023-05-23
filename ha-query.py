import sqlite3
from sqlite3 import Error
from statistics import mean

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
  cur.execute("SELECT * FROM statistics_meta WHERE statistic_id=?", (entityID,)) # Change to statistics_meta table
  
  rows = cur.fetchall()

  for row in rows:
    metadataID = row[0] # this will link the data from the states table

  cur = conn.cursor()  
  temp_rows = cur.execute('SELECT * FROM statistics WHERE metadata_id=? LIMIT 100', (metadataID,)).fetchall()[-1] # Use statistics table, as we get the mean value from there
#  temperature = last_row[4] # temperature mean value from last row, fifth column
#  print(temperature)

  temp_list = []
  for row in temp_rows:
    temperature = row[1] # temperature mean value from last row, fifth column
    temp_list.append(temperature)
#  print(temp_list)

  # Calculate the average of the temperatures
  sum_temp = sum(temp_list)
  temp_avg = sum_temp/len(temp_list)
  print(round(temp_avg,2))
  
def main():
  database = r"home-assistant_v2.db"

  # create a database connection
  conn = connect(database)
  with conn:
    entityID = "sensor.vilp_melcloud_outside_temperature"
    get_metadata_id_by_entity_id(conn, entityID)

if __name__ == '__main__':
    main()