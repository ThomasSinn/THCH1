import json
import requests

import dbInterface

DETECT_BASE_URL = 'https://google-translate1.p.rapidapi.com/language/translate/v2/detect'
TRANSLATE_BASE_URL = 'https://google-translate1.p.rapidapi.com/language/translate/v2'
HEADERS = {
   'x-rapidapi-host': "google-translate1.p.rapidapi.com",
   'x-rapidapi-key': "26f7215a9cmshfd2f82aff494a97p1af0abjsn648069b4979a",
   'content-type': "application/x-www-form-urlencoded"
   }

# I OLY HAVE 50 FREE REQUESTS PER DAY OTHERWISE THEY CHARGE ME PER REQUEST SO
# PLS DOT SPAM IT >:(

# IDEA IS TO TRANSLATE IT FROM DATABASE AD THEN POPULATE TRASLATED TEXT OTO WEBSITE

def translate_from_database():
    result = dbInterface.ParseDB()
    result = json.loads(result)

    # I get a list of lists
    for x in result:
        print('rid:', x[0])
        print('name:', x[1])
        print('open:', x[2])
        print('')

    # to save umber of requests, put it ito oe strig
    text_to_translate = ''

    # not goig to traslate names sice there is no traslation for it

    # was gonna do somethign but then realised we dont really need to translate
    # names right?? not much to translate o the results page except the open close
    # which is hard coded below


# HARD CODE OF WHAT WE NEED:
q = 'open|closed'

espanol = requests.post(TRANSLATE_BASE_URL, data='q={}&target=es'.format(q), headers=HEADERS)
espanol_words = espanol['data']['translations'][0]['translatedText']
espanol_words = espanol_words.split('|')
ESPANOL_OPEN = espanol_words[0]
ESPANOL_CLOSED = espanol_words[1]

italian = requests.post(TRANSLATE_BASE_URL, data='q={}&target=it'.format(q), headers=HEADERS)
italian_words = italian['data']['translations'][0]['translatedText']
italian_words = italian_words.split('|')
ITALIAN_OPEN = italian_words[0]
ITALIAN_CLOSED = italian_words[1]

german = requests.post(TRANSLATE_BASE_URL, data='q={}&target=ge'.format(q), headers=HEADERS)
german_words = german['data']['translations'][0]['translatedText']
german_words = german_words.split('|')
GERMAN_OPEN = german_words[0]
GERMAN_CLOSED = german_words[1]

def translate_menu_items(menu, target):
    # cant actually test this because theres no meu items in database yet

    #.... but assuming that menu is a list of dictionaries {(food)NAME, PRICE} then:
    # '|' is delimiter

    text_to_translate = ''

    for i in menu:
        text_to_translate = text_to_translate + i['name'] + ' | '

    translated = requests.post(TRANSLATE_BASE_URL, data='q={}&target={}'.format(text_to_translate, target), headers=HEADERS)

    # Now split them back up again

    translated_words = translated['data']['translations'][0]['translatedText']
    translated_words = translated_words.split(' | ')

    translated_menu = []
    for i in len(menu):
        translated_item = {'name': translated_words[i], 'price': menu[i]['price']}
        translated_menu.append(translated_item)

    return translated_menu

def detect(text):

   # url encode text
   long_list_of_words = text.split(' ')
   url_encoded_text = "q={}".format('%20'.join(long_list_of_words))

   # make the request
   r = requests.post(DETECT_BASE_URL, data=url_encoded_text, headers=HEADERS)

   return r.json()

def translate(text, target):
   # url encode text
   long_list_of_words = text.split(' ')
   url_encoded_text = "q={}&target={}".format('%20'.join(long_list_of_words), target)

   r = requests.post(TRANSLATE_BASE_URL, data=url_encoded_text, headers=HEADERS)

   return r.json()

translate_from_database()