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
import requests
from _2_covid_old_data_to_database import DataframetoMysql
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
df = pd.read_csv('owid-covid-data.csv')
#Dropping specific columns from dataframe which we do not need
df=df.drop(['new_cases_per_million','new_tests','total_tests_per_thousand','new_tests_per_thousand','tests_units','new_deaths_per_million'], axis=1)
#Inserting multiple empty columns in dataframe
df.insert(7,'total_recovered', np.full(len(df),np.nan))
df.insert(8,'active_cases', np.full(len(df),np.nan))
df.insert(9,'seriouc', np.full(len(df),np.nan))
#
df=df.rename(columns={"location":'country'})
#list of country names which are different in old and new data
existing_names=['United States','United Kingdom','South Korea','United Arab Emirates','Vatican','Central African Republic','Democratic Republic of Congo','Saint Vincent and the Grenadines','Czech Republic','Sint Maarten (Dutch part)','Timor',"Cote d'Ivoire",'Curacao','Macedonia','Cape Verde','Bonaire Sint Eustatius and Saba','Turks and Caicos Islands']
new_names=['USA','UK','S. Korea','UAE','Vatican City','CAR','DRC','St. Vincent Grenadines','Czechia','Saint Martin','Timor-Leste','Ivory Coast','Curaçao','North Macedonia','Cabo Verde','Caribbean Netherlands','Turks and Caicos']
#change the name of countries as needed to match with future data
for i in range(len(existing_names)):
    df=df.replace(existing_names[i],new_names[i])
    
# saving country code and country name to database with new table    
total_df=df[['iso_code','country']].copy()
total_df=total_df.drop_duplicates('country')
total_df=total_df.dropna()
total_df=total_df[total_df.country!='International']
total_df=total_df[total_df.country!='World']
total_df=total_df.reset_index(drop=True)
DataframetoMysql(total_df,'country_iso_code')

#Saving total data to database
#drop country column in future once auto update by getting country_code and dropping country column in woldometer is done
data=df
data = data[data['iso_code'].notna()]
data=data.reset_index(drop=True)
data=data.rename(columns={'seriouc':'serious'})
DataframetoMysql(data,'covid19_data')
        
        
    
    

      