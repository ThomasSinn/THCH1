/*Creates tables and inserts data into the database for testing purposes*/

CREATE TABLE food(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    r_name varchar(256) NOT NULL,
    r_lat decimal(3, 7),
    r_lng decimal(3, 7),
    name varchar(256) NOT NULL,
    service varchar(256) NOT NULL,
    price int NOT NULL
)

