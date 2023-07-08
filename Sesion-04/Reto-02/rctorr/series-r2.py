import pandas as pd

gastos_mensuales = {
    'A': 15000,
    'B': 200000,
    'C': 3250000,
    'D': 120000,
    'E': 135000,
    'F': 55000,
    'G': 100000,
    'H': 25000
}

gastos_serie = pd.Series(gastos_mensuales)
print(gastos_serie)

gastos_D_G = gastos_serie.loc[ ["D", "G"] ]
print(gastos_D_G)

gastos_A_E = gastos_serie.loc[ ["A", "E"] ]
print(gastos_A_E)

gastos_B_F_H = gastos_serie.loc[ ["B", "F", "H", "B"] ]
print(gastos_B_F_H)

gastos_principio_a_E = gastos_serie.loc[:"E"]
print(gastos_principio_a_E)

gastos_C_a_final = gastos_serie.loc["C":]
print(gastos_C_a_final)

gastos_D_a_G = gastos_serie.loc[ "D":"G" ]
print(gastos_D_a_G)
