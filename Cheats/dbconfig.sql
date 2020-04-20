CREATE TABLE restaurants( 
    RID integer PRIMARY KEY,
    name varchar(255),
    open boolean NOT NULL,
    photoPath varchar(255),
    rating float,
    lat float, 
    lng float
);


CREATE TABLE gigPricing(
    PID integer PRIMARY KEY,
    RID integer,
    service varchar(30), 
    price integer,
    FOREIGN KEY (RID) REFERENCES restaurants(RID)
);