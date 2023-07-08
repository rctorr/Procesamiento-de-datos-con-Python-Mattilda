from config import *
import pandas as pd
import pyodbc

config = "DRIVER={/opt/microsoft/msodbcsql17/lib64/libmsodbcsql-17.10.so.4.1};SERVER=" + f"{config_db2['host']};"
config += f"DATABASE={config_db2['database']};"
config += f"UID={config_db2['user']};"
config += f"PWD={config_db2['password']};"

cnx = pyodbc.connect(config)
df = pd.read_sql("SELECT * FROM age_ranges", cnx)
cnx.close()
print(df)
