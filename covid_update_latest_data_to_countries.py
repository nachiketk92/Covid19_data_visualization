#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 14:42:07 2020

@author: nachiketkale
"""
import mysql.connector
from sqlalchemy import create_engine
from mysql.connector import Error
import pandas as pd
import pymysql
pymysql.install_as_MySQLdb()

#def DataframetoMysql(dataframe,country):
    #exception handeling
df=pd.read_csv('covid_data_worldometer-2020-04-19.csv')     
    #try:
#create an engine using sqlalchemy
engine = create_engine("mysql+pymysql://root:N@ch1ket@localhost/covid19")
con=engine.connect()

        #create new cursor
#To Create new database
#mycursor.execute("CREATE DATABASE COVIE-19")
#SPECIFY WHICH DATABSE YOU ARE USING
#mycursor.execute("USE COVID-19")

    # Ececute query to create empty table for country
#    for(rows,rs) indataframe.itterrows():
        #rs is series that contains rows of dataframe
mycursor.execute("""CREATE TABLE  Worldometer ( DT DATE PRIMARY KEY, 
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
                                                Tests_Per_Thousand float(7,4) ) """) 
df.to_sql(con=con, name='Worldometer', if_exists='replace')
    #Specify all columns to extract data from row column wise
        #example col_name=rs[0] and so on for each column
#        Date=rs[0]
#        Total_Cases=rs[2]
#        New_Cases=rs[3]
#        Total_Deaths=rs[4]
#        New_Deaths=rs[5]
#        Total_Recovered=rs[6]
#        Active_Cases=[7]
#        Critical =rs[8]
#        Cases_1M=rs[9]
#        Deaths_1M=rs[10]
#        Total_Tests=rs[11]
#        Tests_Thousans=rs[12]
        
        #sql query
#        query="INSERT INTO {}("+ Date +","+ Total_Cases +","+ New_Cases +","+ Total_Deaths +","+ New_Deaths +","+ Total_Recovered +","+ Active_Cases +","+ Critical +","+ Cases_1M +","+ Deaths_1M +","+ Total_Tests +","+ Tests_Thousands +")"
        #execute query
#        mycursor.execute(query)
mydb.commit()
mycursor.close()
    #except Error as e:
     #   print ("error in mysql connection =",e)
    #finally:
    #    mydb.close()
        
        