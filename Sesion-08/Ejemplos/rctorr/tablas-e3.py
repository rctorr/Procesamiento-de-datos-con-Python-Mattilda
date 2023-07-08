from config import *
import mysql.connector
from mysql.connector import errorcode
import pandas as pd
from pprint import pprint
import sys

try:
    cnx = mysql.connector.connect(**config_db1)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
    sys.exit(1)  # Salir del script con código de error 1

cursor = cnx.cursor()

# Todos los registro de la tabla users
cursor.execute("SELECT * FROM users")
resultados = cursor.fetchall()
pprint(resultados[:10])
print(cursor.column_names)

df = pd.DataFrame(resultados, columns=cursor.column_names)
df_1 = df.set_index("user_id", drop=True)
print(df_1)
print(df_1.dtypes)
df_1.to_csv("csvs/users.csv")

# Descargando datos de la DB de las tablas:
# age_ranges y occupations
cursor.execute("SELECT * FROM age_ranges")
resultados = cursor.fetchall()
print(cursor.column_names)
df = pd.DataFrame(resultados, columns=cursor.column_names)
df_1 = df.set_index("age_id", drop=True)
print(df_1)
print(df_1.dtypes)
df_1.to_csv("csvs/age_ranges.csv")

df_occupations = pd.read_sql("SELECT * FROM occupations", cnx, index_col="occupation_id")
df_occupations.to_csv("csvs/occupations.csv")
print(df_occupations)

cursor.close()
cnx.close()