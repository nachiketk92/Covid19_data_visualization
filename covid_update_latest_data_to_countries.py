#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 14:42:07 2020

@author: nachiketkale
"""

import pandas as pd
import pandasql as sqldf
from  datetime import datetime
import sqlite3
import csv

#df=pd.read_csv('covid_data_worldometer-2020-04-21.csv')
#Country=df['Countries'].unique().tolist()
#df_country=pd.read_csv('{}_data.csv'.format(Country[3]))   
#for i in len(df):
#    row1=df.iloc[[i-1]]
#    df_country=pd.read_csv('{}_data.csv'.format(Country[i]))
#    row2=df_country.iloc[[-1]]
#    if row2
 
conn=sqlite3.connect('covid_19.sqlite')
cur=conn.cursor()