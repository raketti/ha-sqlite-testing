# Home Assistant - SQLite - Testing

Test repo for SQLite and Home Assistant

### TODO List:

- [x] Upload test database from:
  - https://www.sqlitetutorial.net/sqlite-sample-database/
- [x] Create a Python program to read database
- [x] Get latest temperature from Home Assistant SQLite DB
- [ ] Calculate the average temperature for the last ```n = 7 x 24``` measurements
  - [ ] We need to find a way to ignore following states:
    - ``` unavailable ```
    - ``` unknown ```
- [ ] Manipulate the data in the Python program
- [ ] Write new data to the database 


### Home Assistant stuff:
- [x] Get snapshot of HA database
- We get this data from the database:
  - states_meta table
    - metadata_id: 220 for Outside temperature
    - entity_id: <entity_id>

- Based on that, we can find the temperature values
  - states table
    - metadata_id: 220
    - state: <temperature>
    - last_updated_ts
      - <s>There's an issue, we have for example 1684522055.67595 in the database
      - This doesn't match current time, however 1684522055675.95 does</s>
      - So, the time is not in milliseconds, but seconds since epoch, so we need something like:
        ```
        last_updated_ts = 1684522055.67595

        last_updated_ts = time.strftime("%Y.%m.%d %H:%M:%S")
        ```
      - This gives us ```2023.05.22 08:14:29```

- We can get the mean value
  - statistics table
    - MetadataId: 71
    - Min / Max / Mean
