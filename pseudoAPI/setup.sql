/*Creates tables and inserts data into the database for testing purposes*/

CREATE TABLE food(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    item_name varchar(200) NOT NULL,
    cuisine varchar(40) NOT NULL
)

