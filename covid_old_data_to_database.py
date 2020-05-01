#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 14:42:07 2020

@author: nachiketkale

This function takes one arguments dataframe   
and it loads that dataframe to database as a table
"""
from sqlalchemy import create_engine
import pandas as pd

def DataframetoMysql(df,name):
    #create an engine using sqlalchemy
    engine = create_engine("mysql+pymysql://root:N@ch1ket@localhost/covid19") 
    con=engine.connect()
    #To Create new database
    #mycursor.execute("CREATE DATABASE COVIE-19")
    #SPECIFY WHICH DATABSE YOU ARE USING
    #Creating new table in database
    try:
        df.to_sql(name='%s'%name,con=con, if_exists='fail')
    except ValueError as vx:
        print(vx)
    except Exception as ex:
        print (ex)
    finally:
        con.close()
    
        
        
        
    
        
        