import db

conn = db.connect()
cur1 = conn.cursor()

cur1.execute(f"""
    SELECT NAME, RID FROM RESTAURANTS
    ;
    """)

dishes = {
    "indian" : [""],
    "american" : [""],
    "chinese" : [""],
    "italian" : [""],
    "local" : [""]
}

for row in cur1.fetchall():
    pass