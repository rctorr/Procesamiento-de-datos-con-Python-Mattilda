from config import *
import mysql.connector
from mysql.connector import errorcode
import pandas as pd
import sys

try:
    cnx = mysql.connector.connect(**config_db1)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Usuario o clave inválidos")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("La base de datos no existe")
    else:
        print(err)
    sys.exit(1)

df_movies = pd.read_sql(f"SELECT * FROM movies", cnx, index_col="movie_id")
cnx.close()
df_ratings = pd.read_csv("csvs/ratings.csv", index_col=0)

print(df_movies)
print(df_ratings)

print(df_ratings.groupby("movie_id").size())
print(df_ratings.groupby("movie_id").size().sort_values())
df_ratings_movie_count = df_ratings.groupby("movie_id").size()
filtro = df_ratings_movie_count > 2500
print(df_ratings_movie_count[filtro])
df_movies_mas_2500 = df_ratings_movie_count[filtro]

filtro = df_ratings["movie_id"].apply(
    lambda valor, mas_de_2500: valor in mas_de_2500,
    True, (df_movies_mas_2500.values,))

print(filtro.value_counts())
df_ratings_mas_2500 = df_ratings[filtro]
print(df_ratings_mas_2500)

ratings_filtrados_con_nombre = pd.merge(df_ratings_mas_2500, df_movies,
                                        how="left", left_on="movie_id", right_index=True)
print(ratings_filtrados_con_nombre)

def visualizar_boxplots(ratings_filtrados_con_nombre):
    import seaborn as sns
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_title('Distribución de Ratings de las películas con más de 2500 valoraciones')
    plot = sns.boxplot(x=ratings_filtrados_con_nombre['title'], y=ratings_filtrados_con_nombre['rating'], ax=ax)
    ax.set(xlabel=None, ylabel='Rating')
    plot.set_xticklabels(plot.get_xticklabels(), rotation=90)
    plt.show()

visualizar_boxplots(ratings_filtrados_con_nombre)
