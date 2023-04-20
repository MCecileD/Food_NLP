from google.cloud.sql.connector import Connector, IPTypes
import pg8000
import sqlalchemy
import pandas as pd


# TODO: replace these values with your database connection details
db_password = "foodnlp"
instance_connection_name = "stoked-cosine-382607:europe-west9:foodnlp"
db_host = "34.163.110.13"

# If you followed the Google tutorial, no need to change this
db_name = "foodnlp"
db_user = "postgres"
db_port = "5432"

connector = Connector()

# function to return the database connection
def getconn():
    return connector.connect(
        instance_connection_name,
        "pg8000",
        user=db_user,
        password=db_password,
        db=db_name,
    )

# create connection pool
pool = sqlalchemy.create_engine(
    "postgresql+pg8000://",
    creator=getconn,
)

df_csv = pd.read_csv('zeroshotresult.csv', delimiter=",")
df_csv.to_sql('zeroshotresult8',con=pool)
with pool.connect() as db_conn:

    # query database
    result = db_conn.execute(sqlalchemy.text("SELECT * FROM zeroshotresult8")).fetchall()

    # Do something with the results
    for row in result:
        print(row)

connector.close()