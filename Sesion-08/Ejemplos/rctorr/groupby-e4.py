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
df_users = pd.read_sql("SELECT * FROM users", cnx, index_col="user_id")
print(df_users)

df_occupations = pd.read_csv("csvs/occupations.csv", index_col="occupation_id")
print(df_occupations)

df_ages = pd.read_csv("csvs/age_ranges.csv", index_col="age_id")
print(df_ages)

# JOIN: users(occupation) <-> occupations(index)
# df_users_full = pd.merge(df_users, df_occupations, how="left",
#                          left_on="occupation", right_index=False, right_on="occupation2")
df_users_full = pd.merge(df_users, df_occupations, how="left",
                         left_on="occupation", right_index=True)
df_users_full_1 = df_users_full.rename(columns={"occupation":"occupation_id",
                                                "description":"occupation"})
df_users_full_2 = pd.merge(df_users_full_1, df_ages, how="left",
                           left_on="age", right_index=True)
df_users_full_3 = df_users_full_2.rename(columns={"age":"age_id", "range":"age_range"})
print(df_users_full_3)

print(df_users_full_3.groupby("gender").size())

print(df_users_full_3.groupby("gender")["occupation"].value_counts())

print(df_users_full_3.groupby(["gender", "age_range"])["occupation"].value_counts())

df_groupby_1 = df_users_full_3.groupby(["gender", "age_range"])["occupation"].value_counts()
print(df_groupby_1.loc["F"])
print(df_groupby_1.loc["F", "18-24"])

print(df_users_full_3.groupby("gender")["occupation"].agg(pd.Series.mode))

print(df_users_full_3.groupby("gender")["age_id"].agg(["mean", "median", "std"]))

cursor.close()
cnx.close()