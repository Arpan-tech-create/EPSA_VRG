import sqlite3

con=sqlite3.connect('sac')

cur=con.cursor()

cur.execute("SELECT * FROM occupy")

rows=cur.fetchall()

for row in rows:
    print(row)

con.close()