# import sqlite3
from config import *
import mysql.connector

# cnx = sqlite3.connect("mi_basededatos.sqlite3")
# user, dbname, pass, host, port
cnx = mysql.connector.connect(**config_db1)
# cnx = mysql.connector.connect(user=config_db1["user"], password=config_db1["password"], )
cursor = cnx.cursor()
cursor.execute("SHOW TABLES")
resultados = cursor.fetchall()
print(resultados)
cursor.close()
cnx.close()