#needs to be started using 'flask run --port 4888'
import sys
from flask import Flask, request, jsonify
import sqlite3
import json
import random


app = Flask(__name__)

@app.route('/menuPricing/', methods=['GET'])
def handler():
    query_parameters = request.args

    latitude = query_parameters.get('lat')
    longitude = query_parameters.get('lng')
    name = query_parameters.get('name')

    cur = sqlite3.connect('API').cursor()
    itemlist = cur.execute(f"SELECT item_name, service, price from food where r_lat = '{latitude}' AND r_lng = '{longitude}' AND r_name = '{name}'").fetchall()
    return json.dumps(GenPriceService(itemlist))


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
        for j, l in k:
            services += {"service" : j, "price" : k}

        itemsPrice += {"item" : i, "prices" : services}
    
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
    app.run()