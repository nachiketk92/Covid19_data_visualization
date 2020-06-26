"""
Created on Thu Apr 23 14:42:07 2020
@author: nachiketkale
This function takes one arguments dataframe   
and it loads that dataframe to database as a table
"""
from sqlalchemy import create_engine,MetaData
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