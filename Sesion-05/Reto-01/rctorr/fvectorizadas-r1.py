import numpy as np
import pandas as pd

total_aciertos = 68
aciertos = pd.Series([50, 55, 45, 65, 66, 46, 48, 53, 55, 56, 59, 68, 67,
                      60, 45, 56, 66, 64, 59, 55, 34, 45, 49, 48, 55])

#  50 -> 50 / 68 * 100

porcentajes = np.multiply( np.divide(aciertos, total_aciertos), 100 )   # Crear una serie usando numpy
print(porcentajes)
