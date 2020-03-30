#scraper api for uber eats using beautiful soup api
import urllib
import requests
from bs4 import BeautifulSoup

def search(name):    
    # desktop user-agent
    USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"

    query = str(name)
    query = query.replace(' ', '+')
    URL = f"https://google.com/search?q={query}"

    headers = {"user-agent": USER_AGENT}
    resp = requests.get(URL, headers=headers)

    if resp.status_code == 200:
        soup = BeautifulSoup(resp.content, "html.parser")
        results = []
        for g in soup.find_all('div', class_='r'):
            anchors = g.find_all('a')
            if anchors:
                link = anchors[0]['href']
                title = g.find('h3').text
                item = {
                    "title": title,
                    "link": link
                }
                results.append(item)

        #ideally would confirm that this the first url is infact the correct 
        # validated = []
        # for each in results:
        #     if each['title']:
        #         print("checking " + each['title'])
        #         validated.append(each['link'])
        # return validated
        return results

#attempts to parse the fee price.
def GetDeliveryFee(Aurl):
    # desktop user-agent
    USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"

    headers = {"User-agent": USER_AGENT}
    resp = requests.get(Aurl, headers=headers)
    
    print('gets to here')
    possiblePrices = []
    print(resp.status_code)
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.content, "html.parser")
        for each in soup.findall("div", {"class" : "al an"}):
            print(each)
            possiblePrices.append(each)
    
    return (possiblePrices)

print(GetDeliveryFee('https://www.ubereats.com/au/sydney/food-delivery/thai-riffic-on-street-parramatta/PHYOQQhHTxuKS7DimVK1tA'))