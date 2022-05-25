import sqlite3

connection =sqlite3.connect('data.db')
cursor = connection.cursor()

get_users = "SELECT * FROM users"
results = cursor.execute(get_users)

for reng in results:
    print(reng)

connection.commit()

connection.close()
