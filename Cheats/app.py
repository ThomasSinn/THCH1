#Python 3.7 controller 
#uberch'eats project

from flask import Flask, render_template, request, redirect, url_for
from dbInterface import CreateLoc, ParseDB
import json
import db

app = Flask(__name__, static_folder='static/scripts', template_folder='static/pages')

#Home Page
@app.route('/', methods=["GET", "POST"])
def landingPage():
    if request.method == "POST":
        searchtext = request.form.get("search")

        return redirect(url_for('searchPage', searchtext=searchtext))
    else:
        return render_template('index.html')

@app.route('/search/<searchtext>', methods=["GET", "POST"])
def searchPage(searchtext):
    results = []

    conn = db.connect()

    cur1 = conn.cursor()

    cur1.execute(f"""
    SELECT NAME FROM RESTAURANTS
    WHERE NAME LIKE '%{searchtext}%'
    ;
    """)

    for row in cur1.fetchall():
        results += [row[0]]

    return render_template('searchpage.html', results=results)
"""
#should be the actual comparison of the gig economy pricing
@app.route('/store/<storeid>')
def compare():
    return render_template('store.html')
"""

#needs to be passed a jsonified geolocation
#database is also populated through this method
@app.route('/GetDB', methods=['POST'])
def dbOut():
    content = request.json
    print(content)
    CreateLoc(content)
    print("about to return in dbOut")
    return ParseDB()
 
 
if __name__ == "__main__":
    app.run()
