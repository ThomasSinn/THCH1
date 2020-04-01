#Python 3.7 controller 
#uberch'eats project

from flask import Flask, render_template, request
from dbInterface import CreateLoc, ParseDB
import json

from flask import Flask, render_template, request, jsonify
app = Flask(__name__, static_folder='static/scripts', template_folder='static/pages')

#Home Page
@app.route('/', methods=["GET", "POST"])
def landingPage():
    if request.method == "POST":
        searchtext = request.form.get("search")

#this route will produce a screen of cards which relate to the
#search terms.
@app.route('/search/<searchterms>')
def search(searchterms):
    print(searchterms) #prints the terms passed from the index
    return render_template('searchpage.html')

    cur1 = conn.cursor()

    cur1.execute(f"""
    SELECT NAME FROM RESTAURANTS
    WHERE NAME LIKE '%{searchtext}%'
    ;
    """)

    for row in cur1.fetchall():
        results += [row[0]]

    return render_template('searchpage.html', results=results)



# #should be the actual comparison of the gig economy pricing
# @app.route('/store/<storeid>')
# def compare():
#     return render_template('comparepage.html')

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
 
 
# if __name__ == "__main__":
#     app.run()
