import pandas as pd

datos = {
    'producto': ["Pokemaster", "Cegatron", "Pikame Mucho", "Lazarillo de Tormes", "Stevie Wonder", "Needle", "El AyMeDuele", "El Desretinador", "Sacamel Ojocles", "Desojado", "Maribel Buenas Noches", "Cíclope", "El Cuatro Ojos"],
    'precio': [12000, 5500, 2350, 4800, 8900, 6640, 1280, 1040, 23100, 16700, 15000, 13400, 19600],
    'cantidad_en_stock': [34, 54, 36, 78, 56, 12, 34, 4, 0, 18, 45, 23, 5],
    'cantidad_vendidos': [120, 34, 59, 9, 15, 51, 103, 72, 39, 23, 10, 62, 59]
}

df = pd.DataFrame(datos)
print(df)

df_dropped = df.drop(columns=["producto"])
print( df_dropped )

mins = df_dropped.min()
maxs = df_dropped.max()
media = df_dropped.mean()
mediana = df_dropped.median()
std = df_dropped.std()

print("Minimos ----")
print(mins)
print("Máximos ----")
print(maxs)
print("Medias ----")
print(media)
print("Medianas ----")
print(mediana)
print("STDs ----")
print(std)
