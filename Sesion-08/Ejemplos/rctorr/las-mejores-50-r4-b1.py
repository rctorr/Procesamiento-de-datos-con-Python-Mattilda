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

print(df_ratings.groupby("movie_id")["rating"].mean())

df_ratings_media = df_ratings.groupby("movie_id")["rating"].mean()
print(df_ratings_media)
df_ratings_mejores_50 = df_ratings_media.sort_values(ascending=False).head(50)
print(df_ratings_mejores_50)

las_mejores_50 = pd.merge(df_ratings_mejores_50, df_movies, how="left",
                         left_index=True, right_index=True)
print(las_mejores_50)

def plotting_best_50(las_mejores_50):
    import seaborn as sns
    import matplotlib.pyplot as plt

    sns.set_style('darkgrid')
    fig, ax = plt.subplots(figsize=(10, 20))
    ax.set_title('Las mejors 50 películas con las mejores valoraciones')
    splot = sns.barplot(x=las_mejores_50['rating'], y=las_mejores_50['title'], ax=ax)
    ax.set(xlabel='Valoración', ylabel='Título')
    plt.show()

plotting_best_50(las_mejores_50)
