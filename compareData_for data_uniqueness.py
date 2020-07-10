import pymysql
import pandas as  pd
from sqlalchemy import create_engine

def checkFor_uniquerows(df):
    db_connection_str = 'mysql+pymysql://root:N@ch1ket@localhost/covid19'
    db_connection = create_engine(db_connection_str)
    database_data= pd.read_sql(" SELECT country, date from covid19_data", con=db_connection)

    set(df1['c2']).intersection(set(df2['c2']))








