#Python 3.7 controller 
#uberch'eats project

from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_cors import CORS
from dbInterface import CreateLoc, ParseDB, dbPrice
import db
import json
import sqlite3
from exchange import get_exchange

from flask import Flask, render_template, request, jsonify
app = Flask(__name__, static_folder='static/scripts', template_folder='static/pages')
CORS(app)

#Home Page
@app.route('/', methods=["GET", "POST"])
def landingPage():
    if request.method == "POST":
        searchtext = request.form.get("search")
        return redirect(url_for('search', searchterms=searchtext))
    return render_template('index.html')

@app.route('/index', methods=["GET", "POST"])
def landingPage2():
    if request.method == "POST":
        searchtext = request.form.get("search")
        return redirect(url_for('search', searchterms=searchtext))
    return render_template('index.html')

#this route will produce a screen of cards which relate to the
#search terms.
@app.route('/search/<searchterms>')
def search(searchterms):
    print(searchterms) #prints the terms passed from the index
    #return render_template('searchpage.html')

    searchkws = searchterms.split()
    conn = db.connect()
    cur1 = conn.cursor()

    where = ""

    for kw in searchkws:
        where += f"NAME LIKE '%{kw}%' AND "

    if len(where) > 5:
        where = where[:-5]

    cur1.execute(f"""SELECT NAME, PHOTOPATH, RID, rating, lat, lng FROM RESTAURANTS WHERE {where}""")

    results = []
    #needs to modified to include distance. 
    for row in cur1.fetchall():
        #print(getDistance(row[4], row[5]))
        results += [{
            "name": row[0],
            "photopath" : row[1],
            "id" : row[2],
            "rating" : row[3],
            "lat" : float(row[4]),
            "lng" : float(row[5])
        }]

    return render_template('searchpage.html', results=results)

# #should be the actual comparison of the gig economy pricing
@app.route('/store/<storeid>')
def compare(storeid):
    print("storeID route hit: " + str(storeid))
    conn = db.connect()
    cur = conn.cursor()
    cur.execute("select * from restaurants where RID={}".format(int(storeid)))
    result = cur.fetchone()
    print("\n")
    print('ACTUAL COMPARISON OF GIG ECONOMY PRICING',result)
    print("\n")

    #formatting info to make it more usable for js
    resDict = {
        "id" : result[0],
        "name" : result[1],
        "open" : result[2],
        "photopath" : result[3],
        "rating" : result[4],
        "lat" : result[5],
        "lng" : result[6]
    }
    # resdict = json.dumps(resDict)
    # print(resDict)
    return render_template('comparepage.html', storeInfo=json.dumps(resDict))


@app.route('/prices', methods=['GET'])
def getPrices():
    print('some fake prices from DBPRICE', dbPrice())
    return dbPrice()

#needs to be passed a jsonified geolocation
#database is also populated through this method
@app.route('/GetDB', methods=['POST'])
def dbOut():
    content = request.json
    print(content)
    CreateLoc(content)
    print("about to return in dbOut")
    return ParseDB()

# @app.route('/shit', methods=['GET'])
# def tester():
#     print('TESTING')
#     return jsonify(result="find an island")

""" EXTRA PAGES """

#About page
@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')
    
#FAQ page 
@app.route('/faq', methods=['GET'])
def faq():
    return render_template('faq.html')

#Contact us page 
@app.route('/contact', methods=['GET'])
def contact():
    return render_template('contact.html')
 
<<<<<<< HEAD
@app.route('/LocalRestaurants', methods=['GET'])
def localrestaurants():
    latitude = request.GET.get('lat')
    longitude = request.GET.get('long')

    data = {
        {
            name : "Burger Foods",
            rating : 4,
            latitude : latitude,
            longitude : longitude,
            photopath : "https://source.unsplash.com/400x400/?burger",
            rid : 1015
        }
    }
    return JsonResponse(data)

@app.route('/GetMenu', methods=['GET'])
def getmenu():
    latitude = request.GET.get('rid')

    data = {
        {
            name : "Hamburger",
            costs : {
                "ubereats" : 500,
            }
        }
    }
    return JsonResponse(data)
 
#Route for index.js ajax call. 
@app.route('/getInfo', methods=['POST'])
def getStoreInfo():
    resList = request.json
    print('\n')
    print(resList)
    print('\n')
    resList = resList['ids']
    conn = db.connect()
    cur = conn.cursor()
    formattedList = []
    scannedIDs = []
    for each in resList:
        result = cur.execute("select * from restaurants where Rid={id}".format(id=each)).fetchone()
        if result[0] not in scannedIDs:
            resDict = {
                "id" : result[0],
                "name" : result[1],
                "open" : result[2],
                "photopath" : result[3],
                "rating" : result[4],
                "lat" : result[5],
                "lng" : result[6]
            }
            formattedList.append(resDict)
            scannedIDs.append(result[0])
    print('\n')
    print(formattedList)
    print('\n')
    formattedList = json.dumps(formattedList)
    return formattedList
    
        





=======
>>>>>>> 06262e3c3ea962f2e95822c701dc346b337ab010
if __name__ == "__main__":
    #getPrices()
    get_exchange()
    app.run()
    #print('=============================================================================')
