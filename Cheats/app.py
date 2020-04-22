#Python 3.7 controller 
#uberch'eats project

from flask import Flask, render_template, request, redirect, url_for, jsonify
#from flask_cors import CORS
from dbInterface import CreateLoc, ParseDB, dbPrice
import db
import json
import sqlite3
from exchange import get_exchange

from flask import Flask, render_template, request, jsonify
app = Flask(__name__, static_folder='static/scripts', template_folder='static/pages')
#CORS(app)

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

    cur1.execute(f"""SELECT NAME, PHOTOPATH, RID, rating, lat, lng FROM restaurants WHERE {where}""")

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

@app.route('/ridlatlong/<rid>')
def getLatLong(rid):
    conn = db.connect()
    cur = conn.cursor()
    cur.execute("select lat, lng from restaurants where RID={}".format(int(rid)))
    result = cur.fetchone()
    cur.close()
    return jsonify({"lat" : result[0], "lng" : result[1]})

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
 
if __name__ == "__main__":
    #getPrices()
    get_exchange()
    app.run()
    #print('=============================================================================')
