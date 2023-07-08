import pandas as pd
import requests
import sys
import time

url = "https://api.nasa.gov/neo/rest/v1/neo/browse/"
token = "EtSDBzChRyQL87tRvf6vAemUDFCJujscffspj9i5"
parametros = {
    "api_key": token,
}

# Obtener 100 página | for(i=0; i<=100; i++)
df_paginas = []
for i in range(100):
    try:
        resultado = requests.get(url, params=parametros, timeout=5)
    except requests.exceptions.Timeout as error:
        print(f"Error en la consulta de la página 0")
        print(error)
    except requests.exceptions.ConnectionError as error:
        print("El servidor utilizado no existe")
        sys.exit(1)
    if resultado.status_code == requests.codes.ok:
        # Tenemos dados
        print(i, resultado.status_code, url)
        data = resultado.json()
        objetos = data["near_earth_objects"]  # Extraer la lista de objetos de la página
        df = pd.json_normalize(objetos)
        df_paginas.append(df)
        url = data["links"]["next"]  # Obtenemos el link para la consulta de la siguiente página
    else:
        print("Error en la consulta a la API")
    time.sleep(0.5)

df_final = pd.concat(df_paginas, axis=0)
print(df_final.shape)

df_final.to_csv("nasa-final.csv")
