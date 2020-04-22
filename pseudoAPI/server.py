<<<<<<< HEAD
#needs to be started using 'flask run --port 4888'
import sys
from flask import Flask
import sqlite3
import json
import random

app = Flask(__name__)

#returns pricing of cuisine for each service. 
@app.route('/menuPricing/<cuisine>')
def handler(cuisine):
    cur = sqlite3.connect('API').cursor()
    return json.dumps(GenPriceService(cur.execute("SELECT item_name from food where cuisine = '{}'".format(cuisine)).fetchall()))


def GenPriceService(ItemsList):
    
    itemsformat = []
    for each in ItemsList:
        itemsformat.append(each[0])
    
    itemsPrice = []
    for each in itemsformat:
        services = []
        services.append({"service" : "Uber" , "price" : (random.randint(100, 2000)/100)})
        services.append({"service" : 'Deliveroo', "price" : (random.randint(100, 2000)/100)})
        services.append({"service": 'Easi', "price" : (random.randint(100, 2000)/100)})
        services.append({"service" : 'Menulog', "price" : (random.randint(100, 2000)/100)})
        itemsPrice.append({"item" : each, "prices" : services})

    print(itemsPrice)
    return itemsPrice


if __name__ == "__main__":
=======
#needs to be started using 'flask run --port 4888'
import sys
from flask import Flask, request, jsonify
from flask_cors import CORS
import urllib
import sqlite3
import json
import random


app = Flask(__name__)
CORS(app)

@app.route('/menuPricing/', methods=['GET'])
def handler():
    query_parameters = request.args

    try:
        latitude = float(query_parameters.get('lat'))
        longitude = float(query_parameters.get('lng'))
    except:
        pass
    # name = query_parameters.get('name')

    cur = sqlite3.connect('API').cursor()

    itemlist = cur.execute(f"SELECT name, service, price from food where r_lat = '{latitude}' AND r_lng = '{longitude}'").fetchall()

    return jsonify(GenPriceService(itemlist))


def GenPriceService(ItemsList):

    itemsdict = {}
    itemsPrice = []

    for row in ItemsList:
        if row[0] not in itemsdict:
            itemsdict[row[0]] = {}

        if row[1] not in itemsdict[row[0]]:
            itemsdict[row[0]][row[1]] = row[2]

    for i, k in itemsdict.items():
        services = []
        for j, l in k.items():
            services += [{"service" : j, "price" : l}]

        itemsPrice += [{"item" : i, "prices" : services}]
    
    # itemsformat = []
    # for each in ItemsList:
    #     itemsformat.append(each[0])
    
    # itemsPrice = []
    # for each in itemsformat:
    #     services = []
    #     services.append({"service" : "Uber" , "price" : (random.randint(100, 2000)/100)})
    #     services.append({"service" : 'Deliveroo', "price" : (random.randint(100, 2000)/100)})
    #     services.append({"service": 'Easi', "price" : (random.randint(100, 2000)/100)})
    #     services.append({"service" : 'Menulog', "price" : (random.randint(100, 2000)/100)})
    #     itemsPrice.append({"item" : each, "prices" : services})

    return itemsPrice


if __name__ == "__main__":
>>>>>>> master
    app.run()