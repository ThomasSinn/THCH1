#This will handle the google functions which interface with the api
# the script will get resturants near a specified location 

import urllib, json
import urllib.request
import sqlite3
import threading
import requests
import shutil
import random
from HelperFunction import FakeOrders

#google key -> global scope as it is used in multiple functions
AUTH_KEY = "AIzaSyDHAlJ2Qs0KBhp4gWuJ2tl1JcNkwVvf5w4"

location = ""

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

        name = each['name'].replace("'", "''")
        opening_hours = each['opening_hours']['open_now']

        try:
            photopath = imageURL(each['photos'][0]['photo_reference'])
        except KeyError:
            photopath = None
        except NameError:
            photopath = None
        
        rating = each['rating']
        location = each['geometry']['location']

        impData.append({
            "name" : name,
            "opening_hours" : opening_hours,
            "photopath" : photopath,
            "rating" : rating,
            "lat" : location['lat'],
            "lng" : location['lng']
        })
        

       
    #include threading here later to prevent blocking function call. 
    #very ineffiecent atm
    for each in impData:
        InsertDB(each)

    return impData

#needs to be modified to support more attributes(ratings and distance)
def InsertDB(JSONelement):
    #print(JSONelement)
    conn = sqlite3.connect('database')
    cursor = conn.cursor()

    print(("INSERT INTO restaurants VALUES({name}, {open}, {photo}, {rating}, {lat}, {lng})").format(name=JSONelement['name'], open=JSONelement['opening_hours'], photo=JSONelement['photopath'], rating=JSONelement['rating'], lat=JSONelement['lat'], lng=JSONelement['lng']))

    conn.execute(
    ("INSERT INTO restaurants VALUES(NULL, '{name}', {open}, '{photo}', {rating}, {lat}, {lng})").format(name=JSONelement['name'], open=JSONelement['opening_hours'], photo=JSONelement['photopath'], rating=JSONelement['rating'], lat=JSONelement['lat'], lng=JSONelement['lng']))
    conn.commit()
    conn.close()
    print('gets through insert phase')
    #creates fake pricing for orders
    FakeOrders(JSONelement['name'])
    print('executed and commited')

#takes a reference ID a returns the URL
#this url will have to be changed to the source of any cards we use.
def imageURL(refID):
    url = "https://maps.googleapis.com/maps/api/place/photo?maxwidth=600&maxheight=800&photoreference=" + refID + "&key=" + AUTH_KEY
    return url

#uses maps api to get the distance to the restaurant 
# def getDistance(lat, lng):
#     request = "https://maps.googleapis.com/maps/api/distancematrix/json?units=metirc&origins="
#     print("this is the location of the user" + location)
#     modLoc = location

#     modLoc = modLoc.replace("'", "|")
#     request = request + modLoc
#     request = request + "destinations=" + str(lat) + ',' + str(lng)
#     request = request + "&key=" + AUTH_KEY
#     print('\n')
#     print('location query')
#     print(request)

#     response = urllib.request.urlopen(request)
#     print(response)
#     return response
