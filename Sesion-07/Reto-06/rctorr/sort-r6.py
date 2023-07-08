import pandas as pd

df = pd.read_csv("../../Reto-04/rctorr/near_earth_objects-r4.csv", index_col=0)
print(df)
print(df.dtypes)

df_1 = df.sort_values("relative_velocity.kilometers_per_second", ascending=True)
print(df_1["relative_velocity.kilometers_per_second"])
print(df_1["relative_velocity.kilometers_per_second"].loc[313])
print(df_1["relative_velocity.kilometers_per_second"].iloc[0])


df_2 = df.sort_values("estimated_diameter.meters.estimated_diameter_max", ascending=False)
print(df_2["estimated_diameter.meters.estimated_diameter_max"].iloc[0])

# 6516.88, José, Damian, Rctorr
