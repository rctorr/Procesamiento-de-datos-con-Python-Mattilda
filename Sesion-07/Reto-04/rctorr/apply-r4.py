import pandas as pd

df = pd.read_csv("../../Reto-03/rctorr/near_earth_objects-r3.csv", index_col=0)
print(df)

df_1 = df.copy()

def proporcion(diametro):
    diametro_tierra = 12_742  # km
    diametro_tierra_m = diametro_tierra * 1000
    return diametro / diametro_tierra_m

print(df_1["estimated_diameter.meters.estimated_diameter_max"])
df_1["proportion_of_max_diameter_to_earth"] = \
    df_1["estimated_diameter.meters.estimated_diameter_max"].apply(proporcion)
print(df_1["proportion_of_max_diameter_to_earth"])

df_1.to_csv("near_earth_objects-r4.csv")
