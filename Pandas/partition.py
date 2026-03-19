import pandas as pd

df = pd.DataFrame({
    "customer_id":[101,102,103,104,105,106],
    "country":["IN","US","IN","IN","US","US"],
    "amount":[2000,3000,1500,4000,2500,3000],
    "order_date":[
        "2024-01-01",
        "2024-01-02",
        "2024-01-04",
        "2024-01-04",
        "2024-01-05",
        "2024-01-06"
    ]
})

top_rows = df.loc[
    df.groupby("country")["amount"].idxmax()
]

print(top_rows.reset_index(drop=True))
