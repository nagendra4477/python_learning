import pandas as pd

df = pd.DataFrame({
    "customer_id": [101,102,101,104,105],
    "country": ["IN","US","IN","IN","US"],
    "amount": [2000, 3000, 1500, 4000, 2500],
    "tax": [200, 300, 150, 400, 250]
})


grouped = df.groupby(["country","customer_id"], as_index=False)[["amount","tax"]].sum()

grouped.to_csv("grouped_output.csv")



# This is often preferred for "SQL-style" grouping
grouped = df.groupby("country", as_index=False).agg(total_spent=("amount", "sum"), total_tax=("tax", "mean"))
grouped.to_csv("grouped_output_agg.csv", index=False)        