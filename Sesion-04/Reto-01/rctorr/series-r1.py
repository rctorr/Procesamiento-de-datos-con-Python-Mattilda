import pandas as pd

ejecutivo_1 = 'Marco P.'
ejecutivo_2 = 'Jenny'
ejecutivo_3 = 'Britney Baby'
ejecutivo_4 = 'Pepe Guardabosques'
ejecutivo_5 = 'Lombardo El Destructor'

sueldos = pd.Series([10_000.0, 15_000.0, 12_000.0, 20_000.0, 45_000.0],
                    index=[ejecutivo_1, ejecutivo_2, ejecutivo_3, ejecutivo_4, ejecutivo_5])

print('== Sueldos de los principales ejecutivos de EyePoker Inc. ==\n')

print(f'{("Ejecutivo"):25} | {("Sueldo")}')
print('----------------------------------------')
print(f'{ejecutivo_1:25} | ${(sueldos.loc[ejecutivo_1])} MXN')
print(f'{ejecutivo_2:25} | ${(sueldos.loc[ejecutivo_2])} MXN')
print(f'{ejecutivo_3:25} | ${(sueldos.loc[ejecutivo_3])} MXN')
print(f'{ejecutivo_4:25} | ${(sueldos.loc[ejecutivo_4])} MXN')
print(f'{ejecutivo_5:25} | ${(sueldos.loc[ejecutivo_5])} MXN')