import sqlite3
from google import getrestuarants, locationOBJ
import json


def CreateLoc(geodata):
    #range case can be changed if the front allows for range alterations
    #default value is 2000 meters
    newOBJ = locationOBJ(geodata['latitude'], geodata['longitude'], 2000)
    getrestuarants(newOBJ)
    print('location passed and database populated')

#Front end access point to get all data in the database
def ParseDB():
    conn = sqlite3.connect('database')
    cur = conn.cursor()
    cur.execute("SELECT * FROM restaurants;")
    result = cur.fetchall()
    conn.commit()
    result = json.dumps(result)
    return result

#get prices for the front end

'''
CREATE TABLE restaurants(
    RID integer PRIMARY KEY,
    name varchar(255),
    open boolean NOT NULL,
    photoPath varchar(255)
);
CREATE TABLE gigPricing(
    PID integer PRIMARY KEY,
    RID integer,
    service varchar(30),
    price integer,
    FOREIGN KEY (RID) REFERENCES restaurants(RID)
);
'''
def dbPrice():
    conn = sqlite3.connect('database')
    cur = conn.cursor()
    cur.execute("SELECT * FROM gigPricing")
    result = cur.fetchall()
    conn.commit()
    result = json.dumps(result)
    return result 


