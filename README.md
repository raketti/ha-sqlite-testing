# Home Assistant - SQLite - Testing

Test repo for SQLite and Home Assistant

### TODO List:

- [x] Upload test database from:
 - https://www.sqlitetutorial.net/sqlite-sample-database/
- [ ] Create a simple Python program to read database
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
      - There's an issue, we have for example 1684522055.67595 in the database
      - This doesn't match current time, however 1684522055675.95 does

- We can get the mean value
  - statistics table
    - MetadataId: 71
    - Min / Max / Mean