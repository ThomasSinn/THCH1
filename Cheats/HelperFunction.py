#Contains misc. functions to avoid cluter amongst functional code bases

import sqlite3
import random

def FakeOrders(name):
    print("args passed to FakeOrders: " + name)
    conn = sqlite3.connect("database")
    cur = conn.cursor()

    services = ['Uber', 'Deliveroo', 'Easi', 'Doordash']
    
    RID = cur.execute("SELECT RID FROM restaurants WHERE name='{leName}'".format(leName=name)).fetchone()
    # print("RID printed below: \n")
    # print(RID[0])
    # print('\n')
    #need to do a query to get teh rid of the newly created row in res,
    #then bind these services to that rid.
    print("INSERT INTO gigpricing values({TRID}, {service}, {price})".format(TRID=RID[0], service=services[random.randint(0,3)], price=random.randint(0,15)))

    i = 0
    while(i < 4):
        query = "INSERT INTO gigpricing values(NULL,{TRID}, '{service}', {price})".format(TRID=RID[0], service=services[i], price=random.randint(0,15))
        cur.execute(query)
        i += 1
    conn.commit()
    conn.close()
