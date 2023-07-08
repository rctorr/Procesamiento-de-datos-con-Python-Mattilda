import pandas as pd

df = pd.read_csv("../../Reto-03/rctorr/near_earth_objects-reto_3.csv", index_col=0)
print(df.dtypes)
print(df["estimated_diameter.meters.estimated_diameter_max"])

def proporcion_con_tierra(diam_objeto):
    diametro_tierra = 12_742  # en kilómetros
    diametro_tierra_m = diametro_tierra * 1000  # En metros
    return diam_objeto / diametro_tierra_m

df_1 = df.copy()
df_1["proportion_of_max_diameter_to_earth"] = df_1["estimated_diameter.meters.estimated_diameter_max"].apply(
    proporcion_con_tierra
)
print(df_1["proportion_of_max_diameter_to_earth"])

df_1.to_csv("near_earth_objects-reto_4.csv")
