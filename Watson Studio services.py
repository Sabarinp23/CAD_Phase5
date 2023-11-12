import ibm_db
from ibm_db import connect
import ibm_db_dbi
db_credentials = {
    "hostname": "your-db-hostname",
    "username": "your-db-username",
    "password": "your-db-password",
    "port": "50000",
    "database": "your-db-name",
    "security": "SSL"
}
ws_credentials = {
    "apikey": "your-api-key",
    "url": "https://api.us-south.dataplatform.cloud.ibm.com"
}
dsn = (
    "DRIVER={{IBM DB2 ODBC DRIVER}};"
    "DATABASE={0};"
    "HOSTNAME={1};"
    "PORT={2};"
    "PROTOCOL=TCPIP;"
    "UID={3};"
    "PWD={4};"
).format(db_credentials["database"], db_credentials["hostname"], db_credentials["port"], db_credentials["username"], db_credentials["password"])

conn = ibm_db.connect(dsn, "", "")
conn_dbi = ibm_db_dbi.Connection(conn)
query = "SELECT * FROM your_table_name"
results = conn_dbi.execute(query).fetchall()
import pandas as pd
import matplotlib.pyplot as plt
df = pd.DataFrame(results, columns=[i[0] for i in conn_dbi.execute(query).description])
df['column_to_plot'].plot(kind='bar')
plt.title("Data Analysis")
plt.xlabel("X-axis Label")
plt.ylabel("Y-axis Label")
plt.show()
conn_dbi.close()