#Python 3.7 controller 
#uberch'eats project

from flask import Flask, render_template, request, redirect, url_for
#from flask_cors import CORS
from dbInterface import CreateLoc, ParseDB, dbPrice
import db
import json
import sqlite3

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


#this route will produce a screen of cards which relate to the
#search terms.
@app.route('/search/<searchterms>')
def search(searchterms):
    print(searchterms) #prints the terms passed from the index
    #return render_template('searchpage.html')
    conn = db.connect()
    cur1 = conn.cursor()

    cur1.execute(f"""
    SELECT NAME, PHOTOPATH, RID, rating, lat, lng FROM RESTAURANTS
    WHERE NAME LIKE '%{searchterms}%'
    ;
    """)

    results = []
    #needs to modified to include distance. 
    for row in cur1.fetchall():
        #print(getDistance(row[4], row[5]))
        results += [{
            "name": row[0],
            "photopath" : row[1],
            "id" : row[2],
            "rating" : row[3],
            "lat" : row[4],
            "lng" : row[5]
        }]

    return render_template('searchpage.html', results=results)

# #should be the actual comparison of the gig economy pricing
@app.route('/store/<storeid>')
def compare(storeid):
    print("storeID route hit: " + str(storeid))
    conn = db.connect()
    cur = conn.cursor()
    cur.execute("select * from restaurants where RID={}".format(int(storeid)))
    result = cur.fetchall()
    print("\n")
    print(result)
    print("\n")
    return render_template('comparepage.html', storeInfo=result)


@app.route('/prices', methods=['GET'])
def getPrices():
    print(dbPrice())
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
 
 
if __name__ == "__main__":
    #getPrices()
    app.run()
    #print('=============================================================================')
