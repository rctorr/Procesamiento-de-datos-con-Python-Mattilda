import pandas as pd

df = pd.read_csv("../../Reto-01/rctorr/near_earth_objects-reto_1.csv", index_col=0)
print(df["orbit_class_description"].loc[0])

df_1 = df.copy()
df_1["orbit_class_description"] = df_1["orbit_class_description"].str.replace("-", " ")
print(df_1["orbit_class_description"])

df_1["orbit_class_description"] = df_1["orbit_class_description"].str.strip()
print(df_1["orbit_class_description"])

print(df_1["id_name"])
df_1[ ["id", "name"] ] = df_1["id_name"].str.split("-", expand=True)
print(df_1.loc[0])

print(df_1["orbiting_body"])
df_1["orbiting_body"] = df_1["orbiting_body"].str.title()
print(df_1["orbiting_body"])

df_1.to_csv("near_earth_objects-reto_2.csv")
