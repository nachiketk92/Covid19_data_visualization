#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 16:07:45 2020
@author: nachiketkale
"""

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

# Handle date time conversions between pandas and matplotlib
register_matplotlib_converters()



    
def multiple_line_subplots (df,country):
    # Use white grid plot background from seaborn
    sns.set(font_scale=1.5, style="whitegrid")
    #Create figure and plot space (axis object)
    fig, ax = plt.subplots(figsize=(8, 8))
    # Add x-axis and y-axis
    ax.plot(df['date'],df['total_cases'],color='blue')
    ax.plot(df['date'],df['total_deaths'],color='red')
    ax.plot(df['date'],df['total_recovered'],color='green')
    #define legend
    ax.legend(['total_cases','total_deaths','total_recovered'])
    #seting margins so that plot will start from baseline
    ax.margins(x=0)
    # Settitle and labels for axes
    ax.set(xlabel="Date",ylabel="Total Cases",title="%s"%country)
    #autoformat date on x axis
    fig.autofmt_xdate()
    #
    ax.fmt_xdata = mdates.DateFormatter('%Y-%m-%d')
    #specify maximum number of ticks
    ax.xaxis.set_major_locator(plt.MaxNLocator(9))
    #rotate tick by 45 degree for horizontal allignment
    plt.setp(ax.get_xticklabels(), rotation=45, horizontalalignment='right')
    plt.show()
    #save plot with specific file name
    plt.savefig('%s_comparision.png'%country)
    
def single_line_plot(df,country,data_column):
    # Use white grid plot background from seaborn
    sns.set(font_scale=1.5, style="whitegrid")
    #Create figure and plot space (axis object)
    fig, ax = plt.subplots(figsize=(8, 8))
    # Add x-axis and y-axis
    ax.plot(df['date'],df['%s']%data_column,color='blue')
    ax.margins(x=0)
    # Settitle and labels for axes
    ax.set(xlabel="Date",ylabel="data",title="%s"%data_column)
    fig.autofmt_xdate()
    ax.fmt_xdata = mdates.DateFormatter('%Y-%m-%d')
    ax.xaxis.set_major_locator(plt.MaxNLocator(9))
    plt.setp(ax.get_xticklabels(), rotation=45, horizontalalignment='right')
    plt.show()
    plt.savefig('%s_%s.png'%(country,data_column))

def pie_chart():
    #need to get total population of continent
    #plot total population-total cases, total infected, total recovered , total deaths
    #to see the total percentage of population affected in each continet
    #In future add this chart for each country
    
    pass

def bar_chart(df,country):
    fig, ax = plt.subplots(figsize=(10,10))
    ax.bar('date','new_cases',data= df.tail(30),color = "blue")
    ax.margins(x=0)
    ax.set(xlabel="Date",ylabel="Cases",title="New Cases ")
    plt.setp(ax.get_xticklabels(), rotation=45, horizontalalignment='right')
    ax.xaxis.set_major_locator(plt.MaxNLocator(25))
    ax.xaxis.set_major_locator(plt.MaxNLocator(20))
    plt.show()
    plt.savefig('%s_new_cases.png'%(country))
    


















