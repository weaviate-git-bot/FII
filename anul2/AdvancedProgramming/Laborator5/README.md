# Laboratory 5

### Compulsory (1p)

- [x] Create an object-oriented model of the problem. You should have at least the following classes: Catalog and Item. The items should have at least a unique identifier, a title and its location. Consider using an interface or an abstract class in order to describe the items in a catalog.
- [x] Implement the following methods representing commands that will manage the content of the catalog:
    - [x] add: adds a new entry into the catalog;
    - [x] toString: a textual representation of the catalog;
    - [x] save: saves the catalog to an external file using JSON format; you may use Jackson or other library;
    - [x] load: loads the catalog from an external file.

### Homework (2p)
- [x] Represent the commands using classes instead of methods. Use an interface or an abstract class in order to desribe a generic command.
- [x] Implement the commands load, list, view, report (create the classes AddCommand, ListCommand, etc.). 
  - [x] list: prints the list of items on the screen; 
  - [x] view: opens an item using the native operating system application (see the Desktop class); 
  - [x] report: creates (and opens) an HTML report representing the content of the catalog.
  Use a template engine such as FreeMarker or Velocity, in order to create the HTML report.
  - [ ] (+1p) Use Apache Tika in order to extract metadata from your catalog items and implement the command info in order to display them.
- [x] The application will signal invalid date or the commands that are not valid using custom exceptions.
- [x] The final form of the application will be an executable JAR archive. Identify the generated archive and launch the application from the console, using the JAR.