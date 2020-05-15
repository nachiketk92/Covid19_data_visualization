#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 15:46:17 2020

@author: nachiketkale
"""
import mysql.connector
import pandas as pd
from Covid_data_visualization import multiple_line_subplots, single_line_plot, pie_chart, bar_chart

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="N@ch1ket",
  database="covid19"
)
#creating cursor object
mycursor = mydb.cursor()
#mySQL query 
mycursor.execute("select *from country_iso_code ")
#fetching the result of mySQL query
myresult = mycursor.fetchall()
#Converting all data to string
str(myresult)[0:len(myresult)]
#Creating a dataframe
country_df = pd.DataFrame( [[ij for ij in i] for i in myresult] )
countries=country_df['country'].to_list()

for country in countries:
    #mySQL query
    mycursor.execute("select *from covid19_data where country='%s' "%country)
    #fetching the result of mySQL query
    myresult = mycursor.fetchall()
    #Converting all data to string
    str(myresult)[0:len(myresult)]
    #Creating a dataframe
    df = pd.DataFrame( [[ij for ij in i] for i in myresult] )
    df.rename(columns={ 1: 'country',2:'date', 3: 'total_cases', 4: 'new_cases', 5:'total_deaths',6:'new_deaths',7:'total_recovered',8:'active_cases',9:'serious',10:'total_cases_per_million',11:'total_deaths_per_million',12:'total_tests'}, inplace=True)
    multiple_line_subplots(df,country)
    single_line_plot(df,country,'total_cases')
    single_line_plot(df,country,'total_deaths')
    single_line_plot(df,country,'total_recovered')
    bar_chart(df,country)
    
