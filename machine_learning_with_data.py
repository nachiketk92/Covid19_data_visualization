#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 23:07:27 2020

@author: nachiketkale
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#creating cursor object
dataset=pd.read_csv('owid-covid-data.csv')
df=dataset.loc[dataset['location'] == 'Aruba']
x=df.iloc[:,1:4]
y=df.iloc[:,4]

# Taking care of missing data
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer.fit(x[:, 2:4])
x[:, 2:4] = imputer.transform(x[:, 2:4])

# Encoding categorical data
# Encoding the Independent Variable
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

def simple_linear_regression():
    pass
    