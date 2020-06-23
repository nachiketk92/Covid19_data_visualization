from flask import *
import pymysql
from flask_sqlalchemy import SQLAlchemy
import _1_covid_old_data_ourworldindata



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:N@ch1ket@localhost/covid19'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)
_1_covid_old_data_ourworldindata.ourworldindataToDatabase()
#Specifing database login and connection requirments
host='localhost'
user = 'root'
password = 'N@ch1ket'
db = 'covid19'
#Creating database connection object
connectionObject=pymysql.connect(host=host,user=user,password=password,db=db, use_unicode=True, charset='utf8')


try:
    # Create a cursor object
    cursorObject = connectionObject.cursor()
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
    data = cursorObject.fetchall()

except Exception as e:
    print("Exeception occured:{}".format(e))
finally:
    connectionObject.close()
#route base page
@app.route("/")
def home(): 
    return render_template("home.html",data=data)
#rout about this site info
@app.route('/about/')
def about():
    return render_template("about.html")

#Driver code for the flask app   
if __name__ == "__main__":
    app.run(debug=True)