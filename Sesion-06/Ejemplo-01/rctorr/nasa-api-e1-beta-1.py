import pandas as pd
from pprint import pprint
import requests
import sys

url = "https://api.nasa.gov/neo/rest/v1/neo/browse"
parametros = {
    "api_key": "EtSDBzChRyQL87tRvf6vAemUDFCJujscffspj9i5",
}

print("\n"*3 + "-"*70)
try:
    respuesta = requests.get(url, params=parametros, timeout=5)
except requests.exceptions.Timeout as er:
    print("El servidor demoró mucho tiempo en dar respuesta")
    print(er)
    sys.exit(1)

print(respuesta.status_code)

if respuesta.status_code == requests.codes.ok:
    # print(respuesta.text)
    # print(respuesta.content)
    # print(respuesta.encoding)
    # print(respuesta.json())
    datos = respuesta.json()
    print(type(datos))
    print(datos.keys())
    pprint(datos["links"])
    pprint(datos["page"])
    print(type(datos["near_earth_objects"]))
    # pprint(datos["near_earth_objects"][:2])
    objetos = datos["near_earth_objects"]
    print(len(objetos))  # 20 ?
    df = pd.json_normalize(objetos)
    print(df.head())
    print(df.loc[0])
    df.to_csv("nasa-p0.csv")
    print("Se ha creado el archivo: nasa-p0.csv")
else:
    print("Error en la consulta")
