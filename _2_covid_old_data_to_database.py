#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 14:42:07 2020

@author: nachiketkale

This function takes one arguments dataframe   
and it loads that dataframe to database as a table
"""
from sqlalchemy import *

import pandas as pd

def DataframetoMysql(df,name):
    #create an engine using sqlalchemy
    #Add admin account for the root
    engine = create_engine("mysql+pymysql://root:N@ch1ket@localhost/covid19") 
    con=engine.connect()
    metadata =MetaData(engine)
    metadata.create_all(engine)
    #To Create new database
    #mycursor.execute("CREATE DATABASE COVIE-19")
    #SPECIFY WHICH DATABSE YOU ARE USING
    #Creating new table in database
    # Creating mySQL table
    if not engine.dialect.has_table(engine, 'covid19_data'):
        covid19_data= Table ('covid19_data', metadata,
                         Column('iso_code', VARCHAR(15),PRIMARY_KEY=True),
                         Column('country',String(50)),
                         Column('date',DATE),
                         Column('total_cases',Integer),
                         Column('new_cases', Integer),
                         Column('total_deaths', Integer),
                         Column('new_deaths', Integer),
                         Column('total_recovered', Integer),
                         Column('active_cases', Integer),
                         Column('serious', Integer),
                         Column('total_cases_per_million',Float),
                         Column('total_deaths_per_million',Float),
                         Column('total_tests', Integer)
            )
        covid19_data.create()
        covid19_data= Table('covid19_data', metadata, autoload=True)
    
    if not engine.dialect.has_table(engine,'country_iso_code' ):
        country_iso_code= Table('country_iso_code',metadata,
                            Column('iso_code', VARCHAR(15),PRIMARY_KEY=True),
                            Column('country',String(50))
            )
        country_iso_code.create()
        country_iso_code= Table('country_iso_code', metadata, autoload=True)
    

    
    try:
        if name=='covid19_data':
            df.to_sql(name='covid19_data',con=con, if_exists='append',index=False)
        elif name=='country_iso_code':
            df.to_sql(name='country_iso_code',con=con, if_exists='append',index=False)
        else:
            pass
                    
    except ValueError as vx:
        print(vx)
    except Exception as ex:
        print (ex)
    finally:
        con.close()
    
        
        
        
    
        
        