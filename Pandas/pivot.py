import pandas as pd
import pandas as pd

df = pd.DataFrame({
    "date": ["2024-01-01","2024-01-01","2024-01-02","2024-01-02"],
    "product": ["Laptop","Laptop","Mouse","Mouse"],
    "sales": [10,5,40,20]
})

pivot_table = df.pivot_table(
    index="date",
    columns="product",
    values="sales",
    aggfunc="sum"
)


print(pivot_table[pivot_table["Laptop"].isnull()])