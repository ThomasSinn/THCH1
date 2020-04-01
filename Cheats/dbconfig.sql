CREATE TABLE restaurants ( 
    RID integer PRIMARY KEY,
    name varchar(255),
    open boolean NOT NULL,
    photoPath varchar(255),
    price integer NOT NULL
);
