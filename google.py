#This will handle the google functions which interface with the api
# the script will get resturants near a specified location 

import urllib, json
import urllib.request

class locationOBJ:
    #range is in meters
    def __init__(self, latitude, longtitude, range):
        self.longtitude = longtitude 
        self.latitude = latitude
        self.range = range


def getrestuarants(locationobject):
    #making the http request
    AUTH_KEY = "AIzaSyDHAlJ2Qs0KBhp4gWuJ2tl1JcNkwVvf5w4"
    location = str(locationobject.latitude) + "," + str(locationobject.longtitude)
    radius = locationobject.range
    types = "meal_takeaway" #google defined keyword
    MyUrl = ('https://maps.googleapis.com/maps/api/place/nearbysearch/json'
           '?location=%s'
           '&radius=%s'
           '&types=%s'
           '&sensor=false&key=%s') % (location, radius, types, AUTH_KEY)
    print(MyUrl)
    response = requests.urlopen(MyUrl)
    jsonRaw = response.read()
    jsonData = json.loads(jsonRaw)

    impData = []

    for each in jsonData['results']:
        impData.append(each['name'])
    
    return impData

testobj = locationOBJ(-33.917329664, 151.225332432, 2000) 
print(getrestuarants(testobj))