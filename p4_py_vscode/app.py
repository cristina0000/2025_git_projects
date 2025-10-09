
import sqlite3
import pandas as pd

#open a database connection
#this creates a database file tutorial.db of initially 0KB
con = sqlite3.connect("tutorial.db")

# get a cursor in order to execute SQL statements and fetch results:
cur = con.cursor()

#create table(s)
#commenting out as it already exists
#cur.execute("CREATE TABLE movie(title, year, score)")
#cur.execute("CREATE TABLE movie2(title, year, score)")

#check that the table was created
res = cur.execute ("SELECT name FROM sqlite_schema")
#this does the same as above
#res = cur.execute ("SELECT name FROM sqlite_master")
print (res)
print (res.fetchall())

#insert values into table movie manually
cur.execute("""
    INSERT INTO movie VALUES
        ('Monty Pythonk and the Holy Grail', 1975, 8.2),
        ('and Now for Something completely Different', 1971, 7.5)
""")
con.commit()

data = [
    ("MOnty Python Live at the Hollywood Bowl", 1982, 7.9),
    ("Monty Python's the meaning of life", 1983, 7.5),
    ("Monty Python the life of Brian", 1979, 8.0),
]
cur.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)
#commit after inserting:
con.commit()

#execute a SQL query on the table movie:
result = cur.execute ("SELECT * FROM movie")
print (result)
print (result.fetchall())

for row in cur.execute ("SELECT year, title FROM movie ORDER BY year"):
    print(row)
con.close()
new_con = sqlite3.connect("tutorial.db")
new_cur = new_con.cursor()

res = new_cur.execute ("SELECT title, year FROM movie ORDER BY score DESC")
title, year = res.fetchone()
print (f'The highest scoring Monty Python movie is {title!r}, releasee in {year}')

#will have to comment this out later:
#new_cur.execute ("DROP TABLE IF EXISTS movie")
new_con.close()


#print("First 5 records:", df.head())

print("Hello World")
print ("*" *10)

