#sets up the database with dumby data.
import sqlite3
import sys

conn = sqlite3.connect('API')

italianList = ["pizza", "lasagna", "garlic bread", "salad"]
indianList = ['Tika Masala', 'Lamb Rogan Josh', 'Butter Chicken', 'Naan Bread', 'Basamati Rice', 'Jasmine Rice']
chineseList = ['Northern Style Dumplings', 'Southern Style Dumplings', 'Chicken Fried Rice']
cafeList = ['Muffin', 'Bacon and Egg Roll', 'Flat White Coffee', 'English Breakfast Tea']

megaList = [{"type" : "italian", "list" : italianList}, {"type" : "indian", "list" : indianList}, {"type" : "chinese", "list": chineseList}, {"type": "cafe", "list" : cafeList}]

cur = conn.cursor()

for lilList in megaList:
    print('creating tables for {}'.format(lilList['type']))
    for each in lilList['list']:
        print('adding {}'.format(each))
        query = 'INSERT INTO food(item_name, cuisine) VALUES ("{}","{}")'.format(each, lilList['type'])
        cur.execute(query)
        conn.commit()