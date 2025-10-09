
import sqlite3 # sqlite is included with python
import pandas as pd
import csv
import glob
import os

#open a database connection
#this creates a sqlite database file tutorial.db of initially 0KB
con = sqlite3.connect("tutorialcsv.db")

#create sqlite tables (in the database above) from csv files:

#load the csv file into a Pandas data frame
bus_owners_df = pd.read_csv('Business_Owners.csv')
print("First 5 records:", bus_owners_df.head())
#write the data frame to a sqlite table:
bus_owners_df.to_sql('bus_owners_table', con, if_exists = 'replace', index = False) # could also do append

#load the csv file into a Pandas data frame
bus_licenses_df = pd.read_csv('Business_Licenses.csv')
print("First 5 records:", bus_licenses_df.head())
#write the data frame to a sqlite table:
bus_licenses_df.to_sql('bus_licenses_table', con, if_exists = 'replace', index = False) # could also do append

#load the csv file into a Pandas data frame - once in a data frame I could transform or clean as needed
chicago_df = pd.read_csv('Chicago_Population_Counts.csv') 
print("First 5 records:", chicago_df.head())
#cleanup spaces in this field name, as otherwise it causes issues:
chicago_df= chicago_df.rename(columns = {'Population - Total': 'PopulationTotal'})
print("First 5 records:", chicago_df.head())
#write the data frame to a sqlite table:
chicago_df.to_sql('chicago_table', con, if_exists = 'replace', index = False) # could also do append


# get a cursor in order to execute SQL statements and fetch results:
cur = con.cursor()

#check that the table was created
res = cur.execute ("SELECT name FROM sqlite_schema")
#this does the same as above
#res = cur.execute ("SELECT name FROM sqlite_master")
print (res)
print (res.fetchall())

#insert values into table manually

#commit after inserting:
con.commit()

#execute a SQL query on the table chicago_table:
result = cur.execute ("SELECT * FROM chicago_table")
print (result)
#print (result.fetchall())
print (result.fetchone())

for row in cur.execute ("SELECT Year, Geography, PopulationTotal FROM chicago_table ORDER BY year"):
    print(row)
con.close()
new_con = sqlite3.connect("tutorialcsv.db")
new_cur = new_con.cursor()

res = new_cur.execute ("SELECT geography, year FROM chicago_table ORDER BY PopulationTotal DESC")
geography, year = res.fetchone()
print (f'The highest population is for {geography} in {year}')

#will have to comment this out later:
#new_cur.execute ("DROP TABLE IF EXISTS chicago_table")
new_con.close()




print("Hello World")
print ("*" *10)

