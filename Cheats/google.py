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

class locationOBJ:
    #range is in meters
    def __init__(self, latitude, longtitude, range):
        self.longtitude = longtitude 
        self.latitude = latitude
        self.range = range

def getrestuarants(locationobject):
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
        print(each)
        print("\n")

        name = each['name'].replace("'", "%27")
        opening_hours = each['opening_hours']['open_now']

        try:
            photopath = imageURL(each['photos'][0]['photo_reference'])
        except KeyError:
            photopath = None
        except NameError:
            photopath = None
        
        impData.append({
            "name" : name,
            "opening_hours" : opening_hours,
            "photopath" : photopath
        })
        

       
    #include threading here later to prevent blocking function call. 
    #very ineffiecent atm
    for each in impData:
        InsertDB(each)

    return impData


def InsertDB(JSONelement):
    #print(JSONelement)
    conn = sqlite3.connect('database')
    cursor = conn.cursor()

    print(("INSERT INTO restaurants VALUES({name}, {open}, {photo})").format(name=JSONelement['name'], open=JSONelement['opening_hours'], photo=JSONelement['photopath']))

    conn.execute(
    ("INSERT INTO restaurants VALUES(NULL, '{name}', {open}, '{photo}', {price})").format(name=JSONelement['name'], open=JSONelement['opening_hours'], photo=JSONelement['photopath'], price=random.randint(0, 15)))

    conn.commit()
    print('executed and commited')
    conn.close()

#takes a reference ID a returns the URL
#this url will have to be changed to the source of any cards we use.
def imageURL(refID):
    url = "https://maps.googleapis.com/maps/api/place/photo?maxwidth=600&maxheight=800&photoreference=" + refID + "&key=" + AUTH_KEY
    return url