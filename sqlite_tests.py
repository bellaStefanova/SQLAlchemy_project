import sqlite3

con = sqlite3.connect('database.db')

query = 'SELECT * FROM recipes'
cur = con.cursor()
cur.execute(query)
data = cur.fetchall()
print(data)
