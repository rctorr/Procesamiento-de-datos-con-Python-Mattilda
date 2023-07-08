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

columna_nueva = [4, 7, 6, 8, 9, 7, 3]
df_productos_mas_columna_nueva = df_productos.copy()
df_productos_mas_columna_nueva["nivel de dolor"] = pd.Series(columna_nueva, index=indice)
print(df_productos_mas_columna_nueva)

precios_descuento = [8000, 4000, 2000, 500, 14000, 10000, 15000]
df_productos_descuento = df_productos.copy()
df_productos_descuento["precio"] = pd.Series(precios_descuento, index=indice)
print(df_productos_descuento)

df_productos_sin_precio_ni_peso = df_productos.drop(columns=["precio", "peso"])
print(df_productos_sin_precio_ni_peso)

precios_descuento_2 = [8000, 4000, 2000, 500, 14000, 10000, 15000]
df_productos_descuento_2 = df_productos.copy()
df_productos_descuento_2["precio"] = precios_descuento_2  # Refactorización
print(df_productos_descuento)
