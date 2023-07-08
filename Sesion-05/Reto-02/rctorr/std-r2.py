import pandas as pd
import numpy as np

edades = pd.Series([23, 24, 23, 34, 30, 17, 18, 24, 35, 28, 27, 27, 34, 32,
                    29, 16, 16, 17, 19, 34, 45, 46, 43, 45, 43, 32, 25, 29,
                    28, 38, 30, 37, 38, 24, 26, 25, 24, 19, 19, 18, 17, 18,
                    21, 20, 23, 24, 25, 25, 26, 24, 23, 32, 24, 25, 24, 36,
                    35, 36, 38, 39, 45, 46, 43, 48, 42, 41, 41, 26, 19, 19,
                    19, 20, 39, 38, 43, 28, 27, 39, 43, 52, 50, 38, 15, 17,
                    23, 25, 19, 32, 34, 35, 19, 19, 20, 26, 25, 43, 45, 46,
                    34, 33, 30, 30, 34, 45, 50, 50, 47, 25, 34, 37, 38, 19,
                    19, 20, 25, 28, 34, 32, 36, 39, 39, 28, 34, 33, 22, 25,
                    17, 17, 22, 24, 25, 45, 46, 43, 34, 35, 32, 23])

# Media
media = edades.sum() / edades.count()
print(media)
# Diferencia de x - media
edades_diferencia = edades - media  # -> 23-Xm, 24-Xm, ...
print(edades_diferencia)
edades_media_np = np.subtract(edades, media)  # -> 23-Xm, 24-Xm, ...
print(edades_media_np)

# Elevar al cuadrado la diferencia
edades_cuadrado = edades_diferencia ** 2
print(edades_cuadrado)

# Suma de cuadrados
suma_cuadrados = edades_cuadrado.sum()

# cociente de la raiz
cociente = suma_cuadrados / edades_cuadrado.count()

# Raiz
edades_std = cociente ** (1/2)
edades_std = np.sqrt(cociente)
print(edades_std)

# STD usando Numpy
edades_std_np = np.std(edades)
print(edades_std_np)
