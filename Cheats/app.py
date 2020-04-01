#Python 3.7 controller 
#uberch'eats project


from flask import Flask, render_template, request
from dbInterface import CreateLoc, ParseDB
import json

from flask import Flask, render_template, request, jsonify
app = Flask(__name__, static_folder='static/scripts', template_folder='static/pages')

#Home Page
@app.route('/')
def landingPage():
    return render_template('index.html')

"""
#this route will produce a screen of cards which relate to the
#search terms.
@app.route('/search/<searchterms>')
def search(searchterms):
    print(searchterms) #prints the terms passed from the index
    return render_template('searchpage.html')

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



@app.route('/shit', methods=['GET'])
def tester():
    print('TESTING')
    return jsonify(result="find an island")
 
 
 if __name__ == "__main__":
    app.run()
