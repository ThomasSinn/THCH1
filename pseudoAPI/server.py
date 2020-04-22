#needs to be started using 'flask run --port 4888'
import sys
from flask import Flask
from flask_cors import CORS
import sqlite3
import json
import random


app = Flask(__name__)
CORS(app)

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
    app.run()