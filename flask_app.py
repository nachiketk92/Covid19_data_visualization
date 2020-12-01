from flask import *
import pymysql
from flask_sqlalchemy import SQLAlchemy
import _1_covid_old_data_ourworldindata , _3_covid_data_scrapping
import pandas as pd
from sqlalchemy import create_engine
from bokeh.plotting import figure
from bokeh import embed
from bokeh_plots import bokeh_line_chart , bokeh_Bar_chart ,bokeh_stacked_bar_chart
#Floas app
app = Flask(__name__)
#Database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:N@ch1ket@localhost/covid19'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)
##########################################
#Creating tables
class Covid19_data(db.Model):
    __tablename__ = 'covid19_data'
    id=db.Column(db.Integer,primary_key=True)
    continent=db.Column(db.String(20))
    country=db.Column(db.String(50))
    date=db.Column(db.DATE)
    total_cases=db.Column(db.Integer)
    new_cases=db.Column( db.Integer)
    total_deaths=db.Column( db.Integer)
    new_deaths=db.Column( db.Integer)
    total_recovered=db.Column( db.Integer)
    active_cases=db.Column( db.Integer)
    serious=db.Column( db.Integer)
    total_cases_per_million=db.Column(db.VARCHAR(length=36))
    total_deaths_per_million=db.Column(db.VARCHAR(length=36))
    total_tests=db.Column( db.Integer)
class Country_iso_code(db.Model):
    __tablename__ = 'country_iso_code'
    id=db.Column(db.Integer,primary_key=True)
    iso_code=db.Column(db.VARCHAR(15))
    country=db.Column(db.String(50))
db.create_all()
#Specifing database login and connection requirments
host='localhost'
user = 'root'
password = 'N@ch1ket'
db = 'covid19'
#Creating database connection object
connectionObject=pymysql.connect(host=host,user=user,password=password,db=db, use_unicode=True, charset='utf8')
##########################################
db_connection_str = 'mysql+pymysql://root:N@ch1ket@localhost/covid19'
db_connection = create_engine(db_connection_str)
##########################################
#Get data from scrapping and upload it to database
_1_covid_old_data_ourworldindata.ourworldindataToDatabase()
_3_covid_data_scrapping.dataScrappingWorldometer()
########################################
#Database Queries
#Query for home page data
try:
    #createcursor object
    cursorObject=connectionObject.cursor()
    # SQL query string
    sqlQuery = """SELECT tt.* from covid19_data tt
                      INNER JOIN
                      (SELECT country, MAX(date) AS Ddate  FROM covid19_data GROUP BY country)groupedtt
                      ON tt.country= groupedtt.country 
                      AND tt.date = groupedtt.Ddate
                       """
    # Execute the sqlQuery
    cursorObject.execute(sqlQuery)
    #Fetch all the rows
    worldDataTable = cursorObject.fetchall()
except Exception as e:
    print("Exeception occured:{}".format(e))
finally:
    cursorObject.close()
#Query for continent page data
try:
    #createcursor object
    cursorObject=connectionObject.cursor()
    # SQL query string
    sqlQuery="""select continent,Sum(total_cases),Sum(new_cases) ,Sum(total_deaths),Sum(new_deaths) ,Sum(total_recovered),Sum(active_cases) from covid19_data
                where date=curdate() and continent Is not null
                group by continent"""
    # Execute the sqlQuery
    cursorObject.execute(sqlQuery)
    #Fetch all the rows
    ContinentDataTable = cursorObject.fetchall()
except Exception as e:
    print("Exeception occured:{}".format(e))
finally:
    cursorObject.close()
#Query for country page data
try:
    #createcursor object
    cursorObject=connectionObject.cursor()
    #sql query
    sqlQuery="SELECT country FROM country_iso_code"
    #Execute the Query
    cursorObject.execute(sqlQuery)
    #Fetch all the rows
    countryList=cursorObject.fetchall()
except Exception as e:
    print ("Exception occoured :{}".format(e))
finally:
    cursorObject.close()
##########################################
#Query for bokeh plot for world page
world = pd.read_sql("SELECT  Distinct date,new_cases, total_cases, total_deaths,total_recovered FROM covid19_data where country = 'world' ", con=db_connection)
##########################################
#Creating Bokeh plots for world page
plot1 = bokeh_Bar_chart(world)
plot2 = bokeh_line_chart(world)
##########################################
#route home page
@app.route("/")
def world(): 
    script_new_cases, div_new_cases = embed.components(plot1) 
    script_line,div_line =embed.components(plot2)

    return render_template("world.html",data=worldDataTable,script=script_new_cases,div=div_new_cases,script1=script_line,div1=div_line)
##########################################
#route continent page
@app.route('/continents/',methods=['GET', 'POST'])
def continent():
    continents=['Asia','Africa','Antartica','Europe','Oceania','North America','South America']
    if request.method == "POST":
        country = request.form['continent']
        cursor = connectionObject.cursor()
        # search by country
        cursor.execute("""SELECT  distinct country, date,total_cases,new_cases,total_deaths,new_deaths,total_recovered,
active_cases,serious,total_tests from covid19_data WHERE continent LIKE %s
 order by total_cases desc limit 10""" ,(continent))
        connectionObject.commit()
        toptenCountries = cursor.fetchall()
    return render_template('continent.html', continents=continents,data=ContinentDataTable)
##########################################
#route search page
@app.route('/country/', methods=['GET', 'POST'])
def country():
    if request.method == "POST":
        country = request.form['country']
        cursor = connectionObject.cursor()
        # search by country
        cursor.execute("""SELECT  distinct country, date,total_cases,new_cases,total_deaths,new_deaths,total_recovered,
active_cases,serious,total_cases_per_million,total_deaths_per_million,total_tests from covid19_data WHERE country LIKE %s """,( country))
        connectionObject.commit()
        data = cursor.fetchall()
        
        return render_template('country.html', data=data)
    return render_template('country.html')
##########################################
#rout about this site info
@app.route('/about/')
def about():
    return render_template("about.html")
##########################################
#Driver code for the flask app   
if __name__ == "__main__":
    app.run(debug=True)