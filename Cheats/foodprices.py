#make a function to get the food prices
# this is the route @app.route('/menuPricing/<cuisine>')
import urllib, json
import urllib.request


#What port the API is running on 
port = 5001
#change if we want more foods 
n_foods_in_grid = 4

def get_f_prices(cuisine):
    MyUrl = ('http://127.0.0.1:{}/menuPricing/{}'.format(port, str(cuisine)))
    response = urllib.request.urlopen(MyUrl)
    jsonRaw = response.read()
    jsonData = json.loads(jsonRaw)
    fPrices = []
    c = 0
    for i in jsonData:
        if c >= n_foods_in_grid: 
            break
        fPrices.append(i)

    return fPrices



'''
[{"item": "pizza", "prices": [{"service": "Uber", "price": 11.53}, {"service": "Deliveroo", "price": 12.54}, 
{"service": "Easi", "price": 14.34}, 
{"service": "Menulog", "price": 7.63}]},
 {"item": "lasagna", "prices": 
[{"service": "Uber", "price": 7.63}, {"service": "Deliveroo", "price": 2.2}, 
{"service": "Easi", "price": 15.61},
 {"service": "Menulog", "price": 8.48}]}, 
{"item": "garlic bread", "prices": [{"service": "Uber", "price": 6.16}, 
{"service": "Deliveroo", "price": 1.86}, 
{"service": "Easi", "price": 18.37}, 
{"service": "Menulog", "price": 13.04}]}, 
{"item": "salad", "prices": [{"service": "Uber", "price": 5.49}, {"service": "Deliveroo", "price": 15.61},
 {"service": "Easi", "price": 1.94}, {"service": "Menulog", "price": 17.5}]}]

[{
	"item": pizza
	"prices":[all the services(list of dictinoaries]
}]
'''