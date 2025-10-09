import pandas as pd
import sqlite3
import glob
import matplotlib.pyplot as plt


#load sales data from csv to df:
sales_df=pd.read_csv('LA_Retail_Sales.csv')
print (sales_df.head())
sales_df.info()

#clean headers (replace blanks with underscores):
sales_df.columns = sales_df.columns.str.lower().str.replace(" ", "_")
print (sales_df.head())

#get multiple sales files from a folder and add them to a df:
file_paths=glob.glob('LA_Retail_Sales_By_Day/*.csv')
print (file_paths)

sales_df2= pd.concat([pd.read_csv(fp) for fp in file_paths], ignore_index=True)
print (sales_df2.head())
sales_df2.info()

#read only specific files from the folder (first 5 files)
sales_df = pd.DataFrame()  #create an empty data frame
for day in range(1,6):
    print(day)
    #read files in the format sales_2024-09-xx.csv to day_df:
    day_df=pd.read_csv(f"LA_Retail_Sales_By_Day/sales_2024-09-{day:02d}.csv")
    sales_df=pd.concat([sales_df, day_df])
    print (len(sales_df))
print(sales_df.head())

#load from json files (key value pairs - like a python dictionary)
sales_df = pd.read_json("LA_Retail_Sales.json", lines = True)
print ('df from json: ', sales_df.head())

#load from parquet files 
sales_df = pd.read_parquet("LA_Retail_Sales.parquet")
print ('df from parquet: ', sales_df.head())

#load from a database (extract from SQL)
conn=sqlite3.connect("la_sales.sqlite")
sales_df=pd.read_sql("SELECT * FROM Sales", con=conn)
print ('df from sqlite db: ', sales_df)

#load from a database and aggregate:
#''' so I can do multiline sql
sales_df=pd.read_sql('''    
    SELECT store_id, sum(dollar_sales) AS total_sales
    FROM Sales
    GROUP BY store_id
    ORDER BY total_sales DESC

''', con=conn)
print ('df from sqlite db again: ', sales_df)


#plot - this doesn't work in vscode, most likely in colab:
print ('bar chart: ', sales_df.plot.bar())
