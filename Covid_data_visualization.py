#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 16:07:45 2020

@author: nachiketkale
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv("covid_data_worldometer-2020-04-19.csv")

# sample slicing and plot for one country 
#next step creating a plots class with different methods for different plots
country_data=df.iloc[8,1:7].replace(',','',regex=True).astype(float)
# pie chart for single country
plt.pie(country_data, autopct='%1.1f%%', shadow=True, startangle=240)
plt.title("Percentage chart")
plt.show()
 
def line_plot (Country):
    
    plot(dates, Total_number) 
    plt.xlabel('Time line')
    
    plt.ylabel('number of people')
    
    plt.title('{}'.format(Country))
    plt.legend()
    plt.show()