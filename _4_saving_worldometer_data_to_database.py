#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 12:42:49 2020

@author: nachiketkale
"""

import pandas as pd
from sqlalchemy import create_engine


def DataframetoMysql(df):
    #create an engine using sqlalchemy
    engine = create_engine("mysql+pymysql://root:N@ch1ket@localhost/covid19") 
    con=engine.connect()
    try:
        df.to_sql(name='covid19_data',con=con, if_exists='append',index=False)
    except ValueError as vx:
        print(vx)
    except Exception as ex:
        print (ex)
    finally:
        con.close()