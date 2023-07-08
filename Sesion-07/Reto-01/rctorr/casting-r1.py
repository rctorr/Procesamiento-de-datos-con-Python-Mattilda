import pandas as pd

df = pd.read_csv("../../../Datasets/near_earth_objects-jan_feb_1995-dirty.csv", index_col=0)
print(df)
print(df.dtypes)
print(df.loc[0])

df_1 = df.copy()
df_1["relative_velocity.kilometers_per_hour"] = \
    pd.to_numeric( df_1["relative_velocity.kilometers_per_hour"], errors="coerce")
print(df_1.dtypes)
print(df_1.loc[0])
print(df_1["relative_velocity.kilometers_per_hour"].isna().sum())

dict_conver = {
    "close_approach_date": "datetime64[ms]",
}
df_2 = df_1.astype(dict_conver)
print(df_2.dtypes)
print(df_2.loc[0])

df_2["epoch_date_close_approach"] = pd.to_datetime( df_2["epoch_date_close_approach"],
                                                    unit="ms")
print(df_2.dtypes)
print(df_2.loc[0])

df_2.to_csv("near_earth_objects-r1.csv")