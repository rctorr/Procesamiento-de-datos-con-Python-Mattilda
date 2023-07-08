import pandas as pd

# Lectura de conjunto de datos en formato CSV
df = ...

# Examinando el DataFrame obtenido
# print(df)
# print(df.dtypes)
# print(df.loc[0])
# print(df.loc[0, "rank.numberInt"])
# print( type(df.loc[0, "rank.numberInt"]) )

# Transformando la columna "rank.numberInt" en int64 usando
# df.astype() y pd.to_numeric()
# df_1 = df.copy()
# df_1["rank.numberInt"] = ...

# Examinando DataFrame resultante
# print( df_1.dtypes )
# print( type(df_1.loc[0, "rank.numberInt"]) )
# print( df_1["rank.numberInt"] )
# print( df_1["rank.numberInt"].isna().sum() )
# print( df_1.shape )

# Eliminando NaNs
# df_2 = ...
# print( df_2["rank.numberInt"].isna().sum() )
# print( df_2.shape )

# Finalmente convirtiendo a int64
# df_3 = df_2.copy()
# df_3["rank.numberInt"] = ...
# print(df_3.dtypes)
# print(df_3["rank.numberInt"])

# Reiniciando el índice debido a las filas eliminadas
# df_4 = ...
# print(df_4["rank.numberInt"])
# print( df_4.shape )

# Realizando conversión a fecha de la columna
# "bestsellers_date.numberLong"
# df_5 = df_4.copy()
# df_5["bestsellers_date.numberLong"] = ...
# print(df_5.dtypes)
# print(df_5["bestsellers_date.numberLong"])

# Lo mismo pero para la columna "published_date.numberLong"
# df_5["published_date.numberLong"] = ...
# print(df_5.dtypes)
# print(df_5["published_date.numberLong"])
