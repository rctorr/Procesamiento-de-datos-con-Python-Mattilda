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
df_users = pd.read_csv("csvs/users.csv", index_col="user_id")
df_occupations = pd.read_csv("csvs/occupations.csv", index_col="occupation_id")

print(df_movies.head())
print(df_ratings.head())
print(df_users.head())
print(df_occupations.head(20))

df_ratings_occupation = pd.merge(df_ratings, df_users["occupation"],
                                 how="left", left_on="user_id", right_index=True)
print(df_ratings_occupation.head())

filtro = df_ratings_occupation["occupation"] == 15
df_ratings_scientist = df_ratings_occupation[filtro]
print(df_ratings_scientist.head())

df_ratings_scientist_movies = pd.merge(df_ratings_scientist, df_movies["title"],
                                       how="left", left_on="movie_id", right_index=True)
print(df_ratings_scientist_movies)

movies_ratings_num = df_ratings_scientist_movies.groupby("movie_id").size()
filtro_2 = movies_ratings_num > 50
movies_ratings_mas_50 = movies_ratings_num[filtro_2]
print(movies_ratings_mas_50)
def ratings_mas_50(valor):
    return valor in movies_ratings_mas_50
df_ratings_mas_50 = df_ratings_scientist_movies[
    df_ratings_scientist_movies["movie_id"].map(ratings_mas_50)]
print(df_ratings_mas_50)
movies_ratings_media = df_ratings_mas_50.groupby("title")["rating"].mean()
print(movies_ratings_media)

mean_of_scientists_ratings_sorted = movies_ratings_media.sort_values(ascending=False)

def visualizar_lista(mean_of_scientists_ratings_sorted):
    import matplotlib.pyplot as plt
    import seaborn as sns

    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_title('Ratings promedio de las películas más evaluadas por científicos')
    sns.barplot(x=mean_of_scientists_ratings_sorted, y=mean_of_scientists_ratings_sorted.index, ax=ax)
    ax.set(ylabel='Título', xlabel='Rating Promedio')
    plt.show()
    
visualizar_lista(mean_of_scientists_ratings_sorted)