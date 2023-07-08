import pandas as pd

df = pd.read_csv("../../Reto-04/rctorr/near_earth_objects-reto_4.csv", index_col=0)
print(df.dtypes)
print(df["is_potentially_hazardous_asteroid"])

df_hazardous = df[ df["is_potentially_hazardous_asteroid"]==1 ]
print(df_hazardous["is_potentially_hazardous_asteroid"])

df_greater_than_1000 = df[ df["estimated_diameter.meters.estimated_diameter_max"]>1000 ]
print(df_greater_than_1000["estimated_diameter.meters.estimated_diameter_max"])

print(df["epoch_date_close_approach"])
df_1 = df.copy()
df_1["epoch_date_close_approach"] = pd.to_datetime(df_1["epoch_date_close_approach"])
print(df_1["epoch_date_close_approach"])

def feb_1995(fecha):
    return fecha.month == 2 and fecha.year == 1995

df_february = df_1[ df_1["epoch_date_close_approach"].map(feb_1995) ]
print(df_february["epoch_date_close_approach"])

