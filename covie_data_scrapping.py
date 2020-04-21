#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Using the BeautifulSoup library covid 19 tabular data is extracted (Scrapped) from 
worldometer website.
Data modification performed according to requirment and saved in a csv file with time stamp
Created on Tue Apr 14 16:06:44 2020

@author: nachiketkale
"""
# %%
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from  datetime import datetime

#MAke a get request to url
url=requests.get("https://www.worldometers.info/coronavirus/")
# checking the status  
print (url.status_code)
#html.parser is a type of parser we can use different parsers once we know the difference between them
soup=BeautifulSoup(url.content,'html.parser')
table=soup.find('table',id="main_table_countries_today")
get_table_data=table.tbody.find_all("tr")
#creatign  the dictionary to store key value data
dic={}
#extracting ketys of the dict
for i in range(len(get_table_data)):
    # try except to collect all relevant data since for some countries 
    #data is under a tag and for some it is under td tag
    try:
        key=get_table_data[i].find_all("a",href=True)[0].string
    except:
        key=get_table_data[i].find_all("td")[0].string
#extracting values for tkeys        
    values=[j.string for j in get_table_data[i].find_all("td")]

    dic[key]=values

#Transposing the dataframe and storing the data from dictionary in dataframe df
df=pd.DataFrame(dic).iloc[1:,:].T
#Defining new list for countries
column_names=["Total Cases","New Cases","Total Deaths", "New Deaths","Total Recovered","Active Cases","Serious,Critical","Total Cases/1M people","Total Death/1M people","Total Tests","Tests/1M people","Continent"]
# Updating Index name 
df.index_name="Country, Others"
# Updating column names
df.columns=column_names
#Insert new column date with time stamp
df.insert(0,'Date', np.full(214,datetime.date(datetime.now())))
#Make Date column as an index column
df.set_index('Date',inplace=True)
#Create new csv with time stamp and save the dataframe df to it
df.to_csv(datetime.now().strftime('covid_data_worldometer-%Y-%m-%d.csv'))



    
    
    
