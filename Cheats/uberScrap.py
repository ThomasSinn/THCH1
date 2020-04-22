#scraper api for uber eats using beautiful soup api
import urllib
import requests
from bs4 import BeautifulSoup
from selenium import webdriver                    # Import module 
from selenium.webdriver.common.keys import Keys #for Chrome driver preferences
from selenium.webdriver.chrome.options import Options
from time import sleep

#opens a chrome web browser to parse delievery fee information
#current issue: uber eats keeps asking for an address. May need to code in a
#means of entering in UNSW as an address when necessary.
def seldrive(Aurl):

    browser = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver') 
    #my own path variable will need to be updated to work on
    #other people's systems.

    browser.get(Aurl)
    sleep(0.5)



    print(browser.find_element_by_tag_name('h1'))
    results = browser.find_element_by_class_name("al an").get_attribute('innerText')
    #results = browser.find_element_by_class_name('dg dh di b7').get_attribute("innerText")



    return results

    



#uses google to find the ubereats link
#currently needs to be improved to make sure it is the correct store
#as well as an uber eats link
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
#Not functional due to uber anti-scrape protection
# def GetDeliveryFee(Aurl):
#     # desktop user-agent
#     USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"

#     headers = {"User-agent": USER_AGENT}
#     resp = requests.get(Aurl, headers=headers)
    
#     print('gets to here')
#     possiblePrices = []
#     print(resp.status_code)
#     if resp.status_code == 200:
#         soup = BeautifulSoup(resp.content, "html.parser")
#         for each in soup.findall("div", {"class" : "al an"}):
#             print(each)
#             possiblePrices.append(each)
    
#     return (possiblePrices)

print(seldrive('https://www.ubereats.com/au/sydney/food-delivery/mcdonalds-kingsford/HtyV4bLOSSe9OIM0ASPhNA'))