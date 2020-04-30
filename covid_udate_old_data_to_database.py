#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 14:42:07 2020

@author: nachiketkale

This function takes three arguments dataframe and country name  and database_name
and it creates new table for the country with its name as table name and upends dataframeto 
mysql database
"""
from sqlalchemy import create_engine
from mysql.connector import Error
import pandas as pd


def DataframetoMysql(dataframe,country,Database_name):
    df=pd.read_csv('{}.csv').format(country)    
    try:
        #create an engine using sqlalchemy
        engine = create_engine("mysql+pymysql://root:N@ch1ket@localhost/covid19")
        con=engine.connect()
        #To Create new database
        #mycursor.execute("CREATE DATABASE COVIE-19")
        #SPECIFY WHICH DATABSE YOU ARE USING
        mycursor=con.cursor()
        mycursor.execute("USE covid19").format(Database_name)
        #Creating new table in database
        mycursor.execute("""CREATE TABLE  {} ( DT DATE PRIMARY KEY, 
                         Total_Cases int(11), 
                         New_Cases int(11), 
                         Total_Deaths int(11),
                         New_Deaths int(11), 
                         Total_Recovered int(11), 
                         Active_Cases int(11) , 
                         Critical int(11), 
                         Total_Cases_1M_people float(7,4), 
                         Total_Deaths_1M_people float(7,4), 
                         Total_Tests int(11), 
                         Tests_Per_Thousand float(7,4) ) """).format(country)
        df.to_sql(con=con, name='Worldometer', if_exists='replace')
        
        mycursor.close()
    except Error as e:
        print ("error in mysql connection =",e)
    finally:
        mycursor.close()
        
        