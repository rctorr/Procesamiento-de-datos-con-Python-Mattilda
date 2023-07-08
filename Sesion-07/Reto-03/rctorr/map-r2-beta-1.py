import pandas as pd

df = pd.read_csv("../../Reto-02/rctorr/near_earth_objects-reto_2.csv", index_col=0)
print(df["is_potentially_hazardous_asteroid"])

conversion = {
    True: 1,
    False: 0
}
df_1 = df.copy()
df_1["is_potentially_hazardous_asteroid"] = df_1["is_potentially_hazardous_asteroid"].map(conversion)
print(df_1["is_potentially_hazardous_asteroid"])

print(df_1["relative_velocity.kilometers_per_hour"])
df_1["relative_velocity.kilometers_per_hour"] = df_1["relative_velocity.kilometers_per_hour"].map(
    lambda x: x / 60
)
print(df_1["relative_velocity.kilometers_per_hour"])

df_1.to_csv("near_earth_objects-reto_3.csv")
