# import sqlite3

# with sqlite3.connect("PhoneBook.db") as db:
#     cursor = db.cursor()


# cursor.execute("""CREATE TABLE IF NOT EXISTS Names(
#                id integer PRIMARY KEY,
#                firstname text,
#                surname text,
#                phonenumber text);""")

# cursor.execute("""INSERT INTO Names(id,firstname,surname,phonenumber)
#                VALUES("1","Simon","Howels","01223 349752")""")
# db.commit()

# cursor.execute("""INSERT INTO Names(id,firstname,surname,phonenumber)
#                VALUES("2","Karen","Phillips","01954 295772)""")

# db.commit()



import sqlite3

with sqlite3.connect("PhoneBook.db") as db:
    cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Names(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               firstname TEXT,
               surname TEXT,
               phonenumber TEXT);""")

cursor.execute("""INSERT OR IGNORE INTO Names(firstname, surname, phonenumber)
               VALUES("Simon", "Howels", "01223 349752")""")

cursor.execute("""INSERT OR IGNORE INTO Names(firstname, surname, phonenumber)
               VALUES("Karen", "Phillips", "01954 295772")""")

db.commit()
