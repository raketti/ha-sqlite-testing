# Home Assistant - SQLite - Testing

Test repo for SQLite and Home Assistant

### TODO List:

- [x] Upload test database from:
  - https://www.sqlitetutorial.net/sqlite-sample-database/
- [x] Create a Python program to read database
- [x] Get latest temperature from Home Assistant SQLite DB
- [ ] <s>We need to find a way to ignore following states:</s>

   <s> - ``` unavailable ```</s>

   <s> - ``` unknown ```</s>

- [x] Get the data from statistics table to get the mean value
- [x] Append the values to a list
- [x] Calculate the average temperature for the last ```n = 7 x 24``` measurements
- Write new data to
  - [ ] The database
  - [ ] A sensor in Home Assistant 


### Home Assistant stuff:
- [x] Get snapshot of HA database
- We get this data from the database ```statistics_meta``` table
  - metadata_id: 71 for Outside temperature

- Based on that, we can find the temperature values from ```statistics``` table
  - metadata_id: 71
  - mean: mean_temperature, FLOAT
