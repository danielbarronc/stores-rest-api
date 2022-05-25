import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

#item = {'name': 'piano', 'price': 20.99}

#query = "INSERT INTO items VALUES (?, ?)"
query = "SELECT * FROM items"
#cursor.execute(query, (item['name'], item['price']))
datos = cursor.execute(query)

for reng in datos:
    print(reng)
#connection.commit()
connection.close()
