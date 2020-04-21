CREATE TABLE restaurants( 
    RID integer PRIMARY KEY,
    name varchar(255),
    open boolean NOT NULL,
    photoPath varchar(255),
    rating float,
    lat decimal(3, 7),
    lng decimal(3, 7)
);

CREATE TABLE menuitems(
    RID integer PRIMARY KEY,
    name varchar(255),
    photoPath varchar(255),
    priceCents integer,
);

CREATE TABLE gigPricing(
    PID integer PRIMARY KEY,
    RID integer,
    service varchar(30), 
    price integer,
    FOREIGN KEY (RID) REFERENCES restaurants(RID)
);