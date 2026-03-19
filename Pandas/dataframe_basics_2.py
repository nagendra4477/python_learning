# example for drop_duplicates and order by in dataframe_basics_2.py
import pandas as pd



data = {
    "customer_id": [1, 2, 3, 4, 5],
    "amount": [100, 150, None, 150, 250],
    "city": ["New York",None, "New York", "Chicago", "New York"],
    "date": ["2024-01-01",None, "2024-01-03", "2024-01-04", "2024-01-05"] 
}



df = pd.DataFrame(data)
#convert date field to datetime
df["date"] = pd.to_datetime(df["date"], errors="coerce") 
df["year"] = df["date"].dt.year.fillna(0).astype(int)

print("Original DataFrame:")
print(df)

# drop_duplicates example
# df_no_duplicates = df.drop_duplicates(subset=["amount"])
# print("\nDataFrame after dropping duplicates:")
# print(df_no_duplicates)

# # order by example
# df_sorted = df.sort_values(by="amount", ascending=False)
# print("\nDataFrame sorted by amount (descending):")
# print(df_sorted)

# df["category"] = "LOW"
# df.loc[df["amount"] > 150, "category"] = "HIGH"
# print("\nDataFrame with category column:")
# print(df)

# import numpy as np

# df["category"] = np.where(df["amount"] > 150, "HIGH", "LOW")
# print("\nDataFrame with category column using np.where:")
# print(df)

# df = (
#     df
#     .assign(tax=df["amount"] * 0.18)
#     .assign(net=lambda d: d["amount"] + d["tax"])
# )

# print("\nDataFrame with tax and net columns:")
# print(df)

# df = df.rename(columns={"amount": "transaction_amount"})

# print(df)

# print(df.isna().sum()) 
# #types of null handling in pandas
# df["amount"] = df["amount"].fillna(0) 
# df["city"] = df["city"].fillna("Unknown")
# print(df)

# print(df.isna().sum()) #

df = df.fillna({"amount": 0, "city": 0, "date":0})
print(df)

print(df.dtypes)

df= df.astype({"customer_id": "int32", "amount": "float64"})
print(df.dtypes)
