import pandas as pd
from pprint import pprint
import requests
import sys
import time

url = "https://api.nasa.gov/neo/rest/v1/neo/browse"
parametros = {
    "api_key": "EtSDBzChRyQL87tRvf6vAemUDFCJujscffspj9i5",
}
num_paginas = 100

print("\n"*3 + "-"*70)
lista_dfs = []
for npag in range(num_paginas):
    try:
        respuesta = requests.get(url, params=parametros, timeout=5)
    except requests.exceptions.Timeout as er:
        print("El servidor demoró mucho tiempo en dar respuesta")
        print(er)
        sys.exit(1)

    print(f"Procesando página {npag}")
    if respuesta.status_code == requests.codes.ok:
        datos = respuesta.json()
        pprint(datos["links"])
        pprint(datos["page"])
        objetos = datos["near_earth_objects"]
        print(f"Objetos obtenidos {len(objetos)}")
        df = pd.json_normalize(objetos)
        print("Normalizando diccionarios y obteniendo un dataframe ...")
        lista_dfs.append(df)
        print("Agregando dataframe a lista\n")
        url = datos["links"]["next"]
    else:
        print(f"Error en la consulta de la página {npag}")
    time.sleep(1)

df_objetos = pd.concat(lista_dfs, axis=0)
print("Dataframes concatenados")
# pprint(df_objetos)
df_objetos_1 = df_objetos.reset_index(drop=True)
print("Indice reiniciado del dataframe final")
# print(df_objetos_1)
df_objetos_1.to_csv("nasa-p0-99.csv")
print("Dataframe exportado al archivo nasa-p0-99.csv")

print(df_objetos_1.shape)
print(df_objetos_1.dtypes)
print(df_objetos_1.loc[0])
