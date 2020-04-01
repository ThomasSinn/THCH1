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
        impData.append({
            "name" : each['name'].replace("'", "%27"),
            "opening_hours" : each['opening_hours']['open_now'],
            "photopath" : each['photos'][0]['photo_reference']
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



#image download from 'places api' and saves them to photos folder
#issue downloads empty images 
def getImages(googleItem):
    print('\n get images started\n')
    for each in googleItem:
        ref = each['photo_reference']
        r = requests.get('https://maps.googleapis.com/maps/api/place/photo?maxwidth=900&photoreference='+ ref +'&key=' + AUTH_KEY, stream=True)

        with open("static/photos/" + each['photo_reference'] + ".jpg", "wb") as fd:
            for chunk in r.iter_content(chunk_size=128):
                shutil.copyfileobj(r.raw, fd)
            fd.close()
    print("\n link to be saved: " + "static/photos/" + each['photo_reference'] + ".jpg")
    return ("static/photos/" + each['photo_reference'] + ".jpg")


#gps coords for UNSW
#need to get this from the front end
testobj = locationOBJ(-33.917329664, 151.225332432, 2000) 
getrestuarants(testobj)


#code which may be integrated later on.
# def threadedUpdate(ResList):
#     conn = sqlite3.connect('database')
#     cursor = conn.cursor()

#     print('\n threaded updater running\n ')
#     #most dangerous way possible to manage a database, but she'll be right
#     query = "INSERT INTO restuarants VALUES(%s, %s, %s)"
    
#     print(str(ResList[0]['name']), str(ResList[0]['opening_hours']['open_now']), str(getImages(ResList[0]['photopath'])))

#     for each in ResList:
#         #print(each['name'], each['opening_hours'])
#         conn.execute(query, (str(each['name']), str(each['opening_hours']['open_now']), str(getImages(each['photopath']))))
    
#     return True