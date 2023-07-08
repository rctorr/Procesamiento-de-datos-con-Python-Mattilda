import pandas as pd

df = pd.read_csv("../../Reto-04/rctorr/near_earth_objects-r4.csv", index_col=0)
print(df)

df_1 = df.copy()
# and -> & , or -> |,

filtro_de_peligro = df_1["is_potentially_hazardous_asteroid"] == 1
df_2 = df_1[ filtro_de_peligro  ]
print(df_2)

filtro_por_tamanio = df_1["estimated_diameter.meters.estimated_diameter_max"] > 1_000
df_3 = df_1[ filtro_por_tamanio ]
print(df_3)

df_1["epoch_date_close_approach"] = pd.to_datetime(df_1["epoch_date_close_approach"])
def mes_anio(fecha):  # fecha -> datetime64
    return fecha.year == 1995 and fecha.month == 2

df_4 = df_1[ df_1["epoch_date_close_approach"].map(mes_anio) ]
print(df_4["epoch_date_close_approach"])
