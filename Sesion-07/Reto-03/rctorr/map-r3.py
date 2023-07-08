import pandas as pd

df = pd.read_csv("../../Reto-02/rctorr/near_earth_objects-r2.csv", index_col=0)
print(df)

df_1 = df.copy()
print(df_1["is_potentially_hazardous_asteroid"])
dict_map = {
    True: 1,
    False: 0,
}
df_1["is_potentially_hazardous_asteroid"] = \
    df_1["is_potentially_hazardous_asteroid"].map(dict_map)
print(df_1["is_potentially_hazardous_asteroid"])

print(df_1["relative_velocity.kilometers_per_hour"])
def kmh_to_kmm(velocidad):  # km/h -> km/m
    return velocidad / 60

# df_1["relative_velocity.kilometers_per_minute"] = \
#    df_1["relative_velocity.kilometers_per_hour"].map(kmh_to_kmm)
df_1["relative_velocity.kilometers_per_minute"] = \
    df_1["relative_velocity.kilometers_per_hour"].map(lambda v: v/60)

print(df_1["relative_velocity.kilometers_per_minute"])
print(df_1.dtypes)

df_1.to_csv("near_earth_objects-r3.csv")
