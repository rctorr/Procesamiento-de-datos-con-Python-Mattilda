import pandas as pd
from pprint import pprint
import requests
import sys

url = "https://api.nasa.gov/neo/rest/v1/neo/browse/"
token = "EtSDBzChRyQL87tRvf6vAemUDFCJujscffspj9i5"
parametros = {
    "api_key": token,
}

try:
    resultado = requests.get(url, params=parametros, timeout=5)
except requests.exceptions.Timeout as error:
    print(f"Error en la consilta de la página 0")
    print(error)
except requests.exceptions.ConnectionError as error:
    print("El servidor utilizado no existe")
    sys.exit(1)
if resultado.status_code == requests.codes.ok:
    # Tenemos dados
    print(resultado.status_code)
    print(resultado.text[:70])
    print(resultado.content[:70])
    print(resultado.encoding)
    data = resultado.json()
    print( type(data) )
    print( data.keys() )
    pprint( data["links"])
    pprint( data["page"])
    print( type(data["near_earth_objects"]) )
    objetos = data["near_earth_objects"]  # Extraer la lista de objetos de la página
    pprint( objetos[0] )  # Imprimimos el contenido de la data del objeto 0
    df = pd.json_normalize(objetos)
    print(df.shape)
    print(df.dtypes)
    print(df.loc[0])
    df.to_csv("nasa-p0-o0.csv")
    df.to_json("nasa-p0-o0.json")
else:
    print("Error en la consulta a la API")
