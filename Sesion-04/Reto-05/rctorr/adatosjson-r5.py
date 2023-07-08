import pandas as pd

df_newyork = pd.read_json("../../../Datasets/new_york_times_bestsellers-clean.json")
print(df_newyork)
print(df_newyork.columns)

print(df_newyork.head())  # regresan las primeras 5 filas
print(df_newyork.tail(3))  # regresan las ultimas 3 filas
