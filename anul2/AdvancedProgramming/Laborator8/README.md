# Laboratory 8

### Compulsory (1p)

- [x] Create a relational database using any RDBMS (Oracle, Postgres, MySql, Java DB, etc.).
- [x] Write an SQL script that will create the following tables:
  - countries: id, name, code, continent
  - continents: id, name
- [x] Update pom.xml, in order to add the database driver to the project libraries.
- [x] Create a singleton class in order to manage a connection to the database.
- [x] Create DAO classes that offer methods for creating countries and continents, and finding them by their ids and names;
- [x] Implement a simple test using your classes.

### Homework (2p)
- [x] Create the necessary table in order to store cities in your database. A city may contain: id, country, name, capital(0/1), latitude, longitude
- [x] Create an object-oriented model of the data managed by the application.
- [x] Create a tool to import data from a real dataset: World capitals gps or other.
- [x] Display the distances between various cities in the world.
- [ ] (+1p) Create a 2D map (using Swing or JavaFX) and draw on it the cities at their corresponding locations.