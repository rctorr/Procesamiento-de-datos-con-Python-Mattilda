import pandas as pd
import numpy as np

pd.options.mode.chained_assignment = None  # Investigar???

datos = {
    'precio': [12000, 5500, np.nan, 4800, 8900, np.nan, 1280, 1040, 23100, np.nan, 15000, 13400, np.nan],
    'cantidad_en_stock': [34, 54, None, 78, 56, np.nan, 34, 4, 0, 18, 45, 23, 5],
    'cantidad_vendidos': [120, 34, np.nan, 9, 15, np.nan, 103, np.nan, np.nan, 23, 10, 62, 59],
    'descuentos': [np.nan] * 13
}

df = pd.DataFrame(datos, index=["Pokemaster", "Cegatron", "Pikame Mucho",
                                "Lazarillo de Tormes", "Stevie Wonder", "Needle",
                                "El AyMeDuele", "El Desretinador", "Sacamel Ojocles",
                                "Desojado", "Maribel Buenas Noches", "Cíclope", "El Cuatro Ojos"])

print(df)

# Buscar y contar los NaNs de cada columna
print(df.isna().sum())

# Buscar y contar los NaNs de cada fila
print(df.isna().sum(axis=1))

# Eliminando columna "descuentos"
df_1 = df.drop(columns=["descuentos"])
print(df_1)
# Eliminando filas donde todos los valores son NaNs
df_2 = df_1.dropna(axis=0, how="all")  # Eliminando todos los índices en donde todos los valores son NaNas
print(df_2)
print(df_2.isna().sum(axis=1))  # Suma los NaNs por filas

df_3 = df_2.copy()
df_3["cantidad_vendidos"] = df_3["cantidad_vendidos"].fillna(0)
print(df_3)

df_4 = df_3.dropna(axis=0, how="any")
print(df_4)
