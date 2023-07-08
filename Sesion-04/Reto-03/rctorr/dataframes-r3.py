import pandas as pd

datos_productos = {
    "nombre": ["Pokemaster", "Cegatron", "Pikame Mucho", "Lazarillo de Tormes", "Stevie Wonder", "Needle", "El AyMeDuele"],
    "precio": [10000, 5500, 3500, 750, 15500, 12250, 23000],
    "peso": [1.2, 1.5, 2.3, 5.5, 3.4, 2.4, 8.8],
    "capacidad de destrucción retinal": [3, 7, 6, 8, 9, 2, 10],
    "disponible": [True, False, True, True, False, False, True]
}

indice = [1, 2, 3, 4, 5, 6, 7]

df_productos = pd.DataFrame(datos_productos, index=indice)
print(df_productos)

pm_sw = df_productos.loc[ [3,5] ]
print(pm_sw)

p4_final = df_productos.loc[4:]
print(p4_final)

pm_lt_pp = df_productos.loc[[3,4], ["nombre", "precio", "peso"]]
print(pm_lt_pp)

todas_filas = df_productos.loc[:, ["nombre", "precio", "peso"]]
print(todas_filas)