import pandas as pd

# Leer el dataset en formato CSV

df = pd.read_csv("../../../Datasets/melbourne_housing-raw.csv")
print(df)

print(df.columns)
print(df.info)
print(df.dtypes)
print(df.shape)

print(df.head())
print(df.tail())

# Encontrar los NaNs del dataset
print(df.isnull().sum())

df_1 = df.drop(columns=["BuildingArea", "YearBuilt"])
print("Nans por columnas ---")
print(df_1.isnull().sum(axis=0))  # Cantidad de nulos por columnas
print("Nans por filas ---")
print(df_1.isnull().sum(axis=1))  # Cantidad de nulos por filas

# Eliminando filas donde todos los varoes sean NaNs
df_2 = df_1.dropna(axis=0, how="any")  # axis = 0 -> operación por filas, how="all -> todas las columnas con NaNs
print(df_2.isnull().sum(axis=0))  # Cantidad de nulos por columnas
print(df_2)





