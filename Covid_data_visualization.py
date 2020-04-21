#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 16:07:45 2020
@author: nachiketkale
"""
# %%
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("Covid_data_worldometer.csv")

# sample slicing and plot for one country
#next step creating a plots class with different methods for different plots
country_data=df.iloc[8,1:7].replace(',','',regex=True).astype(float)
# pie chart for single country
plt.pie(country_data, autopct='%1.1f%%', shadow=True, startangle=240)
plt.title("Percentage chart")
plt.show()
#pie chart for world and continent
World_and_continent_data=df.iloc[7,1:7].replace(',','',regex=True).astype(float)
plt.pie(World_and_continent_data, autopct='%1.1f%%', shadow=True, startangle=240)
plt.title("Percentage chart")
plt.show()
