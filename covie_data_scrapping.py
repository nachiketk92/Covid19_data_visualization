#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 16:06:44 2020

@author: nachiketkale
"""
# %%
import requests
import csv
from bs4 import BeautifulSoup
#MAke a get request to url
url=requests.get("https://www.worldometers.info/coronavirus/")
# checking the status  
print (url.status_code)
#html.parser is a type of parser we can use different parsers once we know the difference between them
soup=BeautifulSoup(url.content,'html.parser')
table=soup.find('table',id="main_table_countries_today")
#creating new csv file
filename='Covid_data_worldometer.csv'

#create new variable of csv writer
csv_writer=csv.writer(open(filename,'w'))

#run a for loop to extract table data and save it in csv
for tr in table.find_all('tr'):
    data=[]
    #for extracting the table heading
    for th in tr.find_all('th'):
        data.append(th.text)
        
    if(data):
        print("inserting headers :{}".format(','.join(data)))
        csv_writer.writerow(data)
        continue
    
    #scraping actual table values
    for td in tr.find_all('td'):
        data.append(td.text.strip())
    print (data)
    if (data):
        print("inserting table data: {}".format(','.join(data)))
        csv_writer.writerow(data)
        
    
    
    
