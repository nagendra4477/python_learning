import pandas as pd

df = pd.DataFrame({
    "date": ["2025-03-11","2025-03-12","2025-03-13"],
    "sales": [10,12,8]
})

df["date"] = pd.to_datetime(df["date"])
#print(df)

df.set_index("date", inplace=True)
# print(df)
#print(df["2021-01-01":"2024-01-02"])
#print(df)
#print(df["2021-01-01":"2024-01-02"])
# print(df.resample("h").sum())
df["previous_day"] = df["sales"].shift(-1)
print(df)