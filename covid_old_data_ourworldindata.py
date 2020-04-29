#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This script downloads the old  data from ourworldindata site, which we can not scrapp from
worldometer and then, splits it according th country names and 
stores it in different csv files with time stamp as an index
Created on Sun Apr 19 17:29:21 2020

@author: nachiketkale
"""
import pandas as pd
import numpy as np
import datetime as dt
import os
import requests
#url from where CSV file is downloaded
url="https://covid.ourworldindata.org/data/owid-covid-data.csv"
# get request to get data from url
req = requests.get(url)
#request the content from url 
url_content = req.content
#opening new cvs file to write the data extracted from url
csv_file = open('owid-covid-data.csv', 'wb')
#write the downloaded content in newly created csv file
csv_file.write(url_content)
# closing the csv file
csv_file.close()
#Re- opening the closed csv file
# The redundency in the operation is there as the download section will be removed in future
df = pd.read_csv("owid-covid-data.csv")
#Dropping specific columns from dataframe which we do not need
df=df.drop(['iso_code','new_cases_per_million','new_tests','total_tests_per_thousand','new_tests_per_thousand','tests_units'], axis=1)
#Inserting multiple empty columns in dataframe
df.insert(6,'Total Recovered', np.full(len(df),np.nan))
df.insert(7,'Active Cases', np.full(len(df),np.nan))
df.insert(8,'Seriouc, Critical', np.full(len(df),np.nan))
#Renaming all the columns
df.columns = ['Countries','Date',"Total Cases","New Cases","Total Deaths", "New Deaths","Total Recovered","Active Cases","Serious,Critical","Total Cases/1M people","Total Death/1M people","Total Tests","Tests/1M people"]
#Changing data type for date column
df['Date']=[dt.datetime.strptime(x,'%Y-%m-%d') for x in df['Date']]
#Make Date column as an index column
df.set_index('Date',inplace=True)
#Defining new list for countries
countries=df['Countries'].unique().tolist()
    
#Defining new function which will take in a country name as an argument and create new csv file
# for each country with updated column name
def csv_for_each_country(Country):
    new_df=df.loc[df['Countries']=='{}'.format(Country)]
    new_df=new_df.drop(['Countries'],axis=1)
    new_df.to_csv('{}.csv'.format(Country))
    
    
 #Creates seperate csv file for each country data   
for i in countries:
    csv_for_each_country(i)
    
 
#To change country names to match the names from worldometer data
existing_names=['United States','United Kingdom','South Korea','United Arab Emirates','Vatican','Central African Republic','Democratic Republic of Congo','Saint Vincent and the Grenadines','Czech Republic','Sint Maarten (Dutch part)','Timor',"Cote d'Ivoire",'Curacao','Macedonia','Cape Verde','Bonaire Sint Eustatius and Saba','Turks and Caicos Islands']
new_names=['USA','UK','S. Korea','UAE','Vatican City','CAR','DRC','St. Vincent Grenadines','Czechia','Saint Martin','Timor-Leste','Ivory Coast','Curaçao','North Macedonia','Cabo Verde','Caribbean Netherlands','Turks and Caicos']
for i in range(len(existing_names)):
    os.rename('{}.csv'.format(countries[countries.index(existing_names[i])]),'{}.csv'.format(new_names[i]) )    
    