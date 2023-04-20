from google.cloud.sql.connector import Connector, IPTypes
import pg8000
import sqlalchemy



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
pool = sqlalchemy.create_engine(
    "postgresql+pg8000://",
    creator=getconn,
)

