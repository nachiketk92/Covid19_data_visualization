from bokeh.plotting import *
from bokeh.models import HoverTool,Axis
from bokeh.layouts import row
from bokeh.palettes import Spectral3
from bokeh.embed import components
import pandas as pd
import datetime 


def worldData_Bar_chart(df):
    output_file('worldplot.html')
    #calculate date you want to start with
    lastdayfrom = datetime.date.today() + datetime.timedelta(-30)
    df['date']= pd.to_datetime(df['date'])

    #set index from column Date
    df = df.set_index('date')

    #if datetimeindex isn't order, order it
    df= df.sort_index()

    #last 30 days of data
    df = df.loc[lastdayfrom - pd.Timedelta(days=30):lastdayfrom].reset_index()

    # core object that we will use to create plots..
    p = figure(x_axis_type='datetime',plot_width=800, plot_height=600)

    #Hide y axis grid lines
    p.xgrid.visible = False
    #specify total number of  label ticks on x axis
    p.xaxis[0].ticker.desired_num_ticks = 30
    #Rotate x axis label ticks by 45 degree
    p.xaxis.major_label_orientation = 45
    p.vbar(x='date', top='new_cases', source=df, width=datetime.timedelta(0.5))
    p.add_tools(HoverTool(tooltips=[('date', '@date{%F}'), ("TOTAL", "@new_cases")],formatters={'date': 'datetime'}))
    #Next we add a title and label our axes.
    p.title.text = 'New Cases '
    p.xaxis.axis_label = 'Date'
    p.yaxis.axis_label = 'Number Of Cases'
    yaxis = p.select(dict(type=Axis, layout="left"))[0]
    yaxis.formatter.use_scientific = False

    return p

def worldData_line_chart(df):
    output_file('worldplot.html')
    #calculate date you want to start with
    df['date']= pd.to_datetime(df['date'])
    #set index from column Date
    df = df.set_index('date')
    #if datetimeindex isn't order, order it
    df= df.sort_index()

    # core object that we will use to create plots..
    s1 = figure(x_axis_type='datetime',plot_width=400, plot_height=600)
    s1.line(x='date', y='total_cases', line_width=2, source=df, color=Spectral3[2], legend='Total Cases')
    s1.xgrid.visible = False
    s1.xaxis.major_label_orientation = 45
    s1.add_tools(HoverTool(tooltips=[('date', '@date{%F}'),("Total Cases","@total_cases")],formatters={'date': 'datetime'}))
    s1.title.text = 'World Cases'
    s1.xaxis.axis_label = 'Date'
    s1.yaxis.axis_label = 'Number Of Cases'
    yaxis = s1.select(dict(type=Axis, layout="left"))[0]
    yaxis.formatter.use_scientific = False

    s2 = figure(x_axis_type='datetime',plot_width=400, plot_height=600)
    s2.line(x='date', y='total_deaths', line_width=2, source=df, legend='Total Deaths')
    s2.xgrid.visible = False
    s2.xaxis.major_label_orientation = 45
    s2.add_tools(HoverTool(tooltips=[('date', '@date{%F}'),("Total Deaths","@total_deaths")],formatters={'date': 'datetime'}))
    s2.title.text = 'World Deaths'
    s2.xaxis.axis_label = 'Date'
    s2.yaxis.axis_label = 'Number Of Deaths'
    yaxis = s2.select(dict(type=Axis, layout="left"))[0]
    yaxis.formatter.use_scientific = False

    s3 = figure(x_axis_type='datetime',plot_width=400, plot_height=600)
    s3.line(x='date', y='total_recovered', line_width=2, source=df, legend='Total Recovered')
    s3.xgrid.visible = False
    s3.xaxis.major_label_orientation = 45
    s3.add_tools(HoverTool(tooltips=[('date', '@date{%F}'),("Total Recovered","@total_recovered")],formatters={'date': 'datetime'}))
    s3.title.text = 'World Deaths'
    s3.xaxis.axis_label = 'Date'
    s3.yaxis.axis_label = 'Number Of  Recovered Cases'

    return (row(s1, s2, s3))
