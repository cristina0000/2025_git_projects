#figure out how to export the tables from sqlite to csv files, one file per table
#write queries with joins
#figure out how to trim blanks and dashes from the headers in the csv files or data frames
import sqlite3 # sqlite is included with python
import pandas as pd
import csv
import glob
import os

#open a database connection (sqlite)
#this creates a sqlite database file tutorial.db of initially 0KB
con = sqlite3.connect("tutorialcsv.db")

#create sqlite tables (in the database above) from csv files:

#load the csv file into a Pandas data frame
bus_owners_df = pd.read_csv('Business_Owners.csv')
print("First 5 records:", bus_owners_df.head())
#clean the blanks in the field names (header row)
bus_owners_df.columns = bus_owners_df.columns.str.lower().str.replace(" ", "_")
print("First 5 records:", bus_owners_df.head())
#write the data frame to a sqlite table:
bus_owners_df.to_sql('bus_owners_table', con, if_exists = 'replace', index = False) # could also do append

#load the csv file into a Pandas data frame
bus_licenses_df = pd.read_csv('Business_Licenses.csv')
print("First 5 records:", bus_licenses_df.head())
#clean the blanks in the field names (header row)
bus_licenses_df.columns = bus_licenses_df.columns.str.lower().str.replace(" ", "_")
print("First 5 records:", bus_licenses_df.head())
#write the data frame to a sqlite table:
bus_licenses_df.to_sql('bus_licenses_table', con, if_exists = 'replace', index = False) # could also do append

#load the csv file into a Pandas data frame - once in a data frame I could transform or clean as needed
chicago_df = pd.read_csv('Chicago_Population_Counts.csv') 
print("First 5 records:", chicago_df.head())
#cleanup spaces in the field name in the header row, as otherwise it causes issues:
#chicago_df= chicago_df.rename(columns = {'Population - Total': 'PopulationTotal'})
chicago_df.columns = chicago_df.columns.str.lower().str.replace(" - ", "_")
chicago_df.columns = chicago_df.columns.str.lower().str.replace(" ", "_")
print("First 5 records:", chicago_df.head())
chicago_df.info()

#write the data frame to a sqlite table:
chicago_df.to_sql('chicago_table', con, if_exists = 'replace', index = False) # could also do append

pd.read_sql()

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

for row in cur.execute ("SELECT Year, Geography, population_total FROM chicago_table ORDER BY year"):
    print(row)
con.close()
new_con = sqlite3.connect("tutorialcsv.db")
new_cur = new_con.cursor()

res = new_cur.execute ("SELECT geography, year FROM chicago_table ORDER BY population_total DESC")
geography, year = res.fetchone()
print (f'The highest population is for {geography} in {year}')

#loop through all tables - should do that later
#sql to data frame
chicago_tr_df = pd.read_sql ("SELECT * FROM chicago_table", new_con)
#data frame to csv:
chicago_tr_df.to_csv('Chicago_Population_Counts_Tr.csv', index = False) # .csv extension needs to be included to prevent issue with opening file

#will have to comment this out later:
#new_cur.execute ("DROP TABLE IF EXISTS chicago_table")
new_con.close()






