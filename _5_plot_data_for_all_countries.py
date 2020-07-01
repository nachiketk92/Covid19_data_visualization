#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 15:46:17 2020

@author: nachiketkale
"""
from sqlalchemy import create_engine
import pymysql
import pandas as pd
from _6_Covid_data_visualization import multiple_line_subplots

#Declare connection variables 
host="localhost",
user="root",
passwd="N@ch1ket",
database="covid19"
#Creating database connection object
engine = create_engine("mysql+pymysql://root:N@ch1ket@localhost/covid19") 
con=engine.connect()


#mySQL query 
result=con.execute("select *from country_iso_code ")
#fetching the result of mySQL query
myresult=result.fetchall()
#Converting all data to string
str(myresult)[0:len(myresult)]
#Creating a dataframe
country_df = pd.DataFrame( [[ij for ij in i] for i in myresult] )
country_df.rename(columns={ 0: 'iso_code',1:'country'},inplace=True)
countries=country_df['country'].to_list()

for country in countries:
    #mySQL query
    result=con.execute("select *from covid19_data where country='%s' "%country)
    #fetching the result of mySQL query
    myresult=result.fetchall()
    #Converting all data to string
    str(myresult)[0:len(myresult)]
    #Creating a dataframe
    df = pd.DataFrame( [[ij for ij in i] for i in myresult] )
    df.rename(columns={ 1: 'country',2:'date', 3: 'total_cases', 4: 'new_cases', 5:'total_deaths',6:'new_deaths',7:'total_recovered',8:'active_cases',9:'serious',10:'total_cases_per_million',11:'total_deaths_per_million',12:'total_tests'}, inplace=True)
    multiple_line_subplots(df,country)