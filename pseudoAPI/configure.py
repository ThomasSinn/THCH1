#sets up the database with dumby data.
import sqlite3
import sys

conn = sqlite3.connect('API')

italianList = ["Pizza", "Lasagna", "Garlic Bread", "Salad"]
indianList = ['Tika Masala', 'Lamb Rogan Josh', 'Butter Chicken', 'Naan Bread', 'Basamati Rice', 'Jasmine Rice']
chineseList = ['Northern Style Dumplings', 'Southern Style Dumplings', 'Chicken Fried Rice']
cafeList = ['Muffin', 'Bacon and Egg Roll', 'Flat White Coffee', 'English Breakfast Tea']

italianKeywords = ["pizza", "italian", "italy", "pasta"]
indianKeywords = ["india", "curry", "naan", "punjab"]
chineseKeywords = ["chinese", "china"]

# default to cafe if no keywords detected

megaList = {
    "italian" : (italianList, italianKeywords),
    "indian" : (indianList, indianKeywords),
    "chinese" : (chineseList, chineseKeywords),
    "cafe" : (cafeList, None)
}

cur = conn.cursor()

#This will handle the google functions which interface with the api
# the script will get resturants near a specified location 

import urllib, json
import urllib.request
import sqlite3
import threading
import requests
import shutil
import random

#google key -> global scope as it is used in multiple functions
AUTH_KEY = "AIzaSyDHAlJ2Qs0KBhp4gWuJ2tl1JcNkwVvf5w4"

location = ""

class locationOBJ:
    #range is in meters
    def __init__(self, latitude, longtitude, range):
        self.longtitude = longtitude 
        self.latitude = latitude
        self.range = range

def setuprestaurants(locationobject):
    #making the http request
    location = str(locationobject.latitude) + "," + str(locationobject.longtitude)
    radius = locationobject.range
    types = "meal_takeaway" #google defined keyword
    MyUrl = ('https://maps.googleapis.com/maps/api/place/nearbysearch/json'
           '?location=%s'
           '&radius=%s'
           '&types=%s'
           '&sensor=false&key=%s') % (location, radius, types, AUTH_KEY)

    response = urllib.request.urlopen(MyUrl)
    jsonRaw = response.read()
    jsonData = json.loads(jsonRaw)
    #print(jsonData) 

    impData = []
    for each in jsonData['results']:

        name = each['name'].replace("'", "\'")
        
        location = each['geometry']['location']

        lat = location['lat']
        lng = location['lng']

        keyword = "cafe"

        for i, k in megaList.items():
            if k[1]:
                for kw in k[1]:
                    if kw in name.lower():
                        keyword = i

        # keyword = random.choice(list(megaList.keys()))

        itemlist = megaList[keyword][0]

        for i in itemlist:
            for service in ["Uber", "Easi", "Deliveroo", "Menulog"]:
                price = random.randint(100, 2000)
                conn.execute(
                ("INSERT INTO FOOD VALUES(NULL, \"{r_name}\", {lat}, {lng}, '{name}', '{service}', {price})").format(\
                    r_name=each['name'],\
                    lat=lat,\
                    lng=lng,\
                    name=i,\
                    service=service,\
                    price=price))
            conn.commit()

    return impData

conn.execute("DROP TABLE IF EXISTS FOOD")
conn.execute("""CREATE TABLE food(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    r_name varchar(256) NOT NULL,
    r_lat decimal(3, 7),
    r_lng decimal(3, 7),
    name varchar(256) NOT NULL,
    service varchar(256) NOT NULL,
    price int NOT NULL)""")
conn.commit()

setuprestaurants(locationOBJ(-33.8635466, 151.1882907, 1000000))

conn.close()