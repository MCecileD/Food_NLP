from flask import Flask, render_template, request
from google.cloud.sql.connector import Connector, IPTypes
import pg8000
import sqlalchemy
import pandas as pd

app = Flask(__name__)

# Mettez les informations de connexion à la base de données ici comme précédemment
db_password = "foodnlp"
instance_connection_name = "stoked-cosine-382607:europe-west9:foodnlp"
db_host = "34.163.110.13"
db_name = "foodnlp"
db_user = "postgres"
db_port = "5432"

connector = Connector()

def getconn():
    return connector.connect(
        instance_connection_name,
        "pg8000",
        user=db_user,
        password=db_password,
        db=db_name,
    )

pool = sqlalchemy.create_engine(
    "postgresql+pg8000://",
    creator=getconn,
)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result')
def result():
    value = request.args.get('value')

    with pool.connect() as db_conn:
        query = "SELECT * FROM emotions_labels7 WHERE emotions = :value"
        result = db_conn.execute(sqlalchemy.text(query), value=value).fetchone()
        new_label = result[2] 
        query_titre = "SELECT title FROM zeroshotresult8 WHERE labels = :new_label"
        result_title = db_conn.execute(sqlalchemy.text(query_titre),new_label=new_label).fetchall()
        query_recette = "SELECT * FROM food_nlp7 WHERE title in (SELECT title FROM zeroshotresult8 WHERE labels = :new_label)"
        result_recette = db_conn.execute(sqlalchemy.text(query_recette),new_label=new_label).fetchall()

    
    if result or result_title is None:
        label = "Unknown"
    else:
        label = result[0]
    
    return render_template('result.html', result=[result,result_title,result_recette])
    
     

@app.route('/recette/<row_id>')
def recette(row_id):
    with pool.connect() as db_conn:
        row = db_conn.execute(sqlalchemy.text("SELECT * FROM food_nlp WHERE index=:row_id"), row_id=row_id).fetchone()
        return render_template('recette.html', recette=row)
    


if __name__ == '__main__':
    app.run(debug=True)