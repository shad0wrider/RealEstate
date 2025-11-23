import sqlite3 as sql


f = sql.connect("db.db")

k = f.cursor()

k.execute("select * from properties")

print(k.fetchall())