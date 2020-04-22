import urllib, json
import urllib.request

#Returns a dictionary of rates to exchange rates
def get_exchange():
    MyUrl = ('https://api.exchangeratesapi.io/latest?base=AUD&symbols=USD,GBP,JPY,CNY,NZD,EUR')
    response = urllib.request.urlopen(MyUrl)
    jsonRaw = response.read()
    jsonData = json.loads(jsonRaw)
    rates = jsonData["rates"]
    return rates

"""
rates = {
    "EUR" : 13987132
    "GBP" : 238394 
    etc 
}

"""