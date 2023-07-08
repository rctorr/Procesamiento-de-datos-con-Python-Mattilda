import pandas as pd

df = pd.read_csv("../../Reto-04/rctorr/near_earth_objects-reto_4.csv", index_col=0)
print(df.dtypes)

df_1 = df.sort_values("relative_velocity.kilometers_per_second", axis=0)
print(df_1["relative_velocity.kilometers_per_second"])
print(df_1["relative_velocity.kilometers_per_second"].loc[313])

df_2 = df.sort_values("estimated_diameter.meters.estimated_diameter_max", axis=0, ascending=False)
print(df_2["estimated_diameter.meters.estimated_diameter_max"])
print(df_2["estimated_diameter.meters.estimated_diameter_max"].iloc[0])

df.to_excel("near_earth_objects-reto_4.xlsx")
