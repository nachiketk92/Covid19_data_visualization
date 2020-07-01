#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Download the old  data from ourworldindata site.(This data is not available on worldometer site from where current data is scrapped.) 
Store data in data base in two different tables. 
_2_covid_old_data_to_databse.py function which appends the data to database.
Created on Sun Apr 19 17:29:21 2020
@author: nachiketkale
"""

import pandas as pd
import numpy as np
import requests
import io
from _2_covid_old_data_to_database import DataframetoMysql

def ourworldindataToDatabase():
    #ourworldin data URL
    url="https://covid.ourworldindata.org/data/owid-covid-data.csv"
    # get ure contenr and decode it 
    req = requests.get(url).content.decode('utf8')
    #read data from csv file and load it to dataframe
    df=pd.read_csv(io.StringIO(req))
    #Dropping specific columns from dataframe which we do not need this columns might be used in future
    df=df.drop(['new_tests_smoothed','continent','new_cases_per_million','new_tests','total_tests_per_thousand','new_tests_per_thousand','tests_units','new_deaths_per_million','new_tests_smoothed', 'new_tests_smoothed_per_thousand', 'stringency_index', 'population', 'population_density', 'median_age', 'aged_65_older', 'aged_70_older', 'gdp_per_capita', 'extreme_poverty', 'cvd_death_rate', 'diabetes_prevalence', 'female_smokers', 'male_smokers', 'handwashing_facilities', 'hospital_beds_per_thousand', 'life_expectancy'], axis=1)
    list1=df.iso_code.unique()
    #Remove null values from list
    list1 = [x for x in list1 if str(x) != 'nan']
    l2=[]
    #Standard length is 3(can be 4 if we are considering World). For loop is extracting values having length >3
    for i in list1:
       if len(i) > 3:
         l2.append(i)
    print(l2)
    #For iso_code>3, only select last 3 chars as country code
    for i, row in df.iterrows():
        old_src = row['iso_code']
        if old_src in l2:
            new_src = old_src[-3:]
            df['iso_code'].values[i] = new_src

    # Hear a specific row which was creating a problem while applending the data to data base is removed
    df=df[df.iso_code!= 'OWID_KOS']
    #Inserting multiple empty columns in dataframe 
    #We need to get the missing data from somewhere in future
    df.insert(7,'total_recovered', np.full(len(df),np.nan))
    df.insert(8,'active_cases', np.full(len(df),np.nan))
    df.insert(9,'serious', np.full(len(df),np.nan))
    #Renaming the column for consistency 
    df=df.rename(columns={"location":'country'})
    #list of country names which are different in old and new data
    existing_names=['United States','United Kingdom','South Korea','United Arab Emirates','Vatican','Central African Republic','Democratic Republic of Congo','Saint Vincent and the Grenadines','Czech Republic','Sint Maarten (Dutch part)','Timor',"Cote d'Ivoire",'Curacao','Macedonia','Cape Verde','Bonaire Sint Eustatius and Saba','Turks and Caicos Islands']
    new_names=['USA','UK','S. Korea','UAE','Vatican City','CAR','DRC','St. Vincent Grenadines','Czechia','Saint Martin','Timor-Leste','Ivory Coast','Curaçao','North Macedonia','Cabo Verde','Caribbean Netherlands','Turks and Caicos']
    #change the name of countries as needed to match with future data
    for i in range(len(existing_names)):
        df=df.replace(existing_names[i],new_names[i])
   # saving country code and country name to database with new table    
    total_df=df[['iso_code','country']].copy().drop_duplicates('country').dropna()
    total_df=total_df[total_df.country!='International']
    total_df=total_df[total_df.country!='World']
    total_df=total_df.reset_index(drop=True)
    DataframetoMysql(total_df,'country_iso_code')
    #Saving total data to database
    #drop country column in future once auto update by getting country_code and dropping country column in woldometer is done
    data=df
    data = data[data['iso_code'].notna()]
    data=data.loc[:, data.columns != 'iso_code']
    data=data.reset_index(drop=True)
    DataframetoMysql(data,'covid19_data')
